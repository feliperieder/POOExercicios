import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0
        self.ganhou = False

    def atualizar(self):
        avanco = random.randint(1, 6)
        posAtual = self.pos + avanco
        if posAtual % 5 == 0:
            self.pos = posAtual - 1

        elif posAtual == 7 or posAtual == 17:
            self.pos = posAtual +2

        elif posAtual == 13:
            self.pos = 0

        else:
            self.pos = posAtual

        if self.pos > 20:
            self.ganhou = True

    def getPos(self):
        return self.pos
    

competidores = [Competidor("Felipe"), Competidor("Eduarda"), Competidor("Vinícius"), Competidor("Lucas"), Competidor("Luana")]

while True:
    for competidor in competidores:
        competidor.atualizar()
        venceu = competidor.ganhou
        if venceu:
            vencedor = competidor.nome
            break

        print("Competidor: {}   Posição: {}".format(competidor.nome, competidor.getPos()))

    if venceu:
        print('O(A) ganhador(a) foi ', vencedor)
        break

