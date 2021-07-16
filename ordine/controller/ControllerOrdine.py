


class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    #def somma_prodotti(self): pass

    #def modifica_prodotto_by_codice(self, cod_prodotto, new_value):
       # self.model.ListaProdotti.modifica_prodotto(cod_prodotto, new_value)

   # def elimina_prodotto(self, cod_prodotto): pass

    #def get_prodotto(self, index):
       # return self.model.get_prodotto(index)



    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_stato(self):
        return self.model.stato

    def get_numero_tavola(self):
        return self.model.numero_tavola

    def get_data_ordine(self):
       return self.model.data_ordine

    def get_importo_totale(self):
         return self.model.importo_totale

    def get_quantità_totale(self):
        return self.model.quantità_totale

   # def get_ordine(self, cod_fattura):
        #pass
