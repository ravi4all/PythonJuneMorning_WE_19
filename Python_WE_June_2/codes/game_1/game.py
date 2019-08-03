import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0
blue = 0,0,255
black = 0,0,0

def main():
    FPS = 1000
    clock = pygame.time.Clock()

    barWidth = 170
    barHeight = 20
    barImg = pygame.Surface((barWidth,barHeight))
    barImg.fill(red)
    barRect = barImg.get_rect()
    barRect.x = width / 2 - barWidth/2
    barRect.y = height - barHeight - 10
    moveBarX = 0

    ballRadius = 8
    ballMoveX = 0
    ballMoveY = 0
    moveBall = False
    ballReleased = True

    bricksList = []
    brickWidth = 100
    brickHeight = 30
    row = 5
    col = 9
    for i in range(1,row+1):
        for j in range(1,col):
            brick = pygame.Rect((brickWidth + 5) * j,(brickHeight + 5) * i,
                        brickWidth,brickHeight)
            bricksList.append(brick)

    while True:
        if not moveBall:
            ballX, ballY = barRect.center
            ballY -= barHeight
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        screen.blit(barImg, (barRect.x,barRect.y))

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            moveBarX = 1
        elif keypressed[pygame.K_LEFT]:
            moveBarX = -1
        elif keypressed[pygame.K_SPACE]:
            moveBall = True
        else:moveBarX = 0

        pygame.draw.circle(screen, black, [ballX, ballY], ballRadius)
        ballRect = pygame.Rect(ballX, ballY, ballRadius,ballRadius)

        for i in range(len(bricksList)):
            pygame.draw.rect(screen,blue,bricksList[i])

        for i in range(len(bricksList)):
            if bricksList[i].colliderect(ballRect):
                del bricksList[i]
                ballMoveY = 1
                break

        if moveBall and ballReleased:
            ballMoveX = 1
            ballMoveY = -1
            ballReleased = False

        barRect.x += moveBarX
        ballX += ballMoveX
        ballY += ballMoveY

        if ballX > width - ballRadius:
            ballMoveX = -1
        elif ballX < ballRadius:
            ballMoveX = 1
        elif ballY > height*2:
            moveBall = False
            ballReleased = True
            ballMoveX = 0
            ballMoveY = 0
        elif ballY < ballRadius:
            ballMoveY = 1
        elif ballRect.colliderect(barRect):
            ballMoveY = -1

        pygame.display.update()
        clock.tick(FPS)

main()