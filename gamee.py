import pygame
from pygame.locals import *
from random import choice

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GATO")
done = False
imagen = pygame.image.load('img/tableto.jpg')
# imagen X
x = pygame.image.load('img/X.png')
x = pygame.transform.scale(x, (55, 55))
# imagen O
o = pygame.image.load('img/O.png')
o = pygame.transform.scale(o, (55, 55))
ar = [x, o]
el = choice(ar)
screen.blit(imagen, (0, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9:
                screen.blit(ar[1], (264, 50))
            elif event.key == pygame.K_8:
                screen.blit(ar[0], (175, 50))
            elif event.key == pygame.K_7:
                screen.blit(el, (85, 50))
            if event.key == pygame.K_6:
                screen.blit(el, (264, 125))
            elif event.key == pygame.K_5:
                screen.blit(el, (175, 125))
            elif event.key == pygame.K_4:
                screen.blit(el, (85, 125))
            elif event.key == pygame.K_3:
                screen.blit(el, (264, 200))
            if event.key == pygame.K_2:
                screen.blit(el, (175, 200))
            elif event.key == pygame.K_1:
                screen.blit(el, (85, 200))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
    # Tablerp
    pygame.draw.line(screen, WHITE, (150, 250), (150, 50), 8)
    pygame.draw.line(screen, WHITE, (250, 250), (250, 50), 8)
    pygame.draw.line(screen, WHITE, (75, 115), (320, 115), 8)
    pygame.draw.line(screen, WHITE, (75, 190), (320, 190), 8)
    pygame.display.update()
pygame.quit()