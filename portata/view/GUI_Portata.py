import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox



class GUI_Portata(QWidget):
    def __init__(self, portata, parent=None):
        super(GUI_Portata, self).__init__(parent)
        self.portata= portata

        ###################################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        self.setStyleSheet("background-color: #1f2e2e;")
        # self.setStyleSheet(("QLabel {\n"
        #                                     "   background-color:#1f2e2e;\n"
        #                                     "   border-width: 2px;\n"
        #                                     "   border-radius: 10px;\n"
        #                                     "   font: bold 12px;\n"
        #                                     "   padding: 6px;\n"
        #                                     "   color: white;\n"
        #                                     "}"))
        # Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        # istanzio un vertical layout
        self.v_layout = QVBoxLayout()
        # istanzio due Label, una per il nome e una per il body (gli altri campi)
        self.label_nome = QLabel()
        self.label_nome.setStyleSheet("color: white;\n")
        self.label_cod_portata = QLabel()
        self.label_cod_portata.setStyleSheet("color: white;\n")
        self.label_prezzo= QLabel()
        self.label_prezzo.setStyleSheet("color: white;\n")
        self.label_stato= QLabel()
        self.label_stato.setStyleSheet("color: white;\n")
        self.label_tempo_preparazione= QLabel()
        self.label_tempo_preparazione.setStyleSheet("color: white;\n")
        self.label_porzioni= QLabel()
        self.label_porzioni.setStyleSheet("color: white;\n")

        # chiamo le parti dinamiche, cioè che si modificano: update_ui per aggiornare la lista fornitori e update_ui_fornitore per aggiornare i campi
        self.update_ui()
        # imposto un carattere più grande al nome
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)

        # imposto un carattere minore per il body (i campi)
        font_cod_portata = self.label_cod_portata.font()
        font_cod_portata.setPointSize(15)
        self.label_cod_portata.setFont(font_cod_portata)

        font_prezzo = self.label_prezzo.font()
        font_prezzo.setPointSize(15)
        self.label_prezzo.setFont(font_prezzo)

        font_stato = self.label_stato.font()
        font_stato.setPointSize(15)
        self.label_stato.setFont(font_stato)

        font_tempo_preparazione = self.label_tempo_preparazione.font()
        font_tempo_preparazione.setPointSize(15)
        self.label_tempo_preparazione.setFont(font_tempo_preparazione)

        font_porzioni = self.label_porzioni.font()
        font_porzioni.setPointSize(15)
        self.label_porzioni.setFont(font_porzioni)


        # aggiungo il nome al widget, cioè al mio contenitore
        self.v_layout.addWidget(self.label_nome)
        # aggiungo i campi del body al widget
        self.v_layout.addWidget(self.label_cod_portata)
        self.v_layout.addWidget(self.label_prezzo)
        self.v_layout.addWidget(self.label_stato)
        self.v_layout.addWidget(self.label_tempo_preparazione)
        self.v_layout.addWidget(self.label_porzioni)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Portata")

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def update_ui(self):
        self.label_nome.setText(self.portata.nome)
        self.label_cod_portata.setText("Codice portata: {}".format(self.portata.cod_portata))
        self.label_prezzo.setText("Prezzo: {}".format(str(self.portata.prezzo) + " €"))

        if self.portata.stato=="A":
            stato="Antipasto"
        elif self.portata.stato=="P":
            stato="Primo"
        elif self.portata.stato=="S":
            stato="Secondo"
        else:
            stato="Dolce"

        self.label_stato.setText("Piatto: {}".format(stato))
        self.label_tempo_preparazione.setText("Tempo preparazione: {}".format(str(self.portata.tempo_preparazione) + " minuti"))
        self.label_porzioni.setText("Porzioni disponibili: {}".format(self.portata.porzioni))

