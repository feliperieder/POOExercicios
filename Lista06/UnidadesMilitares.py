#classe base: Unidade Militar
class UnidadeMilitar:
    def __init__(self):
        print('Unidade militar foi criada')

    def mover(self):
        print('Unidade militar está se movendo')

    def atacar(self):
        print('Unidade militar está atacando!')
    
class Soldado (UnidadeMilitar):
    def __init__(self):
        print('Soldado foi criado')
    
    def mover(self):
        print('Soldado está marchando em terra')

    def atacar(self):
        print('Soldado está atacando')

class Arqueiro (UnidadeMilitar):
    def __init__(self):
        print('Arqueiro foi criado')
    
    def mover(self):
        print('Arqueiro está se movendo em terra')

    def atacar(self):
        print('Arqueiro está atacando a distância')

class Cavaleiro (UnidadeMilitar):
    def __init__(self):
        print('Cavaleiro foi criado')
    
    def mover(self):
        print('Cavaleiro está andando a cavalo')

    def atacar(self):
        print('Cavaleiro está atacando a cavalo')

    def descerCavalo(self):
        print('Cavaleiro desceu do cavalo')

#---------------------

soldado = Soldado()
arqueiro = Arqueiro()
cavaleiro = Cavaleiro()

unidades = []
unidades.append(soldado)
unidades.append(arqueiro)
unidades.append(cavaleiro)

for unidade in unidades:
    unidade.mover()
    unidade.atacar()

for i in range(len(unidades)):
    unidades[i].mover()
    unidades[i].atacar()