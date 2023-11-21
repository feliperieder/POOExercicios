
class Veiculo:
    def __init__(self, marca, modelo, ano) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def acelerar(self):
        print('Acelerando o veículo!')

    def frear(self):
        print('Freando o veículo!')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor) -> None:
        super().__init__(marca, modelo, ano)
        self.__cor = cor

    def ligarRadio(self):
        print('Ligando rádio do carro!')

    def abrirPorta(self):
        print('Abrindo a porta do carro!')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada) -> None:
        super().__init__(marca, modelo, ano)
        self.__cilidrada = cilindrada

    def emipinar(self):
        print('Empinando a moto!')

    def buzinar(self):
        print('Buzinando a moto!')

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima) -> None:
        super().__init__(marca, modelo, ano)
        self.__carga_maxima = carga_maxima

    def carregar(self):
        print('Carregando o caminhão!')

    def descarregar(self):
        print('Descarregando o caminhão!')


carro = Carro('Hyundai', 'HB20', 2020, 'Prata')
moto = Moto('Yamaha', 'Fluo', 2023, 125)
caminhao = Caminhao('Volvo', 'FH', 2023, 80)

carro.abrirPorta()
carro.acelerar()
carro.frear()
carro.ligarRadio()

caminhao.acelerar()
caminhao.carregar()
caminhao.descarregar()

moto.frear()
moto.buzinar()
moto.emipinar()