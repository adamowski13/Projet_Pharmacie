import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import mysql.connector
from accueil import *

class Connexion(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise l'interface utilisateur
        self.init_ui()

    def init_ui(self):
        # Configure les propriétés de la fenêtre principale
        self.setWindowTitle('Écran de Connexion')
        self.setGeometry(300, 300, 500, 500)  # Augmenter la taille de la fenêtre
        #self.setGeometry(0, 0, 1920, 1080) a ajouter apres les tests

        # Crée des widgets pour la saisie utilisateur et le bouton de connexion
        self.label_utilisateur = QLabel("Nom d'utilisateur")
        self.label_mdp = QLabel("Mot de passe:")
        self.entrée_utilisateur = QLineEdit()
        self.entrée_mdp = QLineEdit()

        # Préremplit les champs de saisie avec les valuers de test
        self.entrée_utilisateur.setText('root')
        self.entrée_mdp.setText('1308')

        self.entrée_mdp.setEchoMode(QLineEdit.Password)
        self.bouton_connexion = QPushButton('Se Connecter')

        # Configure la mise en page de la fenêtre avec un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_utilisateur, alignment=Qt.AlignLeft)  # Centrer le label
        layout.addWidget(self.entrée_utilisateur)
        layout.addWidget(self.label_mdp, alignment=Qt.AlignLeft)  # Centrer le label
        layout.addWidget(self.entrée_mdp)
        layout.addWidget(self.bouton_connexion, alignment=Qt.AlignLeft)  # Centrer le bouton

        self.setLayout(layout)

        # Connecte le clic sur le bouton à la fonction de connexion
        self.bouton_connexion.clicked.connect(self.login)

        # Affiche la fenêtre
        self.show()

        # Ajouter un espace pour agrandir les widgets


    def connexion(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="1308", database="testdb" ) # se connecter la bonne bdd)  # Connexion à la BDD
        mycursor = mydb.cursor()

        id_connexion = self.entrée_utilisateur.text()
        mdp_connexion=self.entrée_mdp.text()

    def login(self): #en lcoal
        # Récupère les informations saisies par l'utilisateur
        nom_utilisateur = self.entrée_utilisateur.text()
        mot_de_passe = self.entrée_mdp.text()

        # Vérifie les informations de connexion
        if nom_utilisateur == 'root' and mot_de_passe == '1308':
            QMessageBox.information(self, 'Connexion Réussie', 'Bienvenue, {}'.format(nom_utilisateur))
            self.change_content()  # Appel de la fonction pour changer le contenu

        else:
            QMessageBox.warning(self, 'Connexion Échouée', 'Nom d\'utilisateur ou mot de passe incorrect')

    def change_content(self):
        self.setWindowTitle('Écran d\'Accueil')
        # Supprime tous les widgets de la fenêtre de connexion
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)

        # Importe la nouvelle classe et ajoute les nouveaux widgets
        accueil_window = Accueil()
        self.layout().addWidget(accueil_window)

if __name__ == '__main__':
    # Initialise l'application PyQt
    app = QApplication(sys.argv)

    # Crée une instance de la classe Connexion
    login_screen = Connexion()

    # Exécute l'application
    sys.exit(app.exec_())
