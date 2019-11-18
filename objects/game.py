from .file import File
from database.db import Database
from game_tools.hanged import Hanged
import random
import string

class Game:
    def __init__(self, gameMode):
        self.att = 5
        self.gameMode = gameMode
        self.score = 0
        self.words = File('backup').getWords()

        random.shuffle(self.words)

        self.word_total = len(self.words)
        self.word_count = self.word_total
        self.currentWord = self.words.pop().upper()
        self.wordPrint = self.createWordPrint()

    def createWordPrint(self):
        wordPrint = ''

        pista = random.choice(string.ascii_uppercase)
        showPista = False

        while showPista == False:
            for char in self.currentWord:
                if pista == char:
                    showPista = True
                    break

                pista = random.choice(string.ascii_uppercase)

        for char in self.currentWord:
            if pista == char:
                wordPrint += pista
                continue

            wordPrint += '_'

        return wordPrint

    def getAtt(self):
        return str(self.att)

    def getHanged(self):
        return Hanged.get(self.att)

    def getScore(self):
        return str(self.score)

    def getWordCount(self):
        return str(self.word_count)

    def getWordPrint(self):
        return " ".join(self.wordPrint)

    def getWordTotal(self):
        return str(self.word_total)

    def isOver(self):
        if self.att <= 0 or self.word_count <= 0:
            return True

        return False

    def play(self, letter):
        if letter == 'END':
            self.att = 0
            return 'Terminaste el juego'

        lostAttempt = True
        wpList = list(self.wordPrint)
        msj = "¡Ups!, algo salió mal D:"

        i = 0
        for char in self.currentWord:
            if letter == self.wordPrint[i]:
                return "Letra ya encontrada, intenta con otra"

            if letter == char:
                msj = "¡Letra '" + letter + "' encontrada!"
                lostAttempt = False
                wpList[i] = letter

            i += 1

        if lostAttempt:
            self.att -= 1
            return "Letra incorrecta D:"

        self.wordPrint = ''.join(wpList)

        if self.wordPrint == self.currentWord:
            msj = "Palabra '" + self.currentWord + "' completada, ¡Has conseguido un punto! :D"
            self.word_count -= 1
            self.score += 1
            self.att = 5

            if len(self.words) > 0:
                self.currentWord = self.words.pop().upper()
                self.wordPrint = self.createWordPrint()

        return msj
