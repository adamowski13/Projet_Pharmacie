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

    def accueil(self):
        app = QApplication(sys.argv)
        window = Accueil()
        window.show()
        app.exec_()

    if __name__ == '__main__':
        accueil()





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
    database="testdb" #se connecter la bonne bdd
)  # Connexion à la BDD

mycursor = mydb.cursor()"""
