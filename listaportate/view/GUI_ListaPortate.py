from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QApplication

from listaportate.controller.ControllerListaPortate import ControllerListaPortate
from listaportate.view.GUI_DisplayPortata import GUI_DisplayPortata

"""
    VISUALIZZAZIONE DELLA LISTA DEI PRODOTTI CON POSSIBILITà DI FILTRAGGIO
"""


class GUI_ListaPortate(QWidget):
    def __init__(self, parent=None):
        super(GUI_ListaPortate, self).__init__(parent)
        self.controller_lista_portate = ControllerListaPortate()
        self.lista_portate = self.controller_lista_portate.get_lista_portate()
        self.setWindowTitle("Menù")
        icon = QtGui.QIcon()

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()


        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)


        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        # ---------------topWidget------------------
        self.topWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.topWidget.setObjectName("topWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.topWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # LOGO
        self.logo = QLabel(self.topWidget)
        #pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        #self.logo.setPixmap(pixmap)
        #self.logo.resize(100, 100)
        self.gridLayout_3.addWidget(self.logo, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)

        # spacer
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 10, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 11)

        # antipasti button
        self.antipasti = QtWidgets.QPushButton(self.topWidget)
        self.antipasti.setObjectName("in_arrivo")
        self.antipasti.setStyleSheet("QPushButton {\n"
                                            "   background-color: #1f2e2e;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                           "QPushButton#antipasti:pressed{\n"
                                           " background-color: white; \n"
                                           "  color: black; \n"
                                           "  border: 2px solid #4CAF50;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#antipasti:hover {background-color:     #ffe066;}\n"
                                           )
        self.gridLayout_3.addWidget(self.antipasti, 1, 0, 1, 1)
        self.antipasti.clicked.connect(self.filter_antipasti)

        # primi button
        self.primi = QtWidgets.QPushButton(self.topWidget)
        self.primi.setObjectName("in_negozio")
        self.primi.setStyleSheet("QPushButton {\n"
                                            "   background-color:#1f2e2e;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                 "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                             "QPushButton#primi:pressed{\n"
                                             " background-color: white; \n"
                                             "  color: black; \n"
                                             "  border: 2px solid #4CAF50;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#primi:hover {background-color:     #ffe066;}\n"
                                             )
        self.gridLayout_3.addWidget(self.primi, 1, 1, 1, 1)
        self.primi.clicked.connect(self.filter_primi)

        # secondi button
        self.secondi = QtWidgets.QPushButton(self.topWidget)
        self.secondi.setObjectName("venduto")
        self.secondi.setStyleSheet("QPushButton {\n"
                                            "   background-color:#1f2e2e;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                   "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                           "QPushButton#secondi:pressed{\n"
                                           " background-color: white; \n"
                                           "  color: black; \n"
                                           "  border: 2px solid #4CAF50;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#secondi:hover {background-color:     #ffe066;}\n"
                                           )
        self.gridLayout_3.addWidget(self.secondi, 1, 2, 1, 1)
        self.secondi.clicked.connect(self.filter_secondi)

        # dolci button
        self.dolci = QtWidgets.QPushButton(self.topWidget)
        self.dolci.setObjectName("reso")
        self.dolci.setStyleSheet("QPushButton {\n"
                                            "   background-color:#1f2e2e;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                 "  transition-duration: 0.4s;\n"
                                            "  cursor: pointer;\n"
                                            "}\n"
                                 "QPushButton#dolci:pressed{\n"
                                 " background-color: white; \n"
                                 "  color: black; \n"
                                 "  border: 2px solid #4CAF50;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#dolci:hover {background-color:     #ffe066;}\n"
                                 )
        self.gridLayout_3.addWidget(self.dolci, 1, 3, 1, 1)
        self.dolci.clicked.connect(self.filter_dolci)

        # indietro
        self.indietro = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indietro.sizePolicy().hasHeightForWidth())
        self.indietro.setSizePolicy(sizePolicy)
        self.indietro.setObjectName("indietro")
        self.indietro.setStyleSheet("QPushButton {\n"
                                            "   background-color:#1f2e2e;\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.indietro, 0, 0, 1, 1)
        self.indietro.clicked.connect(self.close)

        self.verticalLayout.addWidget(self.topWidget)

        # -------------centralWidget---------------
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1172, 851))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.setStyleSheet("background-color: #804d00;")
        self.scrollArea.setStyleSheet("background-color: #1f2e2e;")


        # CREAZIONE DEI WIDGET
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)

        _translate = QtCore.QCoreApplication.translate
        self.antipasti.setText(_translate("MainWindow", "Antipasti"))
        self.indietro.setText(_translate("MainWindow", "<- Indietro"))
        self.primi.setText(_translate("MainWindow", "Primi"))
        self.secondi.setText(_translate("MainWindow", "Secondi"))
        self.dolci.setText(_translate("MainWindow", "Dolci"))

        self.display_build(self.lista_portate)

    """
         Eventi trigger click dei bottoni
    """


    def display_build(self, lista_da_caricare):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        width = self.screenRect.width()

        row = 0
        column = 0
        for portata in lista_da_caricare:
            self.widget_generico = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.displayportata1 = GUI_DisplayPortata(portata, self.retranslateUi, self.controller_lista_portate, self.lista_portate)
            self.widget_generico = self.displayportata1
            self.widget_generico.setMinimumSize(QtCore.QSize((width / 3.2), 450))

            self.gridLayout_2.addWidget(self.widget_generico, row, column, 1, 1)

            if column == 2:
                row = row + 1
                column = 0
            else:
                column = column + 1

    def filter_antipasti(self):
        self.lista_portate.clear()
        lista= self.controller_lista_portate.get_lista_antipasti()
        self.lista_portate= lista[:]
        self.retranslateUi()

    def filter_primi(self):
        self.lista_portate.clear()
        lista= self.controller_lista_portate.get_lista_primi()
        self.lista_portate= lista[:]
        self.retranslateUi()

    def filter_secondi(self):
        self.lista_portate.clear()
        lista= self.controller_lista_portate.get_lista_secondi()
        self.lista_portate= lista[:]
        self.retranslateUi()

    def filter_dolci(self):
        self.lista_portate.clear()
        lista= self.controller_lista_portate.get_lista_dolci()
        self.lista_portate= lista[:]
        self.retranslateUi()

