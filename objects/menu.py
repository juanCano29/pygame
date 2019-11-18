from .file import File
from .game import Game
from database.db import Database
from objcat.cGato import Juego
import os
import random
import time
import pygame

class Menu:
    def __init__(self):
        self.nickname = input("Ingresa tu 'nickname': ")

    def show(self):
        print('\nCargando... Por favor espere')

        db = Database()
        backup = File('backup')

        # Opciones CON base de datos
        if db.connect():
            os.system('cls')
            print('>>> EL AHORCADO (x.x) <<< - ' + self.nickname)

            db.updateData()
            backup = File('backup')

            if backup.count():
                print('1. Jugar\n' +
                '2. Ver puntuaciones\n' +
                '3. Agregar palabra (Hay '+str(backup.count())+')\n' +
                '4. Revisar palabras (-.-)\n' +
                '5. Salir\n\nElige una opción: ')

                option = input().lower()

                if option == '1':
                    game = Game('online')

                    while not game.isOver():
                        os.system('cls')
                        print('PALABRAS\t Total: ' + game.getWordTotal() + ' (Punt. máx.) \tRestante: ' + game.getWordCount() +
                        '\n-----------------------------------------------------\n' +
                        '\tNo. de intentos: ' + game.getAtt() + '\tPuntaje: ' + game.getScore() +
                        '\n-----------------------------------------------------' + game.getHanged() + '\n' + game.getWordPrint())

                        print('\n' + game.play(input("\nEscribe una letra ('end' para salir/terminar): ").upper()))
                        input()

                    os.system('cls')
                    print("---------------------" +
                        "| FIN DE LA PARTIDA |" +
                        "---------------------\n" +
                        'Puntaje: ' + game.getScore())

                    if int(game.getScore()) > 0:
                        if db.connect():
                            db.regScore(self.nickname, game.getScore())
                            print("Partida registrada con exito")
                        else:
                            localScore = File('score').add(self.nickname + '|' + game.getScore())
                            print("Partida completada, intenta conectarte al servidor para que sea registrada")
                    input()

                if option == '2':
                    os.system('cls')
                    print('---> Puntuaciones <---\n')
                    score = File('score').getWords()

                    print("JUGADOR \tPUNTAJE MÁX. \tPUNTAJE TOTAL \tPARTIDAS JUGADAS\n")
                    for row in score:
                        row = row.split('|')
                        print(row[0] + '\t\t' + str(row[1]) + '\t\t' + str(row[2]) + '\t\t' + str(row[3]))
                    input()

                elif option == '3':
                    word = input('\nEscribe la palabra a ingresar ("c" para cancelar):\n').upper()

                    if word != 'C':
                        db.insertWord(word)

                elif option == '4':
                    os.system('cls')
                    print('Palabras guardadas (¡Esponja enloqueciste!)\n')

                    for word in backup.getWords():
                        print(word)
                    input()

                elif option == '5':
                    backup.close()
                    db.close()
                    exit()

            else:
                print('1. Agregar palabras para jugar\n' +
                    '2. Salir\n\nElige una opción: ')

                option = input().lower()

                if option == '1':
                    word = input('\nEscribe la palabra a ingresar ("c" para cancelar):\n').upper()

                    if word != 'C':
                        db.insertWord(word)
                elif option == '2':
                    db.close()
                    backup.close()
                    exit()

        # Opciones SIN base de datos
        else:
            os.system('cls')
            print('>>> EL AHORCADO (x.x) <<< - '+self.nickname+'\n' +
                'No hay conexión al servidor\n' +
                'Tus partidas y palabras añadidas se guardarán cuando haya conexión\n')

            backup = File('backup')

            if backup.count():
                print('1. Jugar\n' +
                '2. Ver palabras disponibles\n' +
                '3. Conectarse al servidor\n' +
                '4. Ver puntuaciones\n' +
                '5. Añadir palabras\n' +
                '6. Salir\n\nElige una opción: ')

                option = input().lower()

                if option == '1':
                    game = Game('offline')

                    while not game.isOver():
                        os.system('cls')
                        print('PALABRAS\t Total: ' + game.getWordTotal() + ' (Punt. máx.) \tRestante: ' + game.getWordCount() +
                        '\n-----------------------------------------------------\n' +
                        '\tNo. de intentos: ' + game.getAtt() + '\tPuntaje: ' + game.getScore() +
                        '\n-----------------------------------------------------' + game.getHanged() + '\n' + game.getWordPrint())

                        print('\n' + game.play(input("\nEscribe una letra ('end' para salir/terminar): ").upper()) )
                        input()

                    os.system('cls')
                    print("---------------------" +
                        "| FIN DE LA PARTIDA |" +
                        "---------------------\n" +
                        'Puntaje: ' + game.getScore())

                    if int(game.getScore()) > 0:
                        if db.connect():
                            db.regScore(self.nickname, game.getScore())
                            print("Partida registrada con exito")
                        else:
                            localScore = File('unsaved_score').add(self.nickname + '|' + game.getScore())
                            print("Partida completada, intenta conectarte al servidor para que sea registrada")
                    input()

                if option == '2':
                    os.system('cls')
                    print('Palabras guardadas (¡Esponja enloqueciste!)\n')

                    for word in backup.getWords():
                        print(word)
                    input()

                elif option == '4':
                    os.system('cls')
                    print('---> Puntuaciones <---\n')
                    score = File('score').getWords()

                    print("JUGADOR \tPUNTAJE MÁX. \tPUNTAJE TOTAL \tPARTIDAS JUGADAS\n")
                    for row in score:
                        row = row.split('|')
                        print(row[0] + '\t\t' + str(row[1]) + '\t\t' + str(row[2]) + '\t\t' + str(row[3]))

                    unsavedScore = File('unsaved_score').getWords()

                    if len(unsavedScore):
                        print("\nPartidas por registrar:")
                        for row in unsavedScore:
                            row = row.split('|')
                            print(row[0] + '\t' + str(row[1]))
                    input()

                elif option == '5':
                    word = ''

                    while word.lower() != 'n':
                        word = str(input('\nEscribe la palabra a ingresar ("n" para terminar): '))

                        if word.lower() != 'n':
                            backup.add(word)

                elif option == '6':
                    backup.close()
                    exit()

            else:
                print('1. Agregar palabras para jugar\n' +
                    '2. Salir\n\nElige una opción: ')

                option = input().lower()

                if option == '1':
                    word = ''

                    while word.lower() != 'n':
                        word = str(input('\nEscribe la palabra a ingresar ("n" para terminar): '))

                        if word.lower() != 'n':
                            backup.add(word)

                elif option == '2':
                    backup.close()
                    exit()

        backup.close()
        self.show()

    def playcat():

        pygame.init()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        size = [600, 600]
        gan = 0
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("GATO")

        imagen = pygame.image.load('img/tableto.jpg')
        # imagen X
        x = pygame.image.load('img/X.png')
        x = pygame.transform.scale(x, (55, 55))
        # imagen O
        o = pygame.image.load('img/O.png')
        o = pygame.transform.scale(o, (55, 55))
        screen.blit(imagen, (0, 0))
        obj = Juego()
        done = False
        turn = obj.turnopy
        jugador = 'X'
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        obj.tirada_(pos[0] // 200, pos[1] // 200, turn)
                        if obj.cambio:
                            if turn == obj.x:
                                turn = obj.o
                            else:
                                turn = obj.x
                        print(turn)
                        obj.print_drid()

                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
            # Tablerp
            obj.dibujartablero(screen)
            pygame.display.update()
        pygame.quit()
#         db = Database()
#
#         if db.connect():
#             db.updateCat()
#
#
#         obj = Juego()
#         os.system("cls")
#         print("""
# +-----------------------+
# |----JUEGO DEL GATO-----|
# +-----------------------+
#             """)
#         print("""
# 1) iniciar juego
# 2) ver partidas
# 3) jugar Ahorcado
# 4) salir
#             """)
#         opc = int(input("Opcion: "))
#         if opc == 1:
#             print()
#             gan = 0
#             pe = 0
#             opc = input("Elige 'x' o 'o': ")
#             obj.humano_elige(opc)
#             os.system("cls")
#             op = str(input("Comenzar (s/n): "))
#             while op.lower() == "s":
#                 Partidas = obj.getPartidas_Jugadas()
#                 obj.getTablero()
#                 obj.getEnd_game()
#                 while not obj.end_game:
#                     print("  0 1 2")
#                     for i, ren in enumerate(obj.tablero):
#                         print(i, " ".join([obj.simbolos[v] for v in ren]))
#                     print()
#                     if obj.turno == obj.humano:
#                         print()
#                         resp = input("Tu turno (renglon, columna): ")
#                         obj.turno = obj.pc
#                         if not obj.juega_humano(resp):
#                             print("Esta coordenada esta ocupada")
#                         print()
#                         if obj.gana(obj.humano):
#                             gan += 1
#                             obj.end_game = True
#                     elif obj.turno == obj.pc:
#                         print()
#                         print("\nTurno de la PC!\n")
#                         obj.juega_pc()
#                         if obj.gana(obj.pc):
#                             pe += 1
#                             obj.end_game = True
#                         obj.turno = obj.humano
#                 print("  0 1 2")
#                 for i, ren in enumerate(obj.tablero):
#                     print(i, " ".join([obj.simbolos[v] for v in ren]))
#                 print()
#                 print(obj.getresultados())
#                 op = str(input("Desea iniciar nuevo juego (s/n): "))
#                 if op == "n":
#                     if int(Partidas) > 0:
#                         if db.connect():
#                             db.regScorecat(self.nickname, gan, pe, Partidas)
#                             print("Partida registrada con exito")
#                             time.sleep(3)
#                         else:
#                             File('score_cat').add(self.nickname + '|' + str(gan) + '|' + str(pe) + '|' + str(Partidas))
#                             print("Partida completada, intenta conectarte al servidor para que sea registrada")
#                             time.sleep(3)
#                     else:
#                         input()
#             if op.lower() == "n":
#                 self.playcat()
#
#         if opc == 2:
#             if db.connect():
#                 os.system("cls")
#                 result = db.getPuntuacionescat()
#                 if len(result):
#                     print("JUGADOR \tPARTIDAS GANADAS.\tPARTIDAS PERDIDAS.\tPARTIDAS JUGADAS\n")
#                     for row in result:
#                         print(row[0] + '\t' + '\t' + str(row[1]) + '\t' + '\t' + '\t' + str(
#                             row[2]) + '\t' + '\t' + '\t' + str(row[3]))
#                     input()
#                     self.playcat()
#                 else:
#                     print("Sin Partidas")
#
#             else:
#                 os.system("cls")
#                 score_cat = File('score_cat').getWords()
#                 if len(score_cat):
#                     print("\nPartidas por registrar:\n")
#                     print("JUGADOR \tPARTIDAS GANADAS.\tPARTIDAS PERDIDAS.\tPARTIDAS JUGADAS\n")
#                     for row in score_cat:
#                         row = row.split('|')
#                         print(
#                             row[0] + '\t' + '\t' + str(row[1]) + '\t' + '\t' + '\t' + str(row[2]) + '\t' + '\t' + '\t' + str(row[3]))
#
#                 else:
#                     print("Sin Partidas")
#                 input()
#                 self.playcat()
#
#         if opc == 3:
#             self.show()
#
#         if opc == 4:
#             os.system("exit")

