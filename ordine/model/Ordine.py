

class Ordine:
    def __init__(self, cod_fattura, stato, data_ordine, importo_totale, quantità_totale):
        super(Ordine, self).__init__()

        self.cod_fattura = cod_fattura
        self.stato = stato
        self.data_ordine = data_ordine
        self.importo_totale = importo_totale
        self.quantita_totale = quantità_totale
