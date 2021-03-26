from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, cpf):
        Pessoa.__init__(self, codigo, nome ) #invocar o metodo construtor da superclasse
        self.cpf = cpf
        print("CPF: ", self.cpf)
