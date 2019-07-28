import pygame

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
white = 255,255,255
screen.fill(white)
while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
