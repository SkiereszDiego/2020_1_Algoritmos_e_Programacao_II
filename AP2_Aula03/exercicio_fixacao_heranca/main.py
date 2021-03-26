from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

aluno01 = Aluno(5, "Diego", 666)
aluno02 = AlunoEnsinoMedio(5, "Diego", 666, 3)
aluno03 = AlunoGraduacao(5, "Diego", 666, 1)

aluno01.imprimir()
aluno02.imprimirAlunoEnsinoMedio()
aluno03.imprimirAlunoGraduacao()