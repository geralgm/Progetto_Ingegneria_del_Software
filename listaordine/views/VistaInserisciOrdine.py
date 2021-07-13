from PyQt5.QtWidgets import QLineEdit, QLabel, QMessageBox, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget

from ordine.model.Ordine import Ordine


class VistaInserisciOrdine(QWidget):
    def __init__(self, controller, update_ui):
        super(VistaInserisciOrdine, self).__init__()
        self.controller = controller
        self.update_ui = update_ui
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("tipo", "Tipo")
        self.get_form_entry("cod_fattura", "Codice fattura")
        self.get_form_entry("cod_fornitore", "Codice fornitore")
        self.get_form_entry("quantita_totale", "Quantita totale")
        self.get_form_entry("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
        self.get_form_entry("data_arrivo", "Data arrivo (dd/mm/AAAA)")
        self.get_form_entry("importo_totale", "importo totale")
        self.get_form_entry("stato", "Stato")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_ordine)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("New")

    def get_form_entry(self, nome, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.info[nome] = current_text_edit
        self.v_layout.addWidget(current_text_edit)

    def inserisci_ordine(self):
        tipo = self.info["tipo"].text()
        cod_fattura = self.info["cod_fattura"].text()
        cod_fornitore = self.info["cod_fornitore"].text()
        quantita_totale = self.info["quantita_totale"].text()
        data_ordine = self.info["data_ordine"].text()
        data_arrivo = self.info["data_arrivo"].text()
        importo_totale = self.info["importo_totale"].text()
        stato = self.info["stato"].text()

        for value in self.info.values():
            if value.text() == "":
               QMessageBox.critical(self, 'Inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
               return

        self.controller.inserisci_ordine(Ordine(tipo, cod_fattura, cod_fornitore, quantita_totale
                                               , data_ordine, data_arrivo,importo_totale))


        self.update_ui()
        self.close()