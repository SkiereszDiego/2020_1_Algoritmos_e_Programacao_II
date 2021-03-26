class Aluno:

    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.imprimir()
    
    def imprimir(self):
        print('\nAlunos\nCodigo: {} \nAluno: {} \nMatricula: {} '
        .format(self.codigo, self.nome, self.matricula))