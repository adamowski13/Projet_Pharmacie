import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="mysql-pharmacieapi.alwaysdata.net",
    user="358438_admin",
    password="Bartra-23!",
    database="pharmacieapi_data"
)
mycursor = mydb.cursor()

# Désactiver temporairement la vérification des clés étrangères
mycursor.execute("SET FOREIGN_KEY_CHECKS=0")

# Lecture du fichier texte et extraction des données
with open("../api/generiques.txt", "r", encoding="ISO-8859-1") as file:
    lines = file.readlines()

donnees = [line.strip().split("\t") for line in lines]

# Requête SQL pour l'insertion des données
sql = "INSERT INTO Groupes_generiques (Identifiant_groupe_generique, Libelle_groupe_generique, Code_CIS, Type_generique, Numero_tri) VALUES (%s, %s, %s, %s, %s)"

# Liste pour stocker les indices des lignes avec des erreurs
indices_erreurs = []

# Exécution de la requête pour chaque ligne de données
for index, row in enumerate(donnees, 1):
    try:
        mycursor.execute(sql, row)
    except mysql.connector.Error as err:
        indices_erreurs.append(index)

# Supprimer les lignes avec des erreurs de la liste des données
donnees_sans_erreurs = [donnees[i - 1] for i in range(1, len(donnees) + 1) if i not in indices_erreurs]

# Validation de la transaction
mydb.commit()

# Réactiver la vérification des clés étrangères
mycursor.execute("SET FOREIGN_KEY_CHECKS=1")

# Fermeture de la connexion à la base de données
mydb.close()
