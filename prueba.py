
import pygame
import random
from pygame.locals import *

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

def dibujar_panel():
    panel = pygame.transform.scale(imagen_panel, [560, 420])
    pantalla.blit(panel, [20, 20])

def dibujar_botones(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])

def main():
    game_over = False
    click = False
    clock = pygame.time.Clock()
    rect_boton_1 = imagen_boton.get_rect()
    botones = []
    rect_boton_1.topleft = [80, 80]
    botones.append(
        {'texto': "Nuevo número", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': rect_boton_1,
         'on_click': True})
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
        pantalla.fill(FONDO)
        dibujar_panel()
        dibujar_botones(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

pygame.init()
dimensiones = [600, 460]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Entrada de texto")
imagen_panel = pygame.image.load("img/tableto.jpg")
imagen_boton = pygame.image.load("../img/button.png")
imagen_boton_pressed = pygame.image.load("../img/buttonPressed.png")

if __name__ == '__main__':
    main()

#
# import pygame as pg
#
#
# def main():
#     screen = pg.display.set_mode((640, 480))
#     font = pg.font.Font(None, 32)
#     clock = pg.time.Clock()
#     input_box = pg.Rect(100, 100, 140, 32)
#     color_inactive = pg.Color('lightskyblue3')
#     color_active = pg.Color('dodgerblue2')
#     color = color_inactive
#     active = False
#     text = ''
#     done = False
#
#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 # If the user clicked on the input_box rect.
#                 if input_box.collidepoint(event.pos):
#                     # Toggle the active variable.
#                     active = not active
#                 else:
#                     active = False
#                 # Change the current color of the input box.
#                 color = color_active if active else color_inactive
#             if event.type == pg.KEYDOWN:
#                 if active:
#                     if event.key == pg.K_RETURN:
#                         print(text)
#                         text = ''
#                     elif event.key == pg.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode
#
#         screen.fill((30, 30, 30))
#         # Render the current text.
#         txt_surface = font.render(text, True, color)
#         # Resize the box if the text is too long.
#         width = max(200, txt_surface.get_width()+10)
#         input_box.w = width
#         # Blit the text.
#         screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#         # Blit the input_box rect.
#         pg.draw.rect(screen, color, input_box, 2)
#
#         pg.display.flip()
#         clock.tick(30)
#
#
# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()
#
