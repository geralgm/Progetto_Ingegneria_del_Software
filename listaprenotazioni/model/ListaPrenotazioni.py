import os
import pickle


class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.lista_prenotazioni = []
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni = pickle.load(f)

    def agguingi_prenotazioni(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def rimuovi_prenotazione_by_tipo(self, tipo):
        for prenotazione in self.lista_prenotazioni:
            print(prenotazione.tipo)
            print(tipo)
            if prenotazione.tipo == tipo:
                prenotazione.prodotto.disponibile = True
                self.lista_prenotazioni.remove(prenotazione)

                return  True
            return False

    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def get_lista_prenotazione(self):
        return self.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

    def agguingi_prenotazione(self, prenotazione):
        pass