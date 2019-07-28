import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0

FPS = 1000
clock = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)

    pygame.display.update()
    clock.tick(FPS)
