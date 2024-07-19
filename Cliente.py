class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf