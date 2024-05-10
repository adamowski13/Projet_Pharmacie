import mysql.connector
import csv

# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1308",
    database="testdb"
)
mycursor = mydb.cursor()

# Création de la table
mycursor.execute('''CREATE TABLE IF NOT EXISTS Specialites (
             code_cis INT,
             denomination VARCHAR(255),
             forme_pharmaceutique VARCHAR(255),
             voies_administration VARCHAR(255),
             statut_amm VARCHAR(255),
             type_procedure VARCHAR(255),
             etat_commercialisation VARCHAR(255),
             date_amm VARCHAR(255),
             statut_bdm VARCHAR(255),
             numero_autorisation_europeenne VARCHAR(255),
             titulaires VARCHAR(255),
             surveillance_renforcee VARCHAR(3)
             )''')

# Lecture du fichier et insertion des données dans la table
with open('../api/specialites.txt', 'r', encoding='latin1') as file:
    for line in file:
        # Split des données
        data = line.strip().split('\t')
        # Insertion des données dans la table
        mycursor.execute('INSERT INTO Specialites VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)

# Commit et fermeture de la connexion
mydb.commit()
mydb.close()
