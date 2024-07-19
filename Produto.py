class Produto:
    def __init__(self, nome, codigo, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
    
    def getQuantidade(self):
        return self.quantidade