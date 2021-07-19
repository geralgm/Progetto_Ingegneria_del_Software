from listaordine.model.ListaOrdini import ListaOrdini


class  ControllerListaOrdini():
    def __init__(self):
        super(ControllerListaOrdini, self).__init__()
        self.model = ListaOrdini()

    def aggiungi_ordine(self, ordine):
        self.model.aggiungi_ordine(ordine)

    def get_lista_ordini(self):
        return self.model.get_lista_ordini()

    def get_ordine_by_index(self, index):
        return self.model.get_ordine_by_index(index)

    def elimina_ordine_by_codice(self, id):
        self.model.elimina_ordine_by_codice(id)

    def save_data(self):
        self.model.save_data()



