class Prenotazione():
    def __init__(self, id, cliente, prodotto, data):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        self.prodotto = prodotto
        self.data = data