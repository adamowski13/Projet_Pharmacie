import mysql.connector

# Fonction pour vérifier si une chaîne peut être convertie en float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="mysql-pharmacieapi.alwaysdata.net",
    user="358438_admin",
    password="Bartra-23!",
    database="pharmacieapi_data"
)

# Création du curseur pour exécuter les requêtes SQL
mycursor = mydb.cursor()

# Lecture du fichier contenant les données
with open('../api/presentations.txt', 'r', encoding='latin1') as file:
    lines = file.readlines()

# Itération sur chaque ligne du fichier
for line in lines:
    # Séparation des données
    data = line.strip().split('\t')
    print(data)

    # Vérification si la ligne contient suffisamment de colonnes de données
    if len(data) >= 10:
        # Vérification si la valeur peut être convertie en float
        taux_remboursement = float(data[8].strip('%')) if is_float(data[8].strip('%')) else None
        prix_euro = float(data[9].replace(',', '.')) if is_float(data[9].replace(',', '.')) else None

        # Vérification si la valeur de Code_CIS existe dans la table Specialites
        sql_check_specialites = "SELECT Code_CIS FROM Specialites WHERE Code_CIS = %s"
        val_check_specialites = (int(data[0]),)
        mycursor.execute(sql_check_specialites, val_check_specialites)
        result = mycursor.fetchone()

        if result:
            # Insertion des données dans la table Presentations
            sql_insert_presentations = "INSERT INTO Presentations (Code_CIS, Code_CIP7, Libelle_presentation, Statut_administratif_presentation, Etat_commercialisation_presentation, Date_declaration_commercialisation, Code_CIP13, Agrement_aux_collectivites, Taux_remboursement, Prix_euro, Indications_remboursement_assurance_maladie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val_insert_presentations = (int(data[0]), data[1], data[2], data[3], data[4], data[5], data[6], data[7], taux_remboursement, prix_euro,
                   data[10] if len(data) > 10 else None)
            mycursor.execute(sql_insert_presentations, val_insert_presentations)
        else:
            print("La valeur de Code_CIS n'existe pas dans la table Specialites. Ignorer cette entrée ou ajouter la valeur à la table Specialites.")

# Commit des changements
mydb.commit()

# Affichage du nombre de lignes insérées
print(mycursor.rowcount, "ligne(s) insérée(s).")

# Fermeture de la connexion
mydb.close()
