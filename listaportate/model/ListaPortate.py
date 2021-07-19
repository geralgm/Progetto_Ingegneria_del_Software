import json
import os
import pickle

from portata.model.Portata import Portata


class ListaPortate:

    def __init__(self):
        super(ListaPortate, self).__init__()
        self.lista_portate = []
        self.lista_antipasti= []
        self.lista_primi= []
        self.lista_secondi= []
        self.lista_dolci= []
        self.refresh_data()

    def refresh_data(self):
        if os.path.isfile('listaportate/data/DatabasePortate.pickle') and os.stat('listaportate/data/DatabasePortate.pickle').st_size!=0:
            with open('listaportate/data/DatabasePortate.pickle', 'rb') as f:
                try:
                    self.lista_portate = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaportate/data/DatabasePortate.json') as f:
                lista_portate_json = json.load(f)
                for portata in lista_portate_json:
                    self.lista_portate.append(
                        Portata(portata["codice_portata"], portata["nome"], portata["prezzo"], portata["stato"],
                                portata["tempo_preparazione"], portata["porzioni"]))

        self.divider()

    def divider(self):
        for portata in self.lista_portate:
            if portata.stato == "A":
                self.lista_antipasti.append(portata)
            elif portata.stato == "P":
                self.lista_primi.append(portata)
            elif portata.stato == "S":
                self.lista_secondi.append(portata)
            elif portata.stato == "D":
                self.lista_dolci.append(portata)
            else:
                raise EOFError