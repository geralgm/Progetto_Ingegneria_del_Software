from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaprenotazioni.controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni
from listaprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioni(QWidget):
    def __init__(self, parent = None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.controller = ControllerListaPrenotazioni()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
       # h_layout.addLayout(self.list_view)


        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Open')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton('New')
        new_button.clicked.connect(self.show_new_prenotazione)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        home_button = QPushButton("Home")
        home_button.clicked.connect(self.close)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)



        self.setLayout(h_layout)
        self.resize(500, 400)
        self.setWindowTitle('Lista Prenotazioni')


    def update_ui(self):
        self.list_view_model = QStandardItemModel(self.list_view)
        for prenotazione in self.controller.get_lista_prenotazioni():
            item = QStandardItem()
            item.setText(prenotazione.cliente.cognome + ' ' + prenotazione.cliente.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(20)
            item.setFont(font)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def show_selected_info(self):
        if(len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            prenotazione_selezionata = self.controller.get_prenotazione_by_index(selected)
            self.vista_prenotazione = VistaPrenotazione(prenotazione_selezionata, self.controller.elimina_prenotazione_by_tipo, self.update_ui)
            self.vista_prenotazione.show()

    def show_new_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui )
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()
        self.vista_inserisci_prenotazione.show()


    def closeEvent(self, Event):
        self.controller.save_data()