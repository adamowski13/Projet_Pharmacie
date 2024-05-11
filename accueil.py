import hashlib

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
        self.lineEdit_7.setText(user_id)
        self.lineEdit_13.setText(user_id)
        self.lineEdit_19.setVisible(False)
        self.lineEdit_20.setVisible(False)
        self.lineEdit_21.setVisible(False)
        self.pushButton_13.setVisible(False)
        self.label_14.setVisible(False)
        self.tableWidget_commande.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # Connexion du signal textChanged à la fonction filtrer_options
        # Ouvrir automatiquement la liste déroulante
        self.comboBox.showPopup() # Sort completions case-insensitively

        """les affichages par des fonctions ici dans le code"""
        self.afficher_client()
        self.afficher_medecin()
        self.afficher_commande()
        self.afficher_client_commande()
        self.afficher_medicament_commande()
        self.afficher_medicament()
        self.afficher_parametre()

    def changement_UI(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_vente.tabBar().setVisible(False)

    def gestion_boutton(self):
        self.accueil_boutton.clicked.connect(self.ouvrir_accueil_tab)
        self.medicament_boutton.clicked.connect(self.ouvrir_medicament_tab)
        self.client_boutton.clicked.connect(self.ouvrir_client_tab)
        self.medecin_boutton.clicked.connect(self.ouvrir_medecin_tab)
        self.vente_boutton.clicked.connect(self.ouvrir_vente_tab)
        self.commande_boutton.clicked.connect(self.ouvrir_commande_tab)
        self.parametre_boutton.clicked.connect(self.ouvrir_parametre_tab)
        self.pushButton_vente.clicked.connect(self.ouvrir_nouvelle_vente)
        self.pushButton_6.clicked.connect(self.liste_des_ventes)


        self.pushButton_2.clicked.connect(self.ajouter_client)
        self.pushButton_5.clicked.connect(self.ajouter_medecin)
        self.pushButton.clicked.connect(self.rechercher_medecin_nom)
        self.pushButton_11.clicked.connect(self.rechercher_commande_nom)
        self.pushButton_8.clicked.connect(self.afficher_medecin)
        self.pushButton_9.clicked.connect(self.afficher_client)
        self.pushButton_12.clicked.connect(self.afficher_commande)
        self.pushButton_10.clicked.connect(self.creer_commande)
        self.pushButton_18.clicked.connect(self.creer_vente)
        self.pushButton_4.clicked.connect(self.rechercher_client_nom)
        self.pushButton_13.clicked.connect(self.creer_utilisateur)
        self.pushButton_20.clicked.connect(self.modifier_mdp)


        #fonctions sur l'onglet médicament
        self.pushButton_3.clicked.connect(self.rechercher_medicament_nom)
        self.pushButton_17.clicked.connect(self.rechercher_medicament_cis)
        self.pushButton_14.clicked.connect(self.afficher_medicament)








        self.pushButton_vente.clicked.connect(self.ouvrir_nouvelle_vente)



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

    def ouvrir_nouvelle_vente(self):
        self.tabWidget_vente.setCurrentIndex(1)

    def liste_des_ventes(self):
        self.tabWidget_vente.setCurrentIndex(0)

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
            host="mysql-pharmacieapi.alwaysdata.net",
            user="358438_admin",
            password="Bartra-23!",
            database="pharmacieapi_data"
        )
        return mydb.cursor(), mydb


