import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import mysql.connector
import hashlib
from accueil import *

class Connexion(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise l'interface utilisateur
        self.init_ui()


    def init_ui(self):
        # Configure les propriétés de la fenêtre principale
        self.setWindowTitle('Écran de Connexion')
        self.setGeometry(100, 100, 1000, 800)  # Augmenter la taille de la fenêtre

        # Crée des widgets pour la saisie utilisateur et le bouton de connexion
        self.label_utilisateur = QLabel("Nom d'utilisateur",)
        self.label_mdp = QLabel("Mot de passe:")
        self.entrée_utilisateur = QLineEdit()
        self.entrée_mdp = QLineEdit()

        # Préremplit les champs de saisie avec les valuers de test
        self.entrée_utilisateur.setText('root')
        self.entrée_mdp.setText('1409')

        self.entrée_mdp.setEchoMode(QLineEdit.Password)
        self.bouton_connexion = QPushButton('Se Connecter')

        # Configure la mise en page de la fenêtre avec un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_utilisateur, alignment=Qt.AlignLeft)  # Centrer le label
        layout.addWidget(self.entrée_utilisateur)
        layout.addWidget(self.label_mdp, alignment=Qt.AlignLeft)  # Centrer le label
        # Affiche la fenêtre
        layout.addWidget(self.entrée_mdp)
        layout.addWidget(self.bouton_connexion, alignment=Qt.AlignLeft)  # Centrer le bouton

        self.setLayout(layout)

        # Connecte le clic sur le bouton à la fonction de connexion
        self.bouton_connexion.clicked.connect(self.login)
        self.show()


    def login(self):

        # Récupère les informations saisies par l'utilisateur
        nom_utilisateur = self.entrée_utilisateur.text()
        mot_de_passe = hashlib.sha256(self.entrée_mdp.text().encode()).hexdigest()

        # Hash le mot de passe
        hashed_password = mot_de_passe

        # Se connecte à la base de données
        try:
            mydb = mysql.connector.connect(
                host="mysql-pharmacieapi.alwaysdata.net",
                user="358438_admin",
                password="Bartra-23!",
                database="pharmacieapi_data"
            )
            mycursor = mydb.cursor()

            # Exécute la requête pour vérifier les informations d'identification
            mycursor.execute("SELECT * FROM utilisateurs WHERE nom_utilisateur = %s AND mot_de_passe = %s", (nom_utilisateur, hashed_password))
            utilisateur = mycursor.fetchone()

            if utilisateur:
                QMessageBox.information(self, 'Connexion Réussie', 'Bienvenue, {}'.format(nom_utilisateur))
                self.change_content()  # Appel de la fonction pour changer le contenu
            else:
                QMessageBox.warning(self, 'Connexion Échouée', 'Nom d\'utilisateur ou mot de passe incorrect')

            # Ferme la connexion à la base de données
            mycursor.close()
            mydb.close()

        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données:", error)

    def change_content(self):
        self.setWindowTitle('Écran d\'Accueil')
        user_id=self.entrée_utilisateur.text()
        # Supprime tous les widgets de la fenêtre de connexion
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)

        # Importe la nouvelle classe et ajoute les nouveaux widgets
        accueil_window = Accueil(user_id)
        self.layout().addWidget(accueil_window)

if __name__ == '__main__':
    # Initialise l'application PyQt
    app = QApplication(sys.argv)

    # Crée une instance de la classe Connexion
    login_screen = Connexion()

    # Exécute l'application
    sys.exit(app.exec_())
