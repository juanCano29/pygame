import mysql.connector
import os
from objects.file import File
from mysql.connector import Error

class Database:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host = 'localhost',
                database = 'ahorcadodb',
                user = 'root',
                password = ''
            )

            if self.db.is_connected():
                self.cursor = self.db.cursor()
                return True
            else:
                return False
        except Error as e:
            return False

    def updateData(self):
        # Actualizar puntajes
        unsavedScoreFile = File('unsaved_score')
        if unsavedScoreFile.count() > 0:
            for row in unsavedScoreFile.getWords():
                row = row.split('|')
                nickname = row[0]
                score = row[1]
                self.cursor.execute("SELECT * FROM jugadores WHERE nickname = %s", (nickname,))
                if len(self.cursor.fetchall()) == 0:
                    self.cursor.execute("INSERT INTO jugadores (nickname) VALUES (%s)", (nickname,))

                self.cursor.execute("INSERT INTO partidas (jugador_id, puntos) VALUES (%s, %s)", (nickname, score))
            unsavedScoreFile.clear()
            self.db.commit()

        self.cursor.execute("SELECT jugadores.nickname, MAX(partidas.puntos) AS maximo," +
            "SUM(partidas.puntos) AS total_pts, COUNT(partidas.id) AS jugadas " +
            "FROM jugadores INNER JOIN partidas ON jugadores.nickname = partidas.jugador_id " +
            "GROUP BY jugadores.nickname ORDER BY maximo DESC, total_pts DESC, jugadas DESC")
        score = self.cursor.fetchall()

        scoreFile = File('score')
        scoreFile.clear()
        for row in score:
            scoreFile.add(row[0] + '|' + str(row[1]) + '|' + str(row[2]) + '|' + str(row[3]))

        # Actualizar archivo de palabras
        self.cursor.execute("SELECT * FROM palabras")
        words = self.cursor.fetchall()

        backup = File('backup')

        #Actualizar palabras
        if len(backup.getWords()) > 0:
            for word in backup.getWords():
                word = word.upper()
                insert = True

                for wordBd in words:
                    if word == wordBd[0]:
                        insert = False
                        break

                if insert:
                    self.cursor.execute("INSERT INTO palabras (palabra) VALUES (%s)", (word,))

            self.db.commit()

            self.cursor.execute("SELECT * FROM palabras")
            words = self.cursor.fetchall()

        backup.clear()
        for word in words:
            backup.add(word[0])

    def updateCat(self):
        file = File('score_cat')
        if file.count() > 0:
            for score in file.getWords():
                row = score.split('|')
                nickname = row[0]
                ganadas = row[1]
                perdidas = row[2]
                jugadas = row[3]
                self.regScorecat(nickname, ganadas, perdidas, jugadas)
            file.clear()
        elif file.count() == 0:
            self.cursor.execute("SELECT jugador_id, partidas_ganadas, partidas_perdidas, partidas_jugadas FROM partidas_gato;")
            scorecats = self.cursor.fetchall()
            for sco in scorecats:
                 file.add(sco[0] + '|' + str(sco[1]) + '|' + str(sco[2]) + '|' + str(sco[3]))

    def regScore(self, nickname, score):
        self.cursor.execute("SELECT nickname FROM jugadores WHERE nickname = '"+(nickname)+"'")

        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO jugadores (nickname) VALUES (%s)", (nickname,))

        self.cursor.execute("INSERT INTO partidas (jugador_id, puntos) VALUES (%s, %s)", (nickname, score))

        self.db.commit()

    def regScorecat(self, nickname, ganadas, perdidas, partidas_jugadas):
        self.cursor.execute("SELECT nickname FROM jugadores WHERE nickname = '" + (nickname) + "'")

        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO jugadores (nickname) VALUES (%s)", (nickname,))

        self.cursor.execute(
            "INSERT INTO partidas_gato (jugador_id, partidas_ganadas, partidas_perdidas, partidas_jugadas) VALUES (%s, %s, %s, %s)",
            (nickname, ganadas, perdidas, partidas_jugadas))

        self.db.commit()

    def getPuntuacionescat(self):
        self.cursor.execute(
            "SELECT nickname, partidas_ganadas, partidas_perdidas, partidas_jugadas FROM partidas_gato INNER JOIN jugadores j ON partidas_gato.jugador_id = j.nickname")
        result = self.cursor.fetchall()
        return result

    def getPuntuaciones(self):
        self.cursor.execute("SELECT jugadores.nickname, MAX(partidas.puntos) AS maximo," +
            "SUM(partidas.puntos) AS total_pts, COUNT(partidas.id) AS jugadas " +
            "FROM jugadores INNER JOIN partidas ON jugadores.nickname = partidas.jugador_id " +
            "GROUP BY jugadores.nickname ORDER BY maximo DESC, total_pts DESC, jugadas DESC")
        result = self.cursor.fetchall()
        return result

    def insertWord(self, word):
        self.cursor.execute("INSERT INTO palabras (palabra) VALUES (%s)", (word,))
        self.db.commit()

    def close(self):
        if (self.db.is_connected()):
            self.cursor.close()
            self.db.close()
