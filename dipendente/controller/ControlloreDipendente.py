class ControlloreDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_id_dipendente(self):
        return self.model.id

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_cf_dipendente(self):
        return self.model.cf

    def get_datanascita_dipendente(self):
        return self.model.datanascita

    def get_email_dipendente(self):
        return self.model.email

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_residenza_dipendente(self):
        return self.model.residenza


    def get_cap_dipendente(self):
        return self.model.cap

    def get_professione_dipendente(self):
        return self.model.professione