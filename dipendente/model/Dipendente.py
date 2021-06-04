class Dipendente():
    def __init__(self, id, nome, cognome, cf,datanascita, email, telefono, residenza, cap, professione):
        super(Dipendente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.datanascita = datanascita
        self.email = email
        self.telefono = telefono
        self.residenza = residenza
        self.cap = cap
        self.professione = professione