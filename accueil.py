import mysql.connector

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.uic import loadUiType




ui,_ = loadUiType('pharmacie.ui')

class Accueil(QMainWindow, ui):

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.changement_UI()
        self.gestion_boutton()
        """les affichages par des fonctions ici dans le code"""
        self.afficher_client()
        self.afficher_medecin()

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
        self.pushButton_5.clicked.connect(self.ajouter_medecin)
        self.pushButton.clicked.connect(self.rechercher_medecin_nom)
        self.pushButton_8.clicked.connect(self.afficher_medecin)
        self.pushButton_4.clicked.connect(self.rechercher_client_nom)



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



    def connexion_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1308",
            database="testdb"
        )
        return mydb.cursor(), mydb


##################################### fonction d'ajout bdd
    def ajouter_client(self):
        mycursor, mydb = self.connexion_db()

        nom = self.lineEdit_2.setText('')
        prenom= self.lineEdit_3.setText('')
        no_secu= self.lineEdit_4.setText('')
        no_mutuel= self.lineEdit_5.text()
        no_tel=self.lineEdit_12.text()
        try:
            mycursor.execute(
                """INSERT INTO client (nom, prenom, noSecu, noMutuel, noTel) VALUES (%s, %s, %s, %s, %s)""",
                (nom, prenom, no_secu, no_mutuel, no_tel))
            mydb.commit()  # N'oubliez pas de valider les changements
            QMessageBox.information(self, 'Succès', 'Client ajouté avec succès!')
            self.afficher_client()
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_12.setText('')
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout du client: {err}")

    def ajouter_medecin(self):
        mycursor, mydb = self.connexion_db()

        nom = self.lineEdit_8.setText('')
        prenom= self.lineEdit_9.setText('')
        spé= self.lineEdit_10.setText('')
        adresse= self.lineEdit_16.text()
        email=self.lineEdit_17.text()
        tel=self.lineEdit_15.setText('')
        try:
            mycursor.execute(
                """INSERT INTO medecin (nom, prenom, specialite, adresse, email, noTel) VALUES (%s, %s, %s, %s, %s, %s)""",
                (nom, prenom, spé, adresse, email,tel))
            mydb.commit()  # N'oubliez pas de valider les changements
            QMessageBox.information(self, 'Succès', 'médecin ajouté avec succès!')
            self.afficher_medecin()
            self.lineEdit_8.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_10.setText('')
            self.lineEdit_16.setText('')
            self.lineEdit_17.setText('')
            self.lineEdit_15.setText('')
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout du médecin: {err}")
    def creer_vente(self):
        mycursor, mydb = self.connexion_db()




    ######################################fct de recherche bdd

    def afficher_client(self):
        mycursor, mydb = self.connexion_db()
        mycursor = mydb.cursor()
        mycursor.execute("""SELECT * FROM client""")
        donnees = mycursor.fetchall()


        if donnees:
            self.tableWidget_client.setRowCount(0)
            self.tableWidget_client.insertRow(0)
            for ligne, tab in enumerate(donnees):#parcours les lignes
                for colonne, objet in enumerate(tab): #parcours les colonnes pour placer les données une par une
                    self.tableWidget_client.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne=+1
                position_ligne = self.tableWidget_client.rowCount()#enregistre le numero de ligne
                self.tableWidget_client.insertRow(position_ligne)

    def afficher_medecin(self):
        mycursor, mydb = self.connexion_db()
        mycursor.execute("""SELECT * FROM medecin""")
        donnees = mycursor.fetchall()
        self.lineEdit_nomMed.setText('')

        if donnees:
            self.tableWidget_medecin.setRowCount(0)
            self.tableWidget_medecin.insertRow(0)
            for ligne, tab in enumerate(donnees):#parcours les lignes
                for colonne, objet in enumerate(tab): #parcours les colonnes pour placer les données une par une
                    self.tableWidget_medecin.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne=+1
                position_ligne = self.tableWidget_medecin.rowCount()#enregistre le numero de ligne
                self.tableWidget_medecin.insertRow(position_ligne)
    def afficher_medicaments(self):
        mycursor, mydb = self.connexion_db()



###########################fct de filtrage bdd
    def rechercher_client_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_nomMed.text()
        sql = "SELECT * FROM medecin WHERE nom = %s"
        mycursor.execute(sql, (nom,))  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_medecin.setRowCount(0)
            self.tableWidget_medecin.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_medecin.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_medecin.rowCount()  # enregistre le numero de ligne
                self.tableWidget_medecin.insertRow(position_ligne)
    def rechercher_medecin_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_6.text()
        sql = "SELECT * FROM client WHERE nom = %s"
        mycursor.execute(sql, (nom,)) #cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_client.setRowCount(0)
            self.tableWidget_client.insertRow(0)
            for ligne, tab in enumerate(donnees):#parcours les lignes
                for colonne, objet in enumerate(tab): #parcours les colonnes pour placer les données une par une
                    self.tableWidget_client.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne=+1
                position_ligne = self.tableWidget_client.rowCount()#enregistre le numero de ligne
                self.tableWidget_client.insertRow(position_ligne)
    def rechercher_medicament_nom(self):
        mycursor, mydb = self.connexion_db()
    def rechercher_medicament_cip(self):#recherche par numéro de série du medoc cip
        mycursor, mydb = self.connexion_db()


    def join_medoc(self):#####permettra d'afficher toutes les données des médicaments depuis les differentes tables
        mycursor, mydb = self.connexion_db()










