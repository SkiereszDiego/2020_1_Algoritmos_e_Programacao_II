from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano 
        self.imprimirAlunoEnsinoMedio()
    
    def imprimirAlunoEnsinoMedio(self):
        print('\nAluno do Ensino Medio \nCodigo: {} \nAluno: {} \nMatricula: {} \nAno: {} '
        .format(self.codigo, self.nome, self.matricula, self.ano))