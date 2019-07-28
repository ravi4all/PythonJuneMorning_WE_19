import pygame

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0
screen.fill(white)
x = 0
y = 0
while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # surface,color,[x,y,w,h]
    pygame.draw.rect(screen,red,[0,0,50,50])
    for i in range(10):
        for j in range(5):
            x = i * 100
            y = j * 100
            pygame.draw.circle(screen,red,[x,y],50)

    pygame.display.update()
