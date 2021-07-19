import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication

from portata.view.GUI_Portata import GUI_Portata

"""
    DISPLAY DEL SINGOLO PRODOTTO IN VistaListaProdotti
        Contiene le informazioni necessarie per costruire l'interfaccia di ogni singola tile di VistaListaProdotti
"""


class GUI_DisplayPortata(QWidget):
    def __init__(self, portata, update_ui, controller, lista_portate):
        super(GUI_DisplayPortata, self).__init__()
        self.update_ui = update_ui
        self.portata = portata
        self.controller = controller
        self.lista_portate_filtrata = lista_portate

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()
        '''
            Costruzione parte statica dell'interfaccia  
        '''
        self.setObjectName("Form")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_foto = QtWidgets.QLabel(self)
        self.label_foto.setScaledContents(False)
        self.label_foto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_foto.setObjectName("label_foto")
        if os.path.isfile('listaportate/data/images/' + str(portata.cod_portata) + '.jpg'):
            pixmap = QPixmap('listaportate/data/images/' + str(portata.cod_portata) + '.jpg')
        else:
            pixmap = QPixmap('listaportate/data/images/noimage.jpg')
        self.label_foto.setPixmap(pixmap)
        self.label_foto.setGeometry(QtCore.QRect(0, 0, self.width/4, self.height/3))
        self.gridLayout.addWidget(self.label_foto, 0, 0, 1, 2)
        self.pushButton_dettagli = QtWidgets.QPushButton(self)
        self.pushButton_dettagli.setObjectName("pushButton_dettagli")
        self.pushButton_dettagli.setStyleSheet("QPushButton {\n"
                                            "   background-color: #663300;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                           "QPushButton#pushButton_dettagli:pressed{\n"
                                           " background-color: white; \n"
                                           "  color: black; \n"
                                           "  border: 2px solid #4CAF50;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#pushButton_dettagli:hover {background-color:     #ffe066;}\n"
                                           )
        self.pushButton_dettagli.clicked.connect(self.show_portata)
        self.gridLayout.addWidget(self.pushButton_dettagli, 4, 0, 1, 2)
        self.label_nome = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy)
        self.label_nome.setMinimumSize(QtCore.QSize(410, 30))
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setFont(font)
        self.label_nome.setStyleSheet("QLabel {\n"
                                       "   background-color: #804d00;\n"
                                       "   border-width: 2px;\n"
                                       "   border-radius: 10px;\n"
                                       "   font: bold 12px;\n"
                                       "   padding: 6px;\n"
                                       "   color: white;\n"
                                       "}")

        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.label_prezzo_vendita = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prezzo_vendita.sizePolicy().hasHeightForWidth())
        self.label_prezzo_vendita.setSizePolicy(sizePolicy)
        self.label_prezzo_vendita.setMinimumSize(QtCore.QSize(0, 30))
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.label_prezzo_vendita.setFont(font)
        self.label_prezzo_vendita.setStyleSheet("QLabel {\n"
                                       "   background-color: #804d00;\n"
                                       "   border-width: 2px;\n"
                                       "   border-radius: 10px;\n"
                                       "   font: bold 12px;\n"
                                       "   padding: 6px;\n"
                                       "   color: white;\n"
                                       "}")
        self.gridLayout.addWidget(self.label_prezzo_vendita, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
       Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        #self.label_marca.setText(_translate("Form", "Marca: " + str(self.portata.marca)))
        self.pushButton_dettagli.setText(_translate("Form", "Dettagli"))
        if str(self.portata.nome) == "None":
            self.label_nome.setText(_translate("Form", "Nome: Nessuno"))
        else:
            self.label_nome.setText(_translate("Form", "Nome: " + str(self.portata.nome)))
        self.label_prezzo_vendita.setText(_translate("Form", "Prezzo: " + str(self.portata.prezzo) + " €"))
        #self.label_taglia.setText(_translate("Form", "Taglia: " + str(self.portata.taglia)))
        #self.label_quantita.setText(_translate("Form", "Quantità: " + str(self.portata.quantita)))

    def show_portata(self):
        self.vista_portata = GUI_Portata(self.portata)
        self.vista_portata.show()
