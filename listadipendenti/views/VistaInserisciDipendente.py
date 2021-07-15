from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from dipendente.model.Dipendente import Dipendente
from PyQt5.QtCore import QSize, QRect
import images3

class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        self.setObjectName("VistaInserisciDipendente")
        self.resize(600, 500)
        self.setMinimumSize(QSize(600, 500))
        self.setMaximumSize(QSize(600, 500))

        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 600, 500))
        self.sfondo.setPixmap(QPixmap(u":/newPrefix/texture.jpg"))
        self.sfondo.setScaledContents(True)

        #self.LogoDipendente = QLabel(self)
        #self.LogoDipendente.setObjectName(u"LogoDipendente")
        #self.LogoDipendente.setGeometry(QRect(200, 10, 141, 131))
        #self.LogoDipendente.setPixmap(QPixmap(u":/newPrefix/logoDipendente.png"))
        #self.LogoDipendente.setScaledContents(True)

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("residenza", "Residenza")
        self.add_info_text("cap", "CAP")
        self.add_info_text("professione", "Professione")
        #self.resize(600, 500)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        #self.setWindowTitle("Nuovo Dipendente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_dipendente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_dipendente(Dipendente(
            (self.qlines["nome"].text()+self.qlines["cognome"].text()).lower(),
            self.qlines["nome"].text(),
            self.qlines["cognome"].text(),
            self.qlines["cf"].text(),
            self.qlines["data_n"].text(),
            self.qlines["email"].text(),
            self.qlines["telefono"].text(),
            self.qlines["residenza"].text(),
            self.qlines["cap"].text(),
            self.qlines["professione"].text())
        )
        self.callback()
        self.close()