##################################### fonction d'ajout bdd
    def ajouter_client(self):
        mycursor, mydb = self.connexion_db()

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
            QMessageBox.information(self, 'Succès', 'Client ajouté avec succès!')
            self.afficher_client()
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_12.setText('')
            if nom not in [self.comboBox_nom_vente.itemText(i) for i in
                                          range(self.comboBox_nom_vente.count())]:
                self.comboBox_nom_vente.addItem(nom)#######permet d'ajouter le nom directement a l'onglet des ventes

            if nom not in [self.comboBox.itemText(i) for i in
                                          range(self.comboBox.count())]:
                self.comboBox.addItem(nom)#######permet d'ajouter le nom directement a l'onglet des commandes
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout du client: {err}")

    def ajouter_medecin(self):
        mycursor, mydb = self.connexion_db()

        nom = self.lineEdit_8.text()
        prenom= self.lineEdit_9.text()
        spé= self.lineEdit_10.text()
        adresse= self.lineEdit_16.text()
        email=self.lineEdit_17.text()
        tel=self.lineEdit_15.text()
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

        pharmacien=self.user_id

        mycursor.execute("SELECT id FROM utilisateurs WHERE nom_utilisateur = %s", (pharmacien,))
        pharmacien_id = mycursor.fetchone()


        no_ordonnance = self.lineEdit_ordonnance.text()
        client_nom = self.comboBox.currentText()
        medicament = self.comboBox_2.currentText()
        quantite = int(self.spinBox_2.text())
        prix=0

        try:
            # Récupérer l'identifiant du client à partir de son nom
            mycursor.execute("SELECT id FROM client WHERE nom = %s", (client_nom,))
            client_id = mycursor.fetchone()
            if client_id is None:
                QMessageBox.warning(self, 'Erreur', 'Client non trouvé')
                return

            mycursor.execute("SELECT id FROM utilisateurs WHERE nom_utilisateur = %s", (pharmacien,))
            pharmacien_id = mycursor.fetchone()

            # Récupérer le code CIS du médicament à partir de son nom
            mycursor.execute("SELECT CODE_CIS FROM Specialites WHERE Denomination_medicament=%s", (medicament,))
            code_cis = mycursor.fetchone()
            if code_cis is None:
                QMessageBox.warning(self, 'Erreur', 'Médicament non trouvé')
                return

            # Insérer la commande avec l'identifiant du client et le code CIS du médicament
            mycursor.execute(
                """INSERT INTO vente (no_ordonnance, id_pharmacien, client_id,medicament_id,quantite,prix_TTC) VALUES (%s, %s, %s,%s,%s,%s)""",
                (no_ordonnance,pharmacien_id[0], client_id[0], code_cis[0], quantite, prix))
            mydb.commit()
            QMessageBox.information(self, 'Succès', 'Nouvelle vente prise en compte')
            self.afficher_commande()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout de la vente: {err}")


    def creer_commande(self):
        mycursor, mydb = self.connexion_db()

        client_nom = self.comboBox.currentText()
        medicament = self.comboBox_2.currentText()
        quantite = int(self.spinBox.text())

        try:
            # Récupérer l'identifiant du client à partir de son nom
            mycursor.execute("SELECT id FROM client WHERE nom = %s", (client_nom,))
            client_id = mycursor.fetchone()
            if client_id is None:
                QMessageBox.warning(self, 'Erreur', 'Client non trouvé')
                return

            # Récupérer le code CIS du médicament à partir de son nom
            mycursor.execute("SELECT CODE_CIS FROM Specialites WHERE Denomination_medicament=%s", (medicament,))
            code_cis = mycursor.fetchone()
            if code_cis is None:
                QMessageBox.warning(self, 'Erreur', 'Médicament non trouvé')
                return

            # Insérer la commande avec l'identifiant du client et le code CIS du médicament
            mycursor.execute(
                """INSERT INTO commande (client_id, cis_id, quantite) VALUES (%s, %s, %s)""",
                (client_id[0], code_cis[0], quantite))
            mydb.commit()
            QMessageBox.information(self, 'Succès', 'Nouvelle commande prise en compte')
            self.afficher_commande()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout de la commande: {err}")

    ######################################fct de recherche bdd

    def afficher_client(self):
        mycursor, mydb = self.connexion_db()
        mycursor = mydb.cursor()
        mycursor.execute("""SELECT * FROM client""")
        donnees = mycursor.fetchall()
        self.lineEdit_6.setText('')


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
    def afficher_medicament(self):
        mycursor, mydb = self.connexion_db()
        mycursor.execute("""SELECT S.CODE_CIS, P.CODE_CIP7, S.Denomination_medicament, P.Libelle_presentation, S.Forme_pharmaceutique, S.Titulaires, S.Surveillance_renforcee, P.Prix_euro, P.Taux_remboursement
FROM Presentations AS P
JOIN Specialites AS S ON P.CODE_CIS = S.CODE_CIS
ORDER BY RAND()
LIMIT 20;

""")
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_medicament.setRowCount(0)
            self.tableWidget_medicament.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_medicament.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_medicament.rowCount()  # enregistre le numero de ligne
                self.tableWidget_medicament.insertRow(position_ligne)

    def afficher_commande(self):
        mycursor, mydb = self.connexion_db()
        mycursor.execute("""SELECT commande.id, commande.client_id, client.nom,  Specialites.Denomination_medicament,commande.cis_id, commande.quantite
                                FROM commande
                                INNER JOIN Specialites ON commande.cis_id = Specialites.CODE_CIS
                                INNER JOIN client ON commande.client_id = client.id""")
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_commande.setRowCount(0)
            self.tableWidget_commande.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_commande.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_commande.rowCount()  # enregistre le numero de ligne
                self.tableWidget_commande.insertRow(position_ligne)

    ###########################fct de filtrage bdd
    def rechercher_client_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_6.text()
        sql = "SELECT * FROM client WHERE nom = %s"
        mycursor.execute(sql, (nom,))  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_client.setRowCount(0)
            self.tableWidget_client.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_client.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_client.rowCount()  # enregistre le numero de ligne
                self.tableWidget_client.insertRow(position_ligne)
    def rechercher_medecin_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_nomMed.text()
        sql = "SELECT * FROM medecin WHERE nom = %s"
        mycursor.execute(sql, (nom,)) #cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_medecin.setRowCount(0)
            self.tableWidget_medecin.insertRow(0)
            for ligne, tab in enumerate(donnees):#parcours les lignes
                for colonne, objet in enumerate(tab): #parcours les colonnes pour placer les données une par une
                    self.tableWidget_medecin.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne=+1
                position_ligne = self.tableWidget_medecin.rowCount()#enregistre le numero de ligne
                self.tableWidget_medecin.insertRow(position_ligne)
    def rechercher_commande_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit.text()
        sql = "SELECT commande.id, commande.client_id, client.nom,  Specialites.Denomination_medicament,commande.cis_id, commande.quantite FROM commande INNER JOIN Specialites ON commande.cis_id = Specialites.CODE_CIS INNER JOIN client ON commande.client_id = client.id WHERE client.nom =%s "

        mycursor.execute(sql, (nom,)) #cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_commande.setRowCount(0)
            self.tableWidget_commande.insertRow(0)
            for ligne, tab in enumerate(donnees):#parcours les lignes
                for colonne, objet in enumerate(tab): #parcours les colonnes pour placer les données une par une
                    self.tableWidget_commande.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne=+1
                position_ligne = self.tableWidget_commande.rowCount()#enregistre le numero de ligne
                self.tableWidget_commande.insertRow(position_ligne)
    def rechercher_vente_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_11.text()
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
    def rechercher_medicament_nom(self):
        mycursor, mydb = self.connexion_db()
        nom = self.lineEdit_18.text()
        sql = "SELECT S.CODE_CIS, P.CODE_CIP7, S.Denomination_medicament, P.Libelle_presentation, S.Forme_pharmaceutique, S.Titulaires, S.Surveillance_renforcee, P.Prix_euro, P.Taux_remboursement FROM Presentations AS P JOIN Specialites AS S ON P.CODE_CIS = S.CODE_CIS WHERE S.Denomination_medicament=%s ORDER BY RAND() LIMIT 20;"
        mycursor.execute(sql, (nom,))  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_medicament.setRowCount(0)
            self.tableWidget_medicament.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_medicament.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_medicament.rowCount()  # enregistre le numero de ligne
                self.tableWidget_medicament.insertRow(position_ligne)
    def rechercher_medicament_cis(self):#recherche par numéro de série du medoc cip
        mycursor, mydb = self.connexion_db()
        cis = self.lineEdit_14.text()
        sql = "SELECT S.CODE_CIS, P.CODE_CIP7, S.Denomination_medicament, P.Libelle_presentation, S.Forme_pharmaceutique, S.Titulaires, S.Surveillance_renforcee, P.Prix_euro, P.Taux_remboursement FROM Presentations AS P JOIN Specialites AS S ON P.CODE_CIS = S.CODE_CIS WHERE S.CODE_CIS=%s ORDER BY RAND() LIMIT 20;"
        mycursor.execute(sql, (cis,))  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        if donnees:
            self.tableWidget_medicament.setRowCount(0)
            self.tableWidget_medicament.insertRow(0)
            for ligne, tab in enumerate(donnees):  # parcours les lignes
                for colonne, objet in enumerate(tab):  # parcours les colonnes pour placer les données une par une
                    self.tableWidget_medicament.setItem(ligne, colonne, QTableWidgetItem(str(objet)))
                    colonne = +1
                position_ligne = self.tableWidget_medicament.rowCount()  # enregistre le numero de ligne
                self.tableWidget_medicament.insertRow(position_ligne)



    ######################################################
    ################## afficher_combobox_

    def afficher_client_commande(self):#permet d'afficher un combobox avec les clients potentiels pour les commandes
        mycursor, mydb = self.connexion_db()
        sql="SELECT nom FROM client ORDER BY nom ASC"
        mycursor.execute(sql)  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        for cat in donnees:
            self.comboBox.addItem(cat[0])
            self.comboBox_nom_vente.addItem(cat[0])


    def afficher_medicament_commande(self):
        mycursor, mydb = self.connexion_db()
        sql="SELECT Denomination_medicament FROM Specialites ORDER BY Denomination_medicament ASC"
        mycursor.execute(sql)  # cette méthode permet de se protéger des injections sql
        donnees = mycursor.fetchall()

        for cis in donnees:
            self.comboBox_2.addItem(cis[0])
            self.comboBox_med_vente.addItem(cis[0])

    def hash_string(self, input_string):
        # Hash la chaîne de caractères en utilisant SHA-256
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        return hashed_string

