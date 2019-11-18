from objects.menu import Menu

import os
import pygame
from pygame.locals import *
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
AM = (255, 255, 0)
RED = (255, 0, 0)
tamaño = [700, 500]
basicFont = pygame.font.SysFont(None, 48)
pantalla = pygame.display.set_mode(tamaño)
pygame.display.set_caption("Menu")
fuente = pygame.font.Font(None, 50)
text = "Menu de Juegos"
mensaje = fuente.render(text, 1, GREEN)
done = False
imagen = pygame.image.load('img/menu.jpg')
pantalla.blit(imagen, (0, 0))
text = basicFont.render('Ahorcado', True, BLACK)
textRect = text.get_rect()
textRect.centerx = pantalla.get_rect().centerx
textRect.centery = pantalla.get_rect().centery+60
text2 = basicFont.render('    Gato    ', True, WHITE)
textRect2 = text2.get_rect()
textRect2.centerx = pantalla.get_rect().centerx
textRect2.centery = pantalla.get_rect().centery-30
while not done:
    pantalla.blit(mensaje, (235, 110))
    cu1 = pygame.draw.rect(pantalla, AM, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
    pantalla.blit(text, textRect)
    cu2 = pygame.draw.rect(pantalla, BLUE, (textRect2.left - 20, textRect2.top - 20, textRect2.width + 40, textRect2.height + 40))
    # draw the text onto the surface
    pantalla.blit(text2, textRect2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cu1.collidepoint(event.pos):
                pygame.quit()
            elif cu2.collidepoint(event.pos):
                Menu.playcat()
    pygame.display.update()
pygame.quit()