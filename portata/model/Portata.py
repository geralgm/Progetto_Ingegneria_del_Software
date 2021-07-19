class Portata:
    def __init__(self, cod_portata, nome, prezzo, stato, tempo_preparazione, porzioni):
        super(Portata, self).__init__()

        self.cod_portata= cod_portata
        self.nome= nome
        self.prezzo= prezzo # in euro €

        # A: antipasto
        # P: primo piatto
        # S: secondo piatto
        # D: dolce
        self.stato= stato
        self.tempo_preparazione= tempo_preparazione # in minuti
        self.porzioni= porzioni