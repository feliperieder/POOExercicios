# Definição da classe Mago 

class Data:
    # Método Construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimirData(self):
        print('Data: {}/{}/{}'.format(self.dia, self.mes, self.ano))

    def imprimirDataPorExtenso(self, cidade):
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        mesExtenso = meses[self.mes - 1]
        print('O dia de hoje em {} é {} de {} de {}.'.format(cidade, self.dia, mesExtenso, self.ano))


    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 

class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola, poder, foco):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        self.poder = poder
        self.foco = foco
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def counterSpell(self):
        print('Cancelou uma magia')

    def lumus(self):
        print('Local iluminado')

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
        
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts', 6, 'Varinha')
gd = Mago('Gandalf', 2000, 'Magia Cinza', 10, 'Cajado')

vd = Mago('Voldemort', 71, 'Hogwarts', 9, 'Varinha')
sm = Mago('Saruman', 2000, 'Magia Branca', 10, 'Cajado')
db = Mago('Dumbledore', 115, 'Hogwarts', 10, 'Varinha')

#Acessando atributos públicos
print(hp.nome)
print(hp.idade)
print(hp.escola)

print(gd.poder)
print(gd.foco)

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()

gd.falar()
gd.counterSpell()

hp.lumus()

vd.falar()
sm.falar()
db.falar()
vd.invocarMagia()
db.counterSpell()
sm.lumus()

del hp
del gd
del vd
del sm

data = Data(23, 8, 2023)
data.imprimirData()
data.imprimirDataPorExtenso('Porto Alegre')

del data