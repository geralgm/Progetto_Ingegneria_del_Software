from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QPushButton

from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllerPrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback



        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_servizio_prenotazione().nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding))

        label_dipendente = QLabel("Dipendente: {} {}".format(self.controller.get_dipendente_prenotazione().nome,
                                                       self.controller.get_dipendente_prenotazione().cognome))
        font_dipendente = label_dipendente.font()
        font_dipendente.setPointSize(30)
        label_dipendente.setFont(font_dipendente)
        v_layout.addWidget(label_dipendente)

        label_data = QLabel("Data: {}".format(self.controller.get_data_prenotazione()))
        font_data = label_data.font()
        font_data.setPointSize(30)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_prodotto_prenotazione().nome)

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_tipo_prenotazione())
        self.elimina_callback()
        self.close()
