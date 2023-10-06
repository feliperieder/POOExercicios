class Usuario:
    def __init__(self, nomeDeUsuario, senha) -> None:
        self.__nomeDeUsuario = nomeDeUsuario
        self.__senha = senha
        self.album = Album

    def Usuario(self):
        pass
    
    def getNomeDeUsuario(self):
        pass

    def cadastrar(self, nomeDeUruario, senha):
        pass

    def verificarLogin(self, nomeDeUsuario, senha):
        pass

    def getAlbum(self):
        pass


class Album: 
    def __init__(self) -> None:
        self.paginas = []
        self.figurinhas =[]
        self.requisicoesTroca = []

    def method(self, type):
        pass

class Pagina:
    def __init__(self, titulo, minNro, maxNro) -> None:
        self.figurinha = []
        self.__titulo = titulo
        self.__minNro = minNro
        self.__maxNro = maxNro

    def method(self, type):
        pass



class Figurinha:
    def __init__(self, numero, nome, conteudo, status, nroPagina) -> None:
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        self.__status = status
        self.__nroPagina = nroPagina

    def method(self, type):
        pass

class Troca:
    def __init__(self, nomeProponente, figurinhaRequerida, figurinhaDisponivel, status) -> None:
        self.__nomeProponente = nomeProponente
        self.__figurinhaRequerida = figurinhaRequerida
        self.__figurinhaDisponivel = figurinhaDisponivel
        self.__status = status

    def Troca(self, nomeProponente, digurinhaRequerida, figurinhaDisponivel):
        pass

    def aceitar(self, aceito):
        pass


    
menu = ''    
while menu != '3':
    menu = input('O que você deseja fazer?\n1 - Criar novo álbum\n2 - Acessar algum álbum\n3 - Sair do aplicativo')

    if menu == '1':
        Usuario.cadastrar

    elif menu == '2':
        pass

    elif menu == '3':
        pass

    else:
        print('Opção inválida, tente novamente')