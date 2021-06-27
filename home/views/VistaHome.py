from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

#from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
#from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaordine.views.VistaListaOrdine import VistaListaOrdini
#from listamagazzino.views.VistaListaMagazzino import VistaListaMagazzino
#from listafornitori.views.VistaListaFornitori import VistaListaFornitori

class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Ordini", self.go_lista_Ordini), 0, 0)
        #grid_layout.addWidget(self.get_generic_button("Lista magazzino"), 0, 1)
        #grid_layout.addWidget(self.get_generic_button("Lista Cliente"), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 0, 1)
        #grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 0)
        #grid_layout.addWidget(self.get_generic_button("Lista fornitori"), 2, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Ristorante")

    '''
    Questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_Ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.show()

    #def go_lista_clienti(self):
      #  self.vista_lista_clienti = VistaListaClienti()
       # self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    #def go_lista_prenotazioni(self):
        #self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        #self.vista_lista_prenotazioni.show()

    #def go_lista_magazzino(self):
     #   self.vista_lista_magazzino= VistaListaMagazzino()
      #  self.vista_lista_magazzino.show()
   # def go_lista_fornitori(self):
    #    self.vista_lista_fornitori=VistaListaFornitori()
     #   self.vista_lista_fornitori.show()


     #VERSIONE QT

# from PyQt5.QtWidgets import QMainWindow
 # from PyQt5 import uic
# from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti

# from listaclienti.views.VistaListaClienti import VistaListaClienti
# from listaordini.views.VistaListaOrdini import VistaListaOrdini
# from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
# from listafornitori.views.VistaListaFornitori import VistaListaFornitori
# from listamagazzino.views.VistaListaMagazzino import VistaListaMagazzino

# class VistaHome(QMainWindow):
    # def __init__(self):
        #  super(VistaHome, self).__init__()
        #  uic.loadUi("GUI_Home.ui", self)
        # self.Button_ListaDipendenti.clicked.connect(self.go_lista_dipendenti)

    # def go_lista_dipendenti(self):
        #vista_lista_dipendenti = VistaListaDipendenti(self)
        # vista_lista_dipendenti.show()
