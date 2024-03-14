import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1308",
    database="testdb" #se connecter la bonne bdd
)  # Connexion à la BDD

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table_name;")


rows = mycursor.fetchall()

for row in rows:
    print(row)
