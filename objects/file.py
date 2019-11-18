from pathlib import Path
from random import shuffle
import os

class File:
    def __init__(self, file_name):
        path = Path(__file__).parent
        self.file = open((path/'../files/'/'{}.txt'.format(file_name)).resolve(), 'r+')
        self.words = [line.rstrip() for line in
                    self.file]

    def add(self, word):
        self.words.append(word)
        self.writeIn()

    def count(self):
        return len(self.words)

    def clear(self):
        self.words.clear()
        self.writeIn()

    def close(self):
        self.file.close()

    def getWords(self):
        return self.words

    def writeIn(self):
        self.file.truncate(0)
        self.file.seek(0)
        self.file.write('\n'.join(str(line) for line in self.words))

    def writeWithArray(self, words_array):
        self.words = words_array
        self.file.truncate(0)
        self.file.seek(0)
        self.file.write('\n'.join(str(line) for line in words_array))
