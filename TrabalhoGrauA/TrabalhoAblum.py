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

    def statusDasFigurinhas(self):
        status = []
        for figurinha in self.figurinhas:
            status.append(figurinha.informarStatusdaFigurinha())
        return status
  
    def colarFigurinha(self, nro):
        self.figurinhasColadas[nro] = True
        if self.figurinhasColecao[nro] and self.figurinhas[nro].informarStatusdaFigurinha() == 1:
                self.figurinhas[nro].statusDaFigurinha(2)

    def figurinhaColada(self, nro):
        return self.figurinhasColadas[nro]

    def figuraNovaColecao(self, nro):
        self.figurinhasColecao[nro] = True
        for n in range(len(self.figurinhasColecao)):
            if self.figurinhasColecao[n] and self.figurinhas[n].informarStatusdaFigurinha() == 0:
                self.figurinhas[n].statusDaFigurinha(1)

    def disponibilizarTroca(self, nro):
        if self.figurinhasColecao[nro]:
                self.figurinhas[nro].statusDaFigurinha(3)
                print(self.figurinhas[nro].informarStatusdaFigurinha())

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
                    nome, conteudo = self.figurinhas[contador].conteudo()
                    print(figura, '-', nome, '-', conteudo)
                figura += 1
                contador +=1


        else:
            print('Times do Brasileirão')

class Usuario:
    def __init__(self, nomeDeUsuario, senha,colecao = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ) -> None:
        self.__nomeDeUsuario = nomeDeUsuario
        self.__senha = senha
        self.album = Album()
        self.colecao = colecao

        self.novasFiguras()

    def statusDasFigurinhas(self):
        return self.album.statusDasFigurinhas()

    def disponibilizarFigurinhaTroca(self, nro):
        self.album.disponibilizarTroca(nro)

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
        if not self.album.figurinhaColada(nro) and self.possuiFigurinhaNaColecao(nro):
            self.album.colarFigurinha(nro)
            self.colecao[nro] -=1
        elif not self.possuiFigurinhaNaColecao(nro):
            print('Você não tem essa figurinha para colar')
        else:
            print('Essa figurinha já foi colada')

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
                
    def trocarFigurinha(self, nro):
            if self.possuiFigurinhaNaColecao(nro):
                self.colecao[nro] = self.colecao[nro] -1
                self.novasFiguras()
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
    
    def conteudo(self):
        return self.__nome, self.__conteudo
    def pagina(self):
        return self.__nroPagina

class Troca:
    def __init__(self, nomeProponente, nomeRequerido, figurinhaRequerida, figurinhaDisponivel) -> None:
        self.__nomeProponente = nomeProponente
        self.__nomeRequerio = nomeRequerido
        self.__figurinhaRequerida = int(figurinhaRequerida)
        self.__figurinhaDisponivel = int(figurinhaDisponivel)
        self.__status = False

    def aceitar(self):
        self.__status = True
        for usuario in usuarios:
            if usuario.getNomeDeUsuario() == self.__nomeProponente:
                usuario.trocarFigurinha(self.__figurinhaDisponivel)
                usuario.adicionarFigurinhaColecao(self.__figurinhaRequerida)
            if usuario.getNomeDeUsuario() == self.__nomeRequerio:
                usuario.trocarFigurinha(self.__figurinhaRequerida)
                usuario.adicionarFigurinhaColecao(self.__figurinhaDisponivel)


    def recusar(self):
        self.__status = True
    def informarNomeRequerido(self):
        return self.__nomeRequerio
    def informarNomeProponente(self):
        return self.__nomeProponente
    def figurinhaRequerida(self):
        return self.__figurinhaRequerida
    def figurinhaDisponivel(self):
        return self.__figurinhaDisponivel
    def status(self):
        return self.__status
    

