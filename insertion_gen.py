import re
import mysql.connector

# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1308",
    database="testdb"
)
mycursor = mydb.cursor()

# Création de la table
mycursor.execute('''CREATE TABLE IF NOT EXISTS Groupes_generiques (
             Identifiant_groupe_generique INT,
             Libelle_groupe_generique VARCHAR(255),
             Code_CIS INT,
             Type_generique INT,
             Numero_tri INT,
             FOREIGN KEY (Code_CIS) REFERENCES Specialites (Code_CIS)
             )''')

# Lecture du fichier et insertion des données dans la table
with open('../api/generiques.txt', 'r', encoding='latin1') as file:
    for line in file:
        # Split des données en utilisant l'espace comme séparateur
        data = re.split(r'\s{2,}', line.strip())

        # Vérifier si la liste data contient suffisamment d'éléments
        if len(data) < 3:
            print("La ligne est mal formatée et sera ignorée:", line.strip())
            continue

        # Assurer que le Code_CIS est un entier
        try:
            code_cis = int(data[2])
        except ValueError:
            print("Le Code_CIS n'est pas un entier et la ligne sera ignorée:", line.strip())
            continue

        # Vérification si le Code_CIS existe dans la table Specialites
        mycursor.execute("SELECT COUNT(*) FROM Specialites WHERE Code_CIS = %s", (code_cis,))
        result = mycursor.fetchone()[0]  # Récupère le nombre de lignes correspondantes

        # Si le Code_CIS n'existe pas dans Specialites, ignorer la ligne
        if result == 0:
            print(f"Ignorer la ligne avec le Code_CIS {code_cis} car il n'existe pas dans la table Specialites")
            continue

        # Insertion des données dans la table
        mycursor.execute('INSERT INTO Groupes_generiques VALUES (%s,%s,%s,%s,%s)', data)

# Commit et fermeture de la connexion
mydb.commit()
mydb.close()
