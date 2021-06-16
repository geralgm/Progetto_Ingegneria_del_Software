from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class ControllerListaPrenotazioni():
    def __init__(self):
        self.model = ListaPrenotazioni()


    def agguingi_prenotazioni(self, prenotazione):
        self.model.agguingi_prenotazione(prenotazione)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazione()

    def get_prenotazione_by_index(self, index):
        return self.model.get_prenotazione_by_index(index)

    def elimina_prenotazione_by_tipo(self, tipo):
        self.model.rimuovi_prenotazione_by_tipo(tipo)


    def save_data(self):
        self.model.save_data()

