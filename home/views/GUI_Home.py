# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from listadipendenti.views.GUI_ListaDipendenti import ListaDipendenti
from PyQt5.QtWidgets import QWidget
import images
from listaportate.view.GUI_ListaPortate import GUI_ListaPortate


class Home(QWidget):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setObjectName("Home")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)

        self.resize(730, 584)
        self.setMinimumSize(QtCore.QSize(730, 584))
        self.setMaximumSize(QtCore.QSize(730, 584))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.setStyleSheet("")

        self.sfondo = QtWidgets.QLabel(self)
        self.sfondo.setGeometry(QtCore.QRect(0, 0, 730, 584))
        self.sfondo.setStyleSheet("")
        self.sfondo.setText("")
        self.sfondo.setPixmap(QtGui.QPixmap(":/newPrefix/texture4.jpg"))
        self.sfondo.setScaledContents(True)
        self.sfondo.setObjectName("sfondo")

        self.label_Logo = QtWidgets.QLabel(self)
        self.label_Logo.setGeometry(QtCore.QRect(240, 30, 201, 171))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap(":/newPrefix/logoRistorante.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")

        self.Button_Ordini = QtWidgets.QPushButton(self)
        self.Button_Ordini.setGeometry(QtCore.QRect(70, 240, 250, 100))
        self.Button_Ordini.setStyleSheet("QPushButton#Button_Ordini{\n"
                                            "  background-color: #663300;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Ordini:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#Button_Ordini:hover {background-color:     #1f2e2e;}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.Button_Ordini.setObjectName("Button_Ordini")

        self.Button_Clienti = QtWidgets.QPushButton(self)
        self.Button_Clienti.setGeometry(QtCore.QRect(70, 340, 250, 100))
        self.Button_Clienti.setStyleSheet("QPushButton#Button_Clienti{\n"
                                            "  background-color:#804d00;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Clienti:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "QPushButton#Button_Clienti:hover {background-color:      #ffe066;}\n"
                                            "")
        self.Button_Clienti.setObjectName("Button_Clienti")
        self.Button_Prenotazioni = QtWidgets.QPushButton(self)
        self.Button_Prenotazioni.setGeometry(QtCore.QRect(70, 440, 250, 100))
        self.Button_Prenotazioni.setStyleSheet("QPushButton#Button_Prenotazioni{\n"
                                                "  background-color: #663300;\n"
                                                "  border-radius: 45px;\n"
                                                "  color: white;\n"
                                                "  padding: 16px 32px;\n"
                                                "  text-align: center;\n"
                                                "  text-decoration: none;\n"
                                                "  display: inline-block;\n"
                                                "  font-size: 22px;\n"
                                                "  margin: 4px 2px;\n"
                                                "  transition-duration: 0.4s;\n"
                                                "  cursor: pointer;\n"
                                                "}\n"
                                                "QPushButton#Button_Prenotazioni:pressed{\n"
                                                " background-color: white; \n"
                                                "  color: black; \n"
                                                "  border: 2px solid #4CAF50;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton#Button_Prenotazioni:hover {background-color:     #1f2e2e;}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
        self.Button_Prenotazioni.setObjectName("Button_Prenotazioni")

        self.Button_Dipendenti = QtWidgets.QPushButton(self)
        self.Button_Dipendenti.setGeometry(QtCore.QRect(390, 240, 250, 100))
        self.Button_Dipendenti.setStyleSheet("QPushButton#Button_Dipendenti{\n"
                                                "  background-color:#804d00;\n"
                                                "  border-radius: 45px;\n"
                                                "  color: white;\n"
                                                "  padding: 16px 32px;\n"
                                                "  text-align: center;\n"
                                                "  text-decoration: none;\n"
                                                "  display: inline-block;\n"
                                                "  font-size: 22px;\n"
                                                "  margin: 4px 2px;\n"
                                                "  transition-duration: 0.4s;\n"
                                                "  cursor: pointer;\n"
                                                "}\n"
                                                "QPushButton#Button_Dipendenti:pressed{\n"
                                                " background-color: white; \n"
                                                "  color: black; \n"
                                                "  border: 2px solid #4CAF50;\n"
                                                "}\n"
                                                "QPushButton#Button_Dipendenti:hover {background-color:      #ffe066;}\n"
                                                "")
        self.Button_Dipendenti.setObjectName("Button_Dipendenti")
        self.Button_Menu = QtWidgets.QPushButton(self)
        self.Button_Menu.setGeometry(QtCore.QRect(390, 340, 250, 100))
        self.Button_Menu.setStyleSheet("QPushButton#Button_Magazzino{\n"
                                            "  background-color: #663300;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Magazzino:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#Button_Magazzino:hover {background-color:     #1f2e2e;}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.Button_Menu.setObjectName("Button_Magazzino")

        self.Button_Fornitori = QtWidgets.QPushButton(self)
        self.Button_Fornitori.setGeometry(QtCore.QRect(390, 440, 250, 100))
        self.Button_Fornitori.setStyleSheet("QPushButton#Button_Fornitori{\n"
                                            "  background-color:#804d00;\n"
                                            "  border-radius: 45px;\n"
                                            "  color: white;\n"
                                            "  padding: 16px 32px;\n"
                                            "  text-align: center;\n"
                                            "  text-decoration: none;\n"
                                            "  display: inline-block;\n"
                                            "  font-size: 22px;\n"
                                            "  margin: 4px 2px;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                            "QPushButton#Button_Fornitori:pressed{\n"
                                            " background-color: white; \n"
                                            "  color: black; \n"
                                            "  border: 2px solid #4CAF50;\n"
                                            "}\n"
                                            "QPushButton#Button_Fornitori:hover {background-color:      #ffe066;}\n"
                                            "")
        self.Button_Fornitori.setObjectName("Button_Fornitori")
        self.Button_Dipendenti.clicked.connect(self.go_lista_dipendenti)
        self.Button_Menu.clicked.connect(self.go_lista_portate)
        self.setWindowTitle("Home")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button_Ordini.setText(_translate("Home", "Ordini"))
        self.Button_Clienti.setText(_translate("Home", "Clienti"))
        self.Button_Prenotazioni.setText(_translate("Home", "Prenotazioni"))
        self.Button_Dipendenti.setText(_translate("Home", "Dipendenti"))
        self.Button_Menu.setText(_translate("Home", "Menù"))
        self.Button_Fornitori.setText(_translate("Home", "Fornitori"))



    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = ListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_portate(self):
        self.vista_lista_portate= GUI_ListaPortate()
        self.vista_lista_portate.showMaximized()