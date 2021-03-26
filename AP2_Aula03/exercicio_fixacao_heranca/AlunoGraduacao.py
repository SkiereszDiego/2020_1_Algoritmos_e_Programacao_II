from Aluno import Aluno

class AlunoGraduacao(Aluno):
    
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre 
        self.imprimirAlunoGraduacao()
    
    def imprimirAlunoGraduacao(self):
        print('\nAluno da Graduacao \nCodigo: {} \nAluno: {} \nMatricula: {} \nAno: {} '
        .format(self.codigo, self.nome, self.matricula, self.semestre))