import pytest
from pytestqt import qtbot


from PyQt5.QtWidgets import QApplication, QMessageBox
from accueil import Accueil


@pytest.fixture
def app():
    """Fixture pour créer une application QApplication."""
    yield QApplication([])


def test_ajouter_client_avec_informations_valides(app, qtbot):
    """Test d'ajout d'un client avec des informations valides."""
    window = Accueil()
    window.lineEdit_2.setText('Nom Test')
    window.lineEdit_3.setText('Prénom Test')
    window.lineEdit_4.setText('123456789')
    window.lineEdit_5.setText('123456')
    window.lineEdit_12.setText("23")

    qtbot.addWidget(window)
    with qtbot.waitSignal(window.afficher_client):
        window.ajouter_client()

    assert QMessageBox.information.called


def test_ajouter_client_avec_informations_invalides(app, qtbot):
    """Test d'ajout d'un client avec des informations invalides."""
    window = Accueil()
    window.lineEdit_2.setText('Nom Test')
    window.lineEdit_3.setText('Prénom Test')

    qtbot.addWidget(window)
    with qtbot.waitSignal(window.afficher_client):
        window.ajouter_client()

    assert QMessageBox.warning.called


# Ajoutez d'autres tests pour les autres fonctionnalités ici

if __name__ == "__main__":
    pytest.main()