##########################################################################

    def modifier_mdp(self):
        user = self.user_id
        ancien_mdp = self.hash_string(self.lineEdit_23.text())
        mdp = self.hash_string(self.lineEdit_24.text())
        mdp_conf = self.hash_string(self.lineEdit_24.text())

        mycursor, mydb = self.connexion_db()
        sql1 = "SELECT mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s"
        mycursor.execute(sql1, (user,))
        verif = mycursor.fetchone()

        if verif is not None:  # Vérifiez si un mot de passe correspondant a été trouvé
            if ancien_mdp == verif[0]:  # Accédez au mot de passe dans le tuple retourné
                if mdp == mdp_conf:
                    try:
                        sql2 = "UPDATE utilisateurs SET mot_de_passe = %s WHERE nom_utilisateur = %s"
                        mycursor.execute(sql2, (mdp, user))
                        mydb.commit()
                        QMessageBox.information(self, 'Succès', 'Mot de passe modifié avec succès!')
                    except mysql.connector.Error as err:
                        QMessageBox.warning(self, 'Erreur', f"Erreur lors de la modification du mot de passe: {err}")
                else:
                    QMessageBox.warning(self, 'Erreur', "Les deux mots de passe ne correspondent pas")
            else:
                QMessageBox.warning(self, 'Erreur', "Ancien mot de passe incorrect")
        else:
            QMessageBox.warning(self, 'Erreur', "Utilisateur non trouvé dans la base de données")

    def afficher_parametre(self):
        if self.user_id=="root": #### a modifier par le nom de l'utilisateur principal
            self.lineEdit_19.setVisible(True)
            self.lineEdit_20.setVisible(True)
            self.lineEdit_21.setVisible(True)
            self.pushButton_13.setVisible(True)
            self.label_16.setVisible(False)
            self.label_14.setVisible(True)


    def creer_utilisateur(self):

            try:
                mycursor, mydb =self.connexion_db()
                utilisateur=self.lineEdit_19.text()
                email=self.lineEdit_20.text()
                mdp = self.hash_string(self.lineEdit_21.text())
                sql="INSERT INTO utilisateurs (nom_utilisateur, email,mot_de_passe) VALUES (%s,%s,%s)"
                mycursor.execute(sql,(utilisateur, email,mdp))
                QMessageBox.information(self, 'Succès', 'utilisateur ajouté avec succès!')
                mydb.commit()
            except mysql.connector.Error as err:
                QMessageBox.warning(self, 'Erreur', f"Erreur lors de l'ajout de l'utilisateur: {err}")












