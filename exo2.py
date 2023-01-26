import sqlite3

id_artiste_input = int(input())

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute("select titre from album where artiste_id = %d" %id_artiste_input)
for row in cursor:
    titre = row
    print("%s" %titre)

connection.close() #toujours fermer la connection