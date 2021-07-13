import pickle


class ControllorePrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        return self.model.id

    def get_cliente_prenotazione(self):
        return self.model.cliente

    def get_prodotto_prenotazione(self):
        return self.model.prodotto

    def get_data_prenotazione(self):
        return self.model.data