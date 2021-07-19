import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QComboBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)
            self.lista_clienti= [c for c in self.lista_clienti_salvata.get_lista_clienti()]
            for cliente in self.lista_clienti:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(20)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.combo_clienti.setModel(self.comboclienti_model)
        v_layout.addWidget(QLabel("Cliente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_prodotti = QComboBox()
        self.comboprodotti_model = QStandardItemModel(self.combo_prodotti)
        if os.path.isfile('listaprodotti/data/lista_prodotti_salvata.pickle'):
            with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'rb') as f:
                self.lista_prodotti_salvata = pickle.load(f)
            self.lista_prodotti_disponibili = [s for s in self.lista_prodotti_salvata.get_lista_prodotti() if s.is_disponibile()]
            for prodotto in self.lista_prodotti_disponibili:
                item = QStandardItem()
                item.setText(prodotto.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboservizi_model.appendRow(item)
            self.combo_prodotti.setModel(self.comboprodotti_model)
        v_layout.addWidget(QLabel("Prodotto"))
        v_layout.addWidget(self.combo_prodotti)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        cliente = self.lista_clienti[self.combo_clienti.currentIndex()]
        prodotto = self.lista_prodotti_disponibili[self.combo_prodotti.currentIndex()]
        if data == "" or not cliente or not prodotto:
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((cliente.cognome+prodotto.tipo).lower(), cliente, prodotto, tipo))
            prodotto.prenota()
            with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_prodotti_salvata, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
