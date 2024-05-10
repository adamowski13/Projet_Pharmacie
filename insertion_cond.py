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
mycursor.execute('''CREATE TABLE IF NOT EXISTS Conditions_prescription_delivrance (
             code_cis INT,
             Condition_prescription_delivrance VARCHAR(255)
             )''')

# Lecture du fichier et insertion des données dans la table
with open('../api/conditions.txt', 'r', encoding='latin1') as file:
    for line in file:
        # Split des données
        data = line.strip().split('\t')
        # Insertion des données dans la table
        mycursor.execute('INSERT INTO Conditions_prescription_delivrance VALUES (%s,%s)', data)

# Commit et fermeture de la connexion
mydb.commit()
mydb.close()
