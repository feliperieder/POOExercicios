
import csv
import random


class Album: 
    def __init__(self) -> None:
        self.paginas = [Pagina(0, 0, 0), Pagina(1, 1, 5), Pagina(2, 6, 10), Pagina(3, 11, 15), Pagina(4, 16, 20)]
        self.figurinhasColecao = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.figurinhasColadas = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.requisicoesTroca = []
        self.figurinhas = []

        with open('.\Figurinhascsv.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
            leitor_csv = csv.reader(arquivo, delimiter=';')
            for linha in leitor_csv:
                self.figurinhas.append(Figurinha(linha[0], linha[1], linha[2], linha[3]))

        for pagina in self.paginas:
            pagina.figurinhasPaginha(self.figurinhas)
  
    def colarFigurinha(self, nro):
        self.figurinhas[nro] = True

    def figuraNovaColecao(self, nro):
        self.figurinhasColecao[nro] = True
        for n in range(len(self.figurinhasColecao)):
            if self.figurinhasColecao[n] and self.figurinhas[n].informarStatusdaFigurinha == 0:
                self.figurinhas[n].statusdaFigurinha = 1



class Pagina:
    def __init__(self, titulo, minNro, maxNro) -> None:
        self.figurinha = []
        self.__titulo = titulo
        self.__minNro = minNro
        self.__maxNro = maxNro
        self.figurinhas = []

    def figurinhasPaginha(self, figurinhas):
        for figurinha in figurinhas:
            if int(figurinha.pagina()) == self.__titulo and int(figurinha.pagina()) <= self.__maxNro:
                self.figurinhas.append(figurinha)


    def show(self):
        print(self.__titulo)

        if self.__minNro > 0:
            contador = 0
            figura = self.__minNro
            while contador < 5:
                if int(self.figurinhas[contador].informarStatusdaFigurinha()) == 0:
                    print(figura, '- X')
                elif int(self.figurinhas[contador].informarStatusdaFigurinha()) == 1:
                    print(figura, '- COLAR')
                else:
                    nome, conteudo = self.figurinhas[contador-1].conteudo()
                    print(figura, '-', nome, '-', conteudo)
                figura += 1
                contador +=1


        else:
            print('Times do Brasileirão')

class Usuario:
    def __init__(self, nomeDeUsuario, senha) -> None:
        self.__nomeDeUsuario = nomeDeUsuario
        self.__senha = senha
        self.album = Album()
        self.colecao = [0,2,0,0,3,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0]

        self.novasFiguras()


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
        self.novasFiguras()
    
    def colarFigurinhaAlbum(self, nro):
        self.album.colarFigurinha(nro)

    def possuiFigurinhaNoAlbum(self, nro):
        return self.album.possuiFigurinha(nro)
    
    def possuiFigurinhaNaColecao(self, nro):
        if self.colecao[nro] > 0:
            return True
        else:
            return False
        
    def figurinhasNaColecao(self):
        for nro in range(len(self.colecao)):
            if self.possuiFigurinhaNaColecao(nro):
                print('Você possui', self.colecao[nro], 'figurinhas', nro+1)

    def novasFiguras(self):
        for nro in range(len(self.colecao)):
            if self.possuiFigurinhaNaColecao(nro):
                self.album.figuraNovaColecao(nro)



class Figurinha:
    def __init__(self, numero, nome, conteudo, nroPagina) -> None:
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        self.__status = 0
        self.__nroPagina = nroPagina

    def statusDaFigurinha(self,novo_status):
        self.__status = novo_status

    def informarStatusdaFigurinha(self):
        return self.__status
    
    def contudo(self):
        return self.__nome, self.__conteudo
    def pagina(self):
        return self.__nroPagina

class Troca:
    def __init__(self, nomeProponente, figurinhaRequerida, figurinhaDisponivel, status) -> None:
        self.__nomeProponente = nomeProponente
        self.__figurinhaRequerida = figurinhaRequerida
        self.__figurinhaDisponivel = figurinhaDisponivel
        self.__status = status

    def aceitar(self, aceito):
        pass

usuarios = []

def verAlbum(conta):
    pagina = 0
    conta.album.paginas[pagina].show()
    menu = ''
    while menu != '3':
        menu = input('O que você deseja fazer?\n1 - Página Anterior\n2 - Próxima Página\n3 - Fechar álbum\n')
        if menu == '2':
            if pagina < 4:
                pagina += 1
                conta.album.paginas[pagina].show()
            else:
                print("Essa é a última página do álbum, tente outra operação")
        elif menu == '1':
            if pagina > 0:
                pagina -= 1
                conta.album.paginas[pagina].show()
            else:
                print("Essa é a primeira página do álbum, tente outra operação")

def menuGerenciarColecao(conta):
    menu = ''    
    while menu != '5':
        menu = input('O que você deseja fazer?\n1 -Colar Figurinha\n2 - Disponibilizar para a troca\n3 - Propor troca de Figurinhas\n4 - Revisar solicitações de troca\n5 - Voltar ao Menu anterior\n')

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
     
def menuAlbum(conta):
    menu = ''    
    while menu != '4':
        menu = input('O que você deseja fazer?\n1 - Ver Álbum\n2 - Gerenciar a Coleção\n3 - Abrir Pacote de Figurinhas\n4 - Voltar ao Menu anterior\n')

        if menu == '1':
            verAlbum(conta)

        elif menu == '2':
            conta.figurinhasNaColecao()
            #depois
            menuGerenciarColecao(conta)


        elif menu == '3':
            print('Abrindo pacote de Figurinhas')
            novafigurinha = [random.randint(1,20),random.randint(0,19),random.randint(1,20)]
            print('Voce ganhou 3 novas figurinhas', novafigurinha[0]+1,',', novafigurinha[1]+1,'e', novafigurinha[2]+1)
            for nova in novafigurinha:
                conta.adicionarFigurinhaColecao(nova)

        elif menu == '4':
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