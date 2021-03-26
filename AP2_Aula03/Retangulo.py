class Retangulo:

    def __init__(self, altura, largura): #sao parametros do metodo construtor
        self.altura = altura # atributos
        self.largura = largura # da linha 1 a 5 e a estrutura. planta da casa
        self.imprimir()
    
    def calcularArea(self):
        return self.altura * self.largura

    def calcularPerimetro(self):
        return (self.altura * 2 ) + ( self.largura * 2)

    def imprimir(self):
        print ( "Altura: " , self.altura , "\nLargura: " , self.largura)