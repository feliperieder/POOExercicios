import random

class Animal:
    def __init__(self, nomeAnimal) -> None:
        self._nomeAnimal = nomeAnimal

    def exibirDescricao(self):
        print('O nome do animal é:', self._nomeAnimal)


class Carnivoro(Animal):
    def __init__(self, nomeAnimal) -> None:
        super().__init__(nomeAnimal)

    def cacar(self):
        print(self._nomeAnimal, 'está caçando')

    def exibirDescricao(self):
        super().exibirDescricao()
        print(self._nomeAnimal, 'é um carnívoro')

class Herbivoro(Animal):
    def __init__(self, nomeAnimal) -> None:
        super().__init__(nomeAnimal)

    def pastar(self):
        print(self._nomeAnimal, 'está pastando')

    def exibirDescricao(self):
        super().exibirDescricao()
        print(self._nomeAnimal, 'é um herbívoro')

class Onivoro(Carnivoro, Herbivoro):
    def __init__(self, nomeAnimal) -> None:
        Carnivoro.__init__(self, nomeAnimal)
        Herbivoro.__init__(self, nomeAnimal)
    
    def comer(self):
        sorteio = random.randint(0, 1)
        if sorteio == 0 :
            Carnivoro.cacar(self)

        elif sorteio == 1:
            Herbivoro.pastar(self)

    def exibirDescricao(self):
        Animal.exibirDescricao(self)
        print(self._nomeAnimal, 'é um onívoro')



leao = Carnivoro('Leão')
leao.cacar()
leao.exibirDescricao()

vaca = Herbivoro('Vaca')
vaca.pastar()
vaca.exibirDescricao()

macaco = Onivoro('Macaco')
macaco.exibirDescricao()
x=0
while x <= 5:
    macaco.comer()
    x +=1