class Funcionario:
    def __init__(self, nome, siape):
        self.nome = nome
        self.siape = siape

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSiape(self, siape):
        self.siape = siape

    def getSiape(self):
        return self.siape