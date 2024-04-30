import mysql.connector

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui,_ = loadUiType('pharmacie.ui')

class Accueil(QMainWindow, ui):
    def __init__(self):
        super().__init__()

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.changement_UI()
        self.gestion_boutton()

    def changement_UI(self):
        self.tabWidget.tabBar().setVisible(False)

    def gestion_boutton(self):
        self.accueil_boutton.clicked.connect(self.ouvrir_accueil_tab)
        self.medicament_boutton.clicked.connect(self.ouvrir_medicament_tab)
        self.client_boutton.clicked.connect(self.ouvrir_client_tab)
        self.medecin_boutton.clicked.connect(self.ouvrir_medecin_tab)
        self.vente_boutton.clicked.connect(self.ouvrir_vente_tab)
        self.commande_boutton.clicked.connect(self.ouvrir_commande_tab)
        self.parametre_boutton.clicked.connect(self.ouvrir_parametre_tab)

        self.pushButton_2.clicked.connect(self.ajouter_client)

##########################################################
#"""
    """"""

    def ouvrir_accueil_tab(self):
        self.tabWidget.setCurrentIndex(0)
    def ouvrir_medicament_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def ouvrir_client_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def ouvrir_medecin_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def ouvrir_vente_tab(self):
        self.tabWidget.setCurrentIndex(4)

    def ouvrir_commande_tab(self):
        self.tabWidget.setCurrentIndex(5)

    def ouvrir_parametre_tab(self):
        self.tabWidget.setCurrentIndex(6)

    #############################################
    def accueil(self):
        app = QApplication(sys.argv)
        window = Accueil()
        window.show()
        app.exec_()

    if __name__ == '__main__':
        accueil()



    def ajouter_client(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1308",
            database="testdb"
        )
        mycursor = mydb.cursor()

        nom = self.lineEdit_2.text()
        prenom= self.lineEdit_3.text()
        no_secu= self.lineEdit_4.text()
        no_mutuel= self.lineEdit_5.text()
        no_tel=self.lineEdit_12.text()
        try:
            mycursor.execute(
                """INSERT INTO client (nom, prenom, noSecu, noMutuel, noTel) VALUES (%s, %s, %s, %s, %s)""",
                (nom, prenom, no_secu, no_mutuel, no_tel))
            mydb.commit()  # N'oubliez pas de valider les changements
            print("Client ajouté avec succès!")
        except mysql.connector.Error as err:
            print("Erreur lors de l'ajout du client:", err)
"""
####################################
#les fonctions suivantes sont reliés aux requếtes SQL


    def Afficher_medicament(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='1308', db='medicament')
        self.curseur = self.db.cursor()

        self.curseur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.curseur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()

    
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1308",
                database="testdb"
            )
            mycursor = mydb.cursor()

            # Exécute la requête pour vérifier les informations d'identification
            mycursor.execute("SELECT * FROM utilisateurs WHERE nom_utilisateur = %s AND mot_de_passe = %s", (nom_utilisateur, hashed_password))
            utilisateur = mycursor.fetchone()
            
                        mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM CLIENT,")
                clients = mycursor.fetchone()"""