usuarios = []
trocas = []
usuarios.append(Usuario('felipe','felipe',[0,2,0,2,0,0,0,2,4,0,0,0,0,0,2,0,0,1,0,0]))
usuarios.append(Usuario('raphael', 'raphael',[0,2,3,1,0,0,0,2,1,0,2,0,0,1,0,0,0,1,0,3]))
usuarios.append(Usuario('oi','oi'))
trocas.append(Troca('raphael', 'felipe', 1, 19))
#with open('.\Usuarios.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
#    leitor_csv = csv.reader(arquivo, delimiter=';')
#    for linha in leitor_csv:
#        figurinhas = []
#        for i in range(len(linha)):
#            if i < 1:
#                figurinhas.append(linha(i))


print(usuarios)
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
        menu = input('O que você deseja fazer?\n1 - Colar Figurinha\n2 - Disponibilizar para a troca\n3 - Propor troca de Figurinhas\n4 - Revisar solicitações de troca\n5 - Voltar ao Menu anterior\n')

        if menu == '1':
            print('Você optou por colar a figurinha')
            colar = int(input('Qual figuriha você deseja colar? '))-1
            conta.colarFigurinhaAlbum(colar)

        elif menu == '2':
            print('Disponibiizar figurinha para troca')
            nro = int(input('Qual figurinha você deseja disponibilizar para troca? ')) -1
            conta.disponibilizarFigurinhaTroca(nro)

        elif menu == '3':
            print('3 - Propor troca de Figurinhas')
            print('Lista de usuários')
            nro =1
            for usuario in usuarios:
                print(nro, '-', usuario.getNomeDeUsuario())
                for status in range(len(usuario.statusDasFigurinhas())):
                    if usuario.statusDasFigurinhas()[status] == 3:
                        print('Figurinha', status+1, 'disponível para troca')

                nro +=1
            usuarioTroca = int(input('Diga o número do usuário comquem deseja realizar a troca:\n'))-1
            trocaDesejada = int(input('Informe o número da figurinha que você quer para você\n'))-1
            figurinhaIndesejada = int(input('Qual figurinha você não quer mais?\n'))-1
            if conta.possuiFigurinhaNaColecao(figurinhaIndesejada):
                trocas.append(Troca(conta.getNomeDeUsuario(), usuarios[usuarioTroca].getNomeDeUsuario(), trocaDesejada, figurinhaIndesejada))
            else:
                print('você não tem essa figurinha na coleção')
            

        elif menu == '4':
            print('Revisar solicitações de troca')
            for troca in trocas:
                if troca.informarNomeRequerido() == conta.getNomeDeUsuario() and not troca.status():
                    print(troca.informarNomeProponente(), 'deseja trocar a carta número', troca.figurinhaRequerida()+1, 'pela carta', troca.figurinhaDisponivel()+1, '.')
                    aceitar = input('Aceita realizar a troca? (s/n)\n')
                    if aceitar == 'n':
                        print('Você recusou a troca')
                        troca.recusar()
                    elif aceitar == 's':
                        print('Troca feita')
                        troca.aceitar()
                    else:
                        print('Opção inválida, tente novamente')
                    break  # Sair do loop após a escolha do usuário
            #for troca in trocas:
            #    if troca.informarNomeRequerido() == conta.getNomeDeUsuario() and not troca.status():
            #        print(troca.informarNomeProponente(), 'deseja trocar a carta número', troca.figurinhaRequerida(),'pela carta', troca.figurinhaDisponivel(),'.')
            #        aceitar = input('Aceita realizar a troca? (s/n)\n')
            #        teste = False
            #        while not teste:
            #            if aceitar == 'n':
            #                print('Você recusou a troca')
            #                teste.recusar()
            #                teste = True
            #                break
            #            elif aceitar == 's':
            #                print('Troca feita')
            #                troca.aceitar()
            #                teste = True
            #                break
            #            else:
            #                print('Opção inválida, tente novamente')
                
            #    else:
            #        print('Ninguém deseja trocar com você')


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
            novafigurinha = [random.randint(0,19),random.randint(0,19),random.randint(0,19)]
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