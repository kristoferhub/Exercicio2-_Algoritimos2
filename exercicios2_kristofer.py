"""
- Nome: Kristofer R.K
Trabalho 2:
- Herança
"""
# Classe Aluno:
class Aluno:
    
    def __init__(self, cod, nome, matricula):
        self.cod = cod
        self.nome = nome
        self.matricula = matricula

    def imprime(self):
        print(f'Código: {self.cod}')
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')


# Classe AlunoEnsinoMedio:
class AlunoEnsinoMedio(Aluno):

    def __init__(self, cod, nome, matricula, ano):
        Aluno.__init__(self, cod, nome, matricula)
        self.ano = ano

    def imprime(self):
        Aluno.imprime(self)
        print(f'Ano: {self.ano}')


# Classe AlunoGraduacao
class AlunoGraduacao(Aluno):

    def __init__(self, cod, nome, matricula, semestre):
        Aluno.__init__(self, cod, nome, matricula)
        self.semestre = semestre

    def imprime(self):
        Aluno.imprime(self)
        print(f'Semestre: {self.semestre}')




print('Aluno Ensino Médio')
em = AlunoEnsinoMedio(1, "Kristofer", 48687, "6º Semestre")
em.imprime()

print('')

print('Aluno Graduação')
gd = AlunoGraduacao(2, "Fulano", 4859, "2º Semestre")
gd.imprime()
