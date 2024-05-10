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
mycursor.execute('''CREATE TABLE IF NOT EXISTS Presentations (
             code_cis INT,
             code_cip7 VARCHAR(10),
             libelle_presentation VARCHAR(255),
             statut_administratif_presentation VARCHAR(50),
             etat_commercialisation_presentation VARCHAR(50),
             date_declaration_commercialisation DATE,
             code_cip13 VARCHAR(13),
             agrement_aux_collectivites VARCHAR(10),
             taux_remboursement DOUBLE,
             prix_euro DECIMAL(10, 2),
             indications_remboursement_assurance_maladie TEXT
             )''')

# Lecture du fichier et insertion des données dans la table
with open('../api/presentations.txt', 'r', encoding='latin1') as file:
    for line in file:
        # Split des données
        data = line.strip().split(' ')
        # Insertion des données dans la table
        mycursor.execute('INSERT INTO Presentations VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)

# Commit et fermeture de la connexion
mydb.commit()
mydb.close()
