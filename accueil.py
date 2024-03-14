from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class Accueil(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise l'interface utilisateur pour la nouvelle fenêtre
        self.init_ui()

    def init_ui(self):
        # fenetre d'accueil
        self.setWindowTitle('Écran d\'Accueil')
        self.setGeometry(400, 400, 400, 300)

        label_accueil = QLabel("Bienvenue dans la Fenêtre d'Accueil")

        # Configure the window layout with a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(label_accueil)

        self.setLayout(layout)
