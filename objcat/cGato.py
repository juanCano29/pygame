import random
import pygame
import os
lx = pygame.image.load(os.path.join('img', 'X.png'))
lx = pygame.transform.scale(lx, (180, 180))
lo = pygame.image.load(os.path.join('img', 'O.png'))
lo = pygame.transform.scale(lo, (180, 180))
class Juego:
    def __init__(self):
        self.lineas_tablero = [((0, 200), (600, 200)),
                               ((0, 400), (600, 400)),
                               ((200, 0), (200, 600)),
                               ((400, 0), (400, 600))]

        self.cambio = True
        self.tablero = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

        self.humano = 1
        self.pc = -1
        self.x = 'X'
        self.o = 'O'
        self.perdidas = 0
        self.ganadas = 0
        self.partidas_jugadas = 0
        self.turno = random.choice([self.humano, self.pc])
        self.turnopy = random.choice([self.x, self.o])
        self.end_game = False
    #     borrar despues

    def print_drid(self):
        for row in self.tablero:
            print(row)

    def Get_celdas_valor(self, x, y):
        return self.tablero[y][x]

    def Set_celdas_valor(self, x, y, valor):
        self.tablero[y][x] = valor

    def tirada_(self, x, y, jugador):
        if self.Get_celdas_valor(x, y) == 0:
            self.cambio = True
            if jugador == self.x:
                self.Set_celdas_valor(x, y, 'X')
            elif jugador == self.o:
                self.Set_celdas_valor(x, y, 'O')
        else:
            self.cambio = False

    def dibujartablero(self, pantalla):
        for line in self.lineas_tablero:
            pygame.draw.line(pantalla, (200, 200, 200), line[0], line[1], 8)

        for y in range(len(self.tablero)):
            for x in range(len(self.tablero)):
                if self.Get_celdas_valor(x, y) == 'X':
                    pantalla.blit(lx, (x*212, y*205))
                elif self.Get_celdas_valor(x, y) == 'O':
                    pantalla.blit(lo, (x*212, y*205))
    # Hasta aqui termina logica pygame

    def getTablero(self):
        self.tablero = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        return self.tablero

    def getEnd_game(self):
        self.end_game = False
        return self.end_game

    def getPerdidas(self):
        return self.perdidas

    def getGanadas(self):
        return self.ganadas

    def getPartidas_Jugadas(self):
        self.partidas_jugadas += 1
        return self.partidas_jugadas

    def humano_elige(self, opc):
        if opc.lower() == "x":
            self.simbolos = [".", "x", "o"]
        elif opc.lower() == "o":
            self.simbolos = [".", "o", "x"]

    def tirada(self, p, j):
        if self.tablero[p[0]][p[1]] == 1 or self.tablero[p[0]][p[1]] == -1:
            self.turno = self.humano
            return False

        self.tablero[p[0]][p[1]] = j
        return True

    def juega_humano(self, resp):
        p = [int(v) for v in resp.split(",")]
        return self.tirada(p, self.humano)

    def Getcasillas_libres(self):
        return [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.tablero[i][j] == 0]

    def juega_pc(self):
        casillas = self.Getcasillas_libres()
        for i in casillas:
            self.tirada(i, self.pc)
            if self.gana(self.pc):
                 return
            else:
                break

        self.tirada(casillas[0], self.pc)

    def gana(self, j):
        for ren in self.tablero:
            if sum(ren) == 3 * j:
                return True
        for col in zip(*self.tablero):
            if sum(col) == 3 * j:
                return True
        x1 = [ren[i] for i, ren in enumerate(self.tablero)]
        if sum(x1) == 3 * j:
            return True
        x2 = [ren[2 - i] for i, ren in enumerate(self.tablero)]
        if sum(x2) == 3 * j:
            return True

    def getresultados(self):
        if self.gana(self.humano):
            msn = "Has Ganado La partida"
        elif self.gana(self.pc):
            msn = "la pc Gana"
        else:
            msn = "Empate"
        return msn
