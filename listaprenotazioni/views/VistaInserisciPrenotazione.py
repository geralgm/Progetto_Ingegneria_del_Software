import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciPrenotazione, self).__init__(parent)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        self.combo_dipendenti = QComboBox()
        self.combodipendenti_model = QStandardItemModel(self.combo_dipendenti)
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti_salvata = pickle.load(f)
            self.lista_dipendenti = [c for c in self.lista_dipendenti_salvata()]
            for dipendente in self.lista_dipendenti:
                item = QStandardItem()
                item.setText(dipendente.nome + " " + dipendente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.combodipendenti_model.appendRow(item)
            self.combo_dipendenti.setModel(self.combodipendenti_model)
        v_layout.addWidget(QLabel("Dipendente"))
        v_layout.addWidget(self.combo_dipendenti)

        self.combo_prodotti = QComboBox()
        self.comboprodotti_model = QStandardItemModel(self.combo_prodotti)
        if os.path.isfile('listaprodotti/data/lista_prodotto_salvata.pickle'):
            with open('listaprodotti/data/lista_prodotto_salvata.pickle', 'rb') as f:
                self.lista_prodotti_salvata = pickle.load(f)
            self.lista_prodotto_disponibili = [s for s in self.lista_prodotti_salvata if s.is_disponibile()]
            for prodotto in self.lista_prodotti_disponibili:
                item = QStandardItem()
                item.setText(prodotto.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboprodotti_model.appendRow(item)
            self.combo_prodotti.setModel(self.comboprodotti_model)
        v_layout.addWidget(QLabel("Prodotti"))
        v_layout.addWidget(self.combo_prodotti)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('New Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        dipendente = self.lista_dipendenti[self.combo_dipendenti.currentIndex()]
        prodotto = self.lista_prodotti_disponibili[self.combo_prodotti.currentIndex()]
        if data == "" or not dipendente or not prodotto:
            QMessageBox(self,'Inserisci tutte le informazioni richieste', QMessageBox.Ok,
                        QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((dipendente.cognome + dipendente.nome).lower(), dipendente, prodotto, data))
            prodotto.prenota()
            with open('listaprodotti/data/lista_prodotto_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_prodotti_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
