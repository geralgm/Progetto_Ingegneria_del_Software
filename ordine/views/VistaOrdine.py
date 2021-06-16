import time

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.model import Ordine


class VistaOrdine(QWidget):
    def __init__(self, cod_fattura, elimina_ordine, modifica_ordine, upda_ui, parent=None):
        super(self, VistaOrdine).__init__(parent)
        self.ordine = self.controller.get_ordine(cod_fattura)
        self.controller = ControllerOrdine(cod_fattura)
        self.elimina_ordine = elimina_ordine
        self.modifiva_ordine = modifica_ordine
        self.updata_ui = upda_ui

        v_layout = QVBoxLayout()

        label_nome = QLabel(str(self.controller.get_cod_fattura()) + " " + str(self.controller.get_data_ordine()))
        font_nome = label_nome.font()
        font_nome.setPointSize(10)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice fattura: {}".format(self.controller.get_cod_fattura())))
        v_layout.addWidget(self.get_info("Codice fornitore: {}".format(self.controller.get_cod_fornitore())))
        v_layout.addWidget(self.get_info("Data ordine: {}".format(self.controller.get_data_ordine())))
        v_layout.addWidget(self.get_info("Importo totale : {}".format(self.controller.get_importo_totale())))
        v_layout.addWidget(self.get_info("Stato: {}".format(self.controller.get_stato())))
        v_layout.addWidget(self.get_info("Data_arrivio: {}".format(self.controller.get_stato())))
        v_layout.addWidget(self.get_info("Quantita_totale: {}".format(self.controller.get_stato())))

        v_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_ordine_click)
        v_layout.addWidget(btn_elimina)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_prodotto_click)
        v_layout.addWidget(btn_modifica)

        btn_back = QPushButton("Indietro")
        btn_back.clicked.connect(self.show_back_click)
        v_layout.addWidget(btn_back)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_cod_fornitore())

    def elimina_ordine_click(self):
        self.elimina_ordine_by_codice(self.controller.get_cod_fattura())
        self.update_ui()
        self.close()

    def modifica_ordine_click(self):
        self.showMaximized(Ordine.view.VistaModificaOrdine.VistaModificaOrdine(self.controller.get_cod_fattura()))
        self.update_ui()
        self.close()

    def show_back_click(self, listaOrdine=None):
        self.vista_back = listaOrdine.view.VistaListaOrdine.VistaListaOrdini()
        self.vista_back.showMaximized()
        time.sleep(0.3)
        self.close()

