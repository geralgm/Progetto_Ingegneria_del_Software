from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaordine.controller.ControllerListaOrdini import ControllerListaOrdini
from listaordine.views.VistaInserisciOrdine import VistaInserisciOrdine
from ordine.views.VistaOrdine import VistaOrdine


class VistaListaOrdini(QWidget):
    def __init__(self, parent= None):
        super(VistaListaOrdini, self).__init__(parent)

        self.controller = ControllerListaOrdini()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Dettegli')
        #open_button.clicked.connect(self.show_ordine)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Inserisci ordine")
        new_button.clicked.connect(self.show_inserici_ordine)
        buttons_layout.addWidget(new_button)
        home_button = QPushButton("HOME")
        home_button.clicked.connect(self.close)
        buttons_layout.addWidget(home_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(500, 200)
        self.setWindowTitle('Ordini')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for ordine in self.controller.get_lista_ordini():
            item = QStandardItem()
            print(ordine.quantita_totale)
            item.setText("Codice fattura: " + str(ordine.cod_fattura) + " Data arrivo: " + str(
                ordine.data_arrivo) + " quantita totale: " + str(ordine.quantita_totale))

            item.setEditable(False)
            font = item.font()
            font.setPointSize(25)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            ordine_selezionato = self.controller.get_ordine_by_index(selected)
            self.vista_ordine = VistaOrdine(ordine_selezionato,
                                                        self.controller.elimina_ordine_by_id,
                                                self.update_ui)
            self.vista_ordine.show()


    '''
    def show_ordine(self):
       if len(self.list_view.selectedIndexes()) > 0:
        selected = self.list_view.selectedIndexes()[0].row()
        ordine_selezionato = self.controller.get_ordini_by_index(selected()
        self.vista_ordine = VistaOrdine(ordine_selezionato, self.controller.get_lista_ordini, self.update_ui)
        self.vista_ordine.showMaximized()
        time.sleep(0.3)
        self.close()
     '''

    def show_inserici_ordine(self):
        self.vista_inserisci_ordine = VistaInserisciOrdine(self.controller, self.update_ui)
        self.vista_inserisci_ordine.show()


    def closeEvent(self, event):
        self.controller.save_data()

