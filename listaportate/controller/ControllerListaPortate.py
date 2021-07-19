from listaportate.model.ListaPortate import ListaPortate


class ControllerListaPortate:
    def __init__(self):
        super(ControllerListaPortate, self).__init__()
        self.model = ListaPortate()

    def get_lista_portate(self):
        return self.model.lista_portate

    def get_lista_antipasti(self):
        return self.model.lista_antipasti

    def get_lista_primi(self):
        return self.model.lista_primi

    def get_lista_secondi(self):
        return self.model.lista_secondi

    def get_lista_dolci(self):
        return self.model.lista_dolci