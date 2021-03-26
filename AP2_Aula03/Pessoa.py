class Pessoa:

    def __init__(self, codigoPessoa, nomePessoa):
        self.codigo = codigoPessoa
        self.nome = nomePessoa
        self.imprimir()
    
    def imprimir(self):
        print( "Codigo: " , self.codigo , "\nNome: " , self.nome)