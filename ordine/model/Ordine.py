

class Ordine:
    def __init__(self, cod_fornitore, cod_fattura, data_arrivo, data_ordine, stato, importo_totale, quantita_totale):
        super(Ordine, self).__init__()
        self.cod_fornitore = cod_fornitore
        self.cod_fattura = cod_fattura
        self.data_ordine = data_ordine
        self.stato = stato
        self.importo_totale = importo_totale
        self.data_arrivo = data_arrivo
        self.quantita_totale = quantita_totale


def view():
    return None