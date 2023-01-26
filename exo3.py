import sqlite3

#read lines of the txt file and store them in list
file_input = open('input.txt', 'r')

for line in file_input:
    input = line.split("|")
    artist_name = input[0]
    album_name = input[1]
    album_year = int(input[2])

file_input.close()

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute(("insert into artiste(nom, est_solo, nombre_individus) "
                            "values(%s, %d, %d)") %(artist_name, 1, 1))

cursor.execute("select last_insert_rowid()")
lastId = cursor.fetchone()[0]
connection.commit()

cursor.execute(("insert into album(titre, annee, artist_id, maison_disque_id) "
                            "values(%s, %d, %d, %d, %d)") %(album_name, album_year, lastId, 0))
connection.commit()

cursor.execute("select titre form album")

for row in cursor:
    titre = row
    print("%s" %titre)

connection.close() #toujours fermer la connection