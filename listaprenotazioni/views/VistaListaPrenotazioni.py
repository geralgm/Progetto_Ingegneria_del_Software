
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView

import imaginePrenotazione

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione



class VistaListaPrenotazioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.controller = ControlloreListaPrenotazioni()

        self.setObjectName("VistaListaPrenotazioni")
        self.resize(730, 600)
        self.setMinimumSize(QtCore.QSize(730, 600))
        self.setMaximumSize(QtCore.QSize(730, 600))

        self.sfondolistaprenotazione = QtWidgets.QLabel(self)
        self.sfondolistaprenotazione.setGeometry(QtCore.QRect(0, 0, 730, 600))
        self.sfondolistaprenotazione.setText("")
        self.sfondolistaprenotazione.setPixmap(QtGui.QPixmap(":/newPrefix/imagine.jpeg"))
        self.sfondolistaprenotazione.setScaledContents(True)
        self.sfondolistaprenotazione.setObjectName("sfondolistaprenotazione")

        h_layout = QHBoxLayout()
        self.list_view = QListView(self)
        self.list_view.setGeometry(QRect(20, 80, 500, 450))
        self.list_view.setObjectName("listWidget")
        self.update_ui()
        h_layout.addWidget(self.list_view)

        self.buttonApri = QtWidgets.QPushButton(self)
        self.buttonApri.setGeometry(QtCore.QRect(610, 40, 111, 70))
        self.buttonApri.setStyleSheet("QPushButton#buttonApri{\n"
                                        "  background-color:#293d3d;\n"
                                        "  border-radius: 30px;\n"
                                        "  color: white;\n"
                                        "  padding: 16px 32px;\n"
                                        "  text-align: center;\n"
                                        "  text-decoration: none;\n"
                                        "  display: inline-block;\n"
                                        "  font-size: 16px;\n"
                                        "  margin: 4px 2px;\n"
                                        "  transition-duration: 0.4s;\n"
                                        "  cursor: pointer;\n"
                                        "}\n"
                                        "QPushButton#buttonApri:pressed{\n"
                                        " background-color: white; \n"
                                        "  color: black; \n"
                                        "  border: 3px solid #4CAF50;\n"
                                        "}\n"
                                        "QPushButton#buttonApri:hover {background-color:      #d1e0e0;}")
        self.buttonApri.setObjectName("buttonApri")

        self.buttonHome = QtWidgets.QPushButton(self)
        self.buttonHome.setGeometry(QtCore.QRect(610, 180, 111, 70))
        self.buttonHome.setStyleSheet("QPushButton#buttonHome{\n"
                                        "  background-color:#293d3d;\n"
                                        "  border-radius: 30px;\n"
                                        "  color: white;\n"
                                        "  padding: 16px 32px;\n"
                                        "  text-align: center;\n"
                                        "  text-decoration: none;\n"
                                        "  display: inline-block;\n"
                                        "  font-size: 16px;\n"
                                        "  margin: 4px 2px;\n"
                                        "  transition-duration: 0.4s;\n"
                                        "  cursor: pointer;\n"
                                        "}\n"
                                        "QPushButton#buttonHome:pressed{\n"
                                        " background-color: white; \n"
                                        "  color: black; \n"
                                        "  border: 3px solid #4CAF50;\n"
                                        "}\n"
                                        "QPushButton#buttonHome:hover {background-color:      #d1e0e0;}")
        self.buttonHome.setObjectName("buttonHome")

        self.buttonNuovaprenotazione = QtWidgets.QPushButton(self)
        self.buttonNuovaprenotazione.setGeometry(QtCore.QRect(610, 110, 111, 70))
        self.buttonNuovaprenotazione.setStyleSheet("QPushButton#buttonNuovprenotazione{\n"
                                                    "  background-color:#293d3d;\n"
                                                    "  border-radius: 30px;\n"
                                                    "  color: white;\n"
                                                    "  padding: 16px 32px;\n"
                                                    "  text-align: center;\n"
                                                    "  text-decoration: none;\n"
                                                    "  display: inline-block;\n"
                                                    "  font-size: 16px;\n"
                                                    "  margin: 4px 2px;\n"
                                                    "  transition-duration: 0.4s;\n"
                                                    "  cursor: pointer;\n"
                                                    "}\n"
                                                    "QPushButton#buttonNuovprenotazione:pressed{\n"
                                                    " background-color: white; \n"
                                                    "  color: black; \n"
                                                    "  border: 3px solid #4CAF50;\n"
                                                    "}\n"
                                                    "QPushButton#buttonNuovprenotazione:hover {background-color:      #d1e0e0;}")
        self.buttonNuovaprenotazione.setObjectName("buttonNuovprenotazione")

        self.buttonNuovaprenotazione.clicked.connect(self.show_new_prenotazione)
        self.buttonHome.clicked.connect(self.close)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.controller.get_lista_delle_prenotazioni():
            from PyQt5.QtGui import QStandardItem
            item = QStandardItem()
            item.setText(prenotazione.cliente.cognome + ": " + prenotazione.prodotto.tipo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_new_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui)
        self.vista_inserisci_prenotazione.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("VistaListaPrenotazioni", "Form"))
        self.buttonApri.setText(_translate("VistaListaPrenotazioni", "Apri"))
        self.buttonNuovaprenotazione.setText(_translate("VistaListaPrenotazioni", "Nuova"))
        self.buttonHome.setText(_translate("VistaListaPrenotazioni", ""))