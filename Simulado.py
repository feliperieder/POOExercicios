           
class Bioma:
    def __init__(self, nome):
        self.__nome = nome 
        self.__fauna = []
        self.__flora = []

    def getNome(self):
        return self.__nome

    def adicionarAnimal(self, Animal):
        self.__fauna.append(Animal)

    def adicionarVegetal(self, Vegetal):
        self.__flora.append(Vegetal)

    def exibirFauna(self):
        for animal in self.__fauna:
                print(animal.getNome())

    def exibirFlora(self):
        for vegetal in self.__flora:
            print(vegetal.getNome())

class Animal: 
    def __init__(self, nome, nomeCientifico = None, filo = None, classe = None, familia = None, genero = None, especie = None, estadoConservacao = None):
        self.__nome = nome
        self.__nomeCientifico = nomeCientifico
        self.__filo = filo
        self.__classe = classe
        self.__familia = familia
        self.__genero = genero
        self.__especie = especie
        self.__estadoConservacao = estadoConservacao

    def getNome(self):
        return self.__nome

class Vegetal:
    def __init__(self, nome, nomeCientifico = None, filo = None, classe = None, familia = None, genero = None, especie = None, estadoConservacao = None):
        self.__nome = nome
        self.__nomeCientifico = nomeCientifico
        self.__filo = filo
        self.__classe = classe
        self.__familia = familia
        self.__genero = genero
        self.__especie = especie
        self.__estadoConservacao = estadoConservacao

    def getNome(self):
        return self.__nome


def main():
    biomas = []
    biomas.append(Bioma("Amazônia"))
    biomas.append(Bioma("Mata Atlântica"))
    biomas.append(Bioma("Cerrado"))
    biomas.append(Bioma("Caatinga"))
    biomas.append(Bioma("Pampa"))
    biomas.append(Bioma("Pantanal"))


    faunaBR = [
        # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
        ['Capivara',	True,	True,	True,	True,	True,	True],
        ['Gralha azul',	False,	True,	False,	False,	True,	False],
        ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],
        ['Onça pintada',	True,	True,	False,	True,	False,	True],
        ['Tatu-bola',	False,	False,	False,	True,	False,	False]
    ]

    floraBR = [
        # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
        ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
        ['Araucária',	False,	True,	False,	False,	True,	False],
        ['Mandacaru',	False,	False,	True,	True,	False,	False],
        ['Vitória-régia',	True,	False,	False,	False,	False,	True],
        ['Jatobá',	True,	True,	True,	False,	False,	True]

    ]

    #Percorrendo a tabela de animais
    for i in range(len(faunaBR)):
        animal = Animal(faunaBR[i][0])
        for j in range(1, len(faunaBR[i])):
            if faunaBR[i][j]:
                biomas[j-1].adicionarAnimal(animal)

    #percorrendo tabela de vegetais
    for i in range(len(floraBR)):
        vegetal = Vegetal(floraBR[i][0])
        for j in range(1, len(floraBR[i])):
            if floraBR[i][j]:
                biomas[j-1].adicionarVegetal(vegetal)
    



    for bioma in biomas:
        print("Bioma:", bioma.getNome())
        print("Fauna:")
        print(bioma.exibirFauna())
        print('\nFlora:')
        print(bioma.exibirFlora())
        print('-----------------------------------------------------')

if __name__ == "__main__":
    main()