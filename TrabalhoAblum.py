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
    def __init__(self, nomeDeUsuario, senha) -> None:
        self.__nomeDeUsuario = nomeDeUsuario
        self.__senha = senha
        self.album = Album()
        self.colecao = [0,0,0,0,0,0,0,0,0,0]


    def getNomeDeUsuario(self):
        return self.__nomeDeUsuario

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
            return True
        else:
            return False

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


usuarios = []

def menuAlbum(conta):
    menu = ''    
    while menu != '4':
        menu = input('O que você deseja fazer?\n1 - Colar Figurinha\n2 - Disponibilizar para a troca\n3 - Propor Troca de Figurinhas\n4 - Revisar solicitações de troca\n5 - Voltar ao Menu anterior')

        if menu == '1':
            pass

        elif menu == '2':
            pass

        elif menu == '3':
            pass

        elif menu == '4':
            pass

        elif menu == '5':
            print('Voltando para o menu anterior.')
            print('Voltando para o menu anterior..')
            print('Voltando para o menu anterior...')

        else:
            print('Opção inválida, tente novamente')

    
menu = ''    
while menu != '3':
    menu = input('O que você deseja fazer?\n1 - Criar novo álbum\n2 - Acessar algum álbum\n3 - Sair do aplicativo\n')

    if menu == '1':
        nome = input('Defina o nome do Usuário: ')
        senha = input('Defina a senha: ')
        usuarios.append(Usuario(nome, senha))

    elif menu == '2':
        nome = input('Informe o nome do Usuário: ')
        senha = input('Informe a senha: ')
        existe = False
        for i in range(len(usuarios)):
            if usuarios[i].verificarLogin(nome, senha):
                existe = True
                conta = usuarios[i]
        
        if existe:
            menuAlbum(conta)

        else:
            print('Nome de usuário e/ou senha incorretos')
            

    elif menu == '3':
        print('Encerrando atividades no aplicativo')

    else:
        print('Opção inválida, tente novamente')