class Venda:
    def __init__(self, cliente, funcionario, produtos):
        self.cliente = cliente
        self.funcionario = funcionario
        self.produtos = produtos

    def setCliente(self, cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
    def setFuncionario(self, funcionario):
        self.funcionario = funcionario
    
    def getFuncionario(self):
        return self.funcionario
    
    def setProdutos(self, produtos):
        self.produtos = produtos
    
    def getProdutos(self):
        return self.produtos