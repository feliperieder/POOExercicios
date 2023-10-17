class Album: 
    def __init__(self) -> None:
        self.paginas = []
        self.figurinhas = [False,False,False,False,False,False,False,False,False,False]
        self.requisicoesTroca = []

    def colarFigurinha(self, nro):
        self.figurinhas[nro] = True

    def possuiFigurinha(self,nro):
        if self.figurinhas[nro] == True:
            return True
        else:
            return False

class Pagina:
    def __init__(self, titulo, minNro, maxNro) -> None:
        self.figurinha = []
        self.__titulo = titulo
        self.__minNro = minNro
        self.__maxNro = maxNro

    def method(self, type):
        pass


class Usuario:
    def __init__(self, nomeDeUsuario) -> None:
        self.__nomeDeUsuario = nomeDeUsuario
        self.__senha = None
        self.album = Album()
        self.colecao = [0,0,0,0,0,0,0,0,0,0]


    def getNomeDeUsuario(self):
        return self.__nomeDeUsuario

    def cadastrar(self, nomeDeUruario, senha):
        self.__nomeDeUsuario = nomeDeUruario
        self.__senha = senha

    def verificarLogin(self, nomeDeUsuario, senha):
        if nomeDeUsuario == self.__nomeDeUsuario:
            nome = True
        else:
            nome = False

        if senha == self.__senha:
            senha = True
        else:
            senha = False 
        
        if nome and senha:
            print('Nome e senha corretos')
        elif nome and not senha:
            print('Senha incorreta')
        else:
            print('Nome de Usuário e/ou senha inorretos')

    def getAlbum(self):
        return self.album
    
    def adicionarFigurinhaColecao(self, nro):
        self.colecao[nro] = self.colecao[nro] +1
    
    def colarFigurinhaAlbum(self, nro):
        self.album.colarFigurinha(nro)

    def possuiFigurinhaNoAlbum(self, nro):
        return self.album.possuiFigurinha(nro)
    
    def possuiFigurinhaNaColecao(self, nro):
        if self.colecao[nro] > 0:
            return True
        else:
            return False



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
        pass

    elif menu == '2':
        pass

    elif menu == '3':
        pass

    else:
        print('Opção inválida, tente novamente')