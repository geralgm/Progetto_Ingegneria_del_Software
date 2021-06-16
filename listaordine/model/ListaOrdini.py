import json
import os
import pickle

from ordine.model.Ordine import Ordine


class ListaOrdini():

    def __init__(self):
        super(ListaOrdini, self ).__init__()
        self.lista_ordini = []
        if os.path.isfile('listaordine/data/DatabaseOrdini.pickle'):
            with open('listaordine/data/DatabaseOrdini.pickle', 'rb') as f:

                try:
                   self.lista_ordini = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaordine/data/DatabaseOrdini.json') as f:
                lista_ordine_json = json.load(f)
                for ordine_da_caricare in lista_ordine_json:
                    self.lista_ordini.append(Ordine(ordine_da_caricare['cod_fattura'],
                                                    ordine_da_caricare['cod_fornitore'], ordine_da_caricare['data_ordine'],
                                                    ordine_da_caricare['stato'], ordine_da_caricare['importo_totale'],
                                                      ordine_da_caricare["quantita_totale"], ordine_da_caricare['data_arrivo']))

    def aggiungi_ordine(self, ordine=None):
        self.lista_ordini.append(ordine)

    def get_lista_ordini(self):
        return self.lista_ordini

    def get_ordine_by_index(self, index):
        return self.lista_ordini[index]

    def filtra_ordine(self, cod_fattura):
        return self.lista_ordini[cod_fattura]


    def save_data(self):
        with open('listaordine/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

