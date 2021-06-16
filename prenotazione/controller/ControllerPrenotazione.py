


class ControllerPrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_tipo_prenotazione(self):
        print(self.model.tipo)
        return self.model.tipo

    def get_cliente_prenotazione(self):
        return self.model.dipendente

    def get_servizio_prenotazione(self):
        return self.model.prodotto

    def get_data_prenotazione(self):
        return self.model.data.prenotazione