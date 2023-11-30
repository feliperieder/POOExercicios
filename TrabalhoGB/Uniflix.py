import csv

class Usuario:
    def __init__(self,  nome_usuario, senha, tipo = 'Simples', lista_perfis = None) -> None:
        self._nome_usuario = nome_usuario
        self.__senha = senha
        self._tipo = tipo
        if lista_perfis:
            self._lista_perfis = lista_perfis
        else:
            self._lista_perfis = []
        if self._tipo == 'Simples':
            self.__n_usuarios = 3
        elif self._tipo == 'Premium':
            self.__n_usuarios = 5

    def adicionarPerfil(self, nome, idade, lista_favoritos = [], ultimos_assistidos = []):
        if len(self._lista_perfis) < self.__n_usuarios:
            self._lista_perfis.append(Perfil(nome, idade, lista_favoritos, ultimos_assistidos))
            print('Perfil adicionado')

        else:
            print('Sua conta não te permite ter essa quantidade de perfis')
            print('Número de perfis atuais:', len(self._lista_perfis))       

    def excluirPerfil(self, nome):
        perfil_excluido = None
        for nro in range(len(self._lista_perfis)):
            if self._lista_perfis[nro]._nome == nome:
                perfil_excluido = nro
        
        if perfil_excluido == None:
            print("Não exiter peril com esse nome")
        else:
            del self._lista_perfis[perfil_excluido]
            print('Perfil excluído')
        
        print('Lista de perfis:')
        for perfil in self._lista_perfis:
            print(perfil._nome)

    def alterarSenha(self, novaSenha):
        self.__senha = novaSenha
        print('Senha alterada com sucesso!')

    def alterarPlano(self, novoTipo):
        if novoTipo == 'Simples':
            self._tipo = novoTipo
            self.__n_usuarios = 3
            print('Seu plano foi atualizado')
            print('Benefícios:\n - Direito a 3 perfis\n - Propagandas entre mídias assistidas\n - Custo 29,90 mensal')
        elif novoTipo == 'Premium':
            self._tipo = novoTipo
            self.__n_usuarios = 5
            print('Seu plano foi atualizado')
            print('Benefícios:\n - Direito a 5 perfis\n - Sem propagandas\n - Custo 49,90 mensal')
        else:
            print('Esse plano não existe. Tente novamente digitando "premium" ou "simples".')

    def verificarLogin(self, nomeDeUsuario, senha):
        if nomeDeUsuario == self._nome_usuario:
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

class Perfil:
    def __init__(self, nome, idade, lista_favoritos = None, ultimos_assistidos = None) -> None:
        self._nome = nome
        self.__idade = idade
        if lista_favoritos:
            self.__lista_favoritos = lista_favoritos
        else: 
            self.__lista_favoritos = []
        if ultimos_assistidos:
            self.__ultimos_assistidos = ultimos_assistidos
        else: 
            self.__ultimos_assistidos = []
        
    def adicionarFavorito(self, media):
        if len(self.__lista_favoritos) < 10:
            self.__lista_favoritos.append(media)
            print('Mídia favoritada')
        else:
            print('Sua lista de favoritos já está cheia. Por favor, remova um item da sua lista para adicionar outro')

    def removerFavorito(self, media):
        media_removida = None
        for nro in range(len(self.__lista_favoritos)):
            if self.__lista_favoritos[nro] == media:
                media_removida = nro
        
        if media_removida == None:
            print("Não exite nenhuma mídia com esse ID")
        else:
            del self.__lista_favoritos[media_removida]
            print('Mídia removida da lista de favoritos.')

    def adicionarUltimoAssistido(self, media):
        assistido = None
        for nro in range(len(self.__ultimos_assistidos)):
            if self.__ultimos_assistidos[nro] == media:
                assistido = nro
        if assistido != None:
            del self.__ultimos_assistidos[nro]

        
        if len(self.__ultimos_assistidos) < 10:
            self.__ultimos_assistidos.append(media)
        else:
            del self.__ultimos_assistidos[0]
            self.__ultimos_assistidos.append(media)

    def listarMediasApropriadas(self, tipo, catalogo):
        lista_exigida = catalogo.obterLista(tipo)
        lista_apropriada = []
        for media in lista_exigida:
            if media.classificacao() == 'L':
                lista_apropriada.append(media)
            elif int(media.classificacao()) <= int(self.__idade):
                lista_apropriada.append(media)
        return(lista_apropriada)

    def assistirMedia(self, media):
        print('Você acabou de assisitir', media._titulo)
        self.adicionarUltimoAssistido(media)

    def favoritar(self, media):
        favorito = False
        for nro in range(len(self.__lista_favoritos)):
            if media._titulo == self.__lista_favoritos[nro]._titulo:
                favorito = True

        if not favorito:
            self.adicionarFavorito(media)
        else:
            self.removerFavorito(media)

    def buscarTitulo(self, procurar_titulo, catalogo):
        encontrou = False
        for filme in catalogo.obterLista('Filme'):
            if procurar_titulo == filme._titulo:
                encontrou = True
                media_achada = filme
        for documentario in catalogo.obterLista('Documentário'):
            if procurar_titulo == documentario._titulo:
                encontrou = True
                media_achada = documentario
        for animacao in catalogo.obterLista('Animação'):
            if procurar_titulo == animacao._titulo:
                encontrou = True
                media_achada = animacao
        for serie in catalogo.obterLista('Série'):
            if procurar_titulo == serie._titulo:
                encontrou = True
                media_achada = serie
        for programa in catalogo.obterLista('Programa de Auditório'):
            if procurar_titulo == programa._titulo:
                encontrou = True
                media_achada = programa
            
        if encontrou:
            return media_achada

        else:
            return None
        
    def ultimosAssistidos(self):
        return self.__ultimos_assistidos
    
    def favoritos(self):
        return self.__lista_favoritos

class Media:
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao) -> None:
        self._id = id
        self._tipo = tipo
        self._titulo = titulo
        self.__genero = genero
        self.__lancamento = lancamento
        self.__classificacao = classificacao

    def exibirInfo(self):
        print('Genêro:', self.__genero, '\nLançamento:', self.__lancamento, '\nClassificação Indicativa:', self.__classificacao)
    
    def classificacao(self):
        return self.__classificacao

class Serie(Media):
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao, n_temporadas, ep_por_temporada = None) -> None:
        super().__init__(id, tipo, titulo, genero, lancamento, classificacao)
        self.__n_temporadas = int(n_temporadas)
        if ep_por_temporada:
            self.__ep_por_temporada = ep_por_temporada
        else:
            self.__ep_por_temporada = [] 

        while len(self.__ep_por_temporada)+1 <= self.__n_temporadas:
            self.__ep_por_temporada.append([])

    def temporadas(self):
        return self.__n_temporadas

    def classificacao(self):
        return super().classificacao()

    def exibirInfo(self):
        print(self._titulo, 'é uma série de', self.__n_temporadas, 'temporadas.')
        return super().exibirInfo()
    
    def listarEpisodios(self):
        temporada = int(input('Selecione a temporada que você deseja assistir (ex. 1, 2).\nNúmero de temporadas {}:\n'.format(self.__n_temporadas)))
        if temporada <= len(self.__ep_por_temporada):
            contador = 1
            for episodio in self.__ep_por_temporada[temporada-1]:
                print(contador, '-', episodio)
                contador +=1
            return self.__ep_por_temporada[temporada-1]
        else:
            print('Error')

    def adicionarEpisodio(self, temporada, titulo):
        self.__ep_por_temporada[temporada -1].append(titulo)

class Filme(Media):
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao, diretor, produtor) -> None:
        super().__init__(id, tipo, titulo, genero, lancamento, classificacao)
        self.__diretor = diretor
        self.__produtor = produtor

    def classificacao(self):
        return super().classificacao()

    def exibirInfo(self):
        print(self._titulo, 'é um Filme dirigido por', self.__diretor, 'e produzido por', self.__produtor)
        return super().exibirInfo()

class Documentario(Media):
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao, tema) -> None:
        super().__init__(id, tipo, titulo, genero, lancamento, classificacao)
        self.__tema = tema

    def exibirInfo(self):
        print(self._titulo, 'é um Documentário sobre', self.__tema)
        return super().exibirInfo()
    def classificacao(self):
        return super().classificacao()

class Animacao(Media):
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao, estudio) -> None:
        super().__init__(id, tipo, titulo, genero, lancamento, classificacao)
        self.__estudio = estudio

    def exibirInfo(self):
        print(self._titulo, 'é um filme de animação lançado pelos estúdios', self.__estudio)
        return super().exibirInfo()   

    def classificacao(self):
        return super().classificacao()
    
class Programa_TV(Media):
    def __init__(self, id, tipo, titulo, genero, lancamento, classificacao, lista_ep = None) -> None:
        super().__init__(id, tipo, titulo, genero, lancamento, classificacao)
        if lista_ep:
            self.__lista_ep = lista_ep
        else:
            self.__lista_ep = []
        self.__nro_eps = len(self.__lista_ep)

    def classificacao(self):
        return super().classificacao()
    def exibirInfo(self):
        print(self._titulo, 'é um programa de TV com', self.__nro_eps, 'episódios.')
        return super().exibirInfo()
    
    def listarEpisodios(self):
        print('Episódios de {}:'.format(self._titulo))
        contador = 1
        for episódio in self.__lista_ep:
            print(contador, '-', episódio)
            contador +=1
        return self.__lista_ep

    def adicionarEpisodio(self, temporada, titulo):
        self.__lista_ep.append(titulo)

class Catalogo:
    def __init__(self, series = [], filmes = [], documentarios = [], animacoes = [], programas_de_tv = []) -> None:
        self.__series = series
        self.__filmes = filmes
        self.__documentarios = documentarios
        self.__animacoes = animacoes
        self.__programas_de_tv = programas_de_tv

    def adicionarMedia(self, media, tipo):
        if tipo == 'Filme':
            self.__filmes.append(media)
        elif tipo == 'Documentário':
            self.__documentarios.append(media) 
        elif tipo == 'Animação':
            self.__animacoes.append(media)
        elif tipo == 'Série':
            self.__series.append(media)
        elif tipo == 'Reality Show' or linha[1] == 'Programa de Auditório':
            self.__programas_de_tv.append(media)

    def obterLista(self, tipo):
        if tipo == 'Série':
            lista = self.__series
        elif tipo == 'Filme':
            lista = self.__filmes
        elif tipo == 'Documentário':
            lista = self.__documentarios
        elif tipo == 'Animação':
            lista = self.__animacoes
        elif tipo == 'Reality Show' or tipo == 'Programa de Auditório':
            lista = self.__programas_de_tv
        return lista
    
    def buscarID(self, procurar_id):
        encontrou = False
        for filme in self.__filmes:
            if procurar_id == filme._id:
                encontrou = True
                media_achada = filme
        for documentario in self.__documentarios:
            if procurar_id == documentario._id:
                encontrou = True
                media_achada = documentario
        for animacao in self.__animacoes:
            if procurar_id == animacao._id:
                encontrou = True
                media_achada = animacao
        for serie in self.__series:
            if procurar_id == serie._id:
                encontrou = True
                media_achada = serie
        for programa in self.__programas_de_tv:
            if procurar_id == programa._id:
                encontrou = True
                media_achada = programa
            
        if encontrou:
            return media_achada

        else:
            return None

lista_serie = []
lista_filme = []
lista_documentario = []
lista_animacao = []
lista_programaTV = []
#Adicionando catálogo
with open('.\CatalogoExemplo.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=';')
    for linha in leitor_csv:
        if linha[1] == 'Filme':
            lista_filme.append(Filme(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[7], linha[8]))
        elif linha[1] == 'Documentário':
            lista_documentario.append(Documentario(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[8])) 
        elif linha[1] == 'Animação':
            lista_animacao.append(Animacao(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[9]))
        elif linha[1] == 'Série':
            lista_serie.append(Serie(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))
        elif linha[1] == 'Reality Show' or linha[1] == 'Programa de Auditório':
            lista_programaTV.append(Programa_TV(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]))

catalogo = Catalogo(lista_serie, lista_filme, lista_documentario, lista_animacao, lista_programaTV)
catalogo.adicionarMedia(Serie(25, 'Série', 'Dark', 'Drama', 2017, 16, 4), 'Série')
catalogo.adicionarMedia(Programa_TV(27, 'Programa de Auditório', 'Receitas da Vovó', 'Culinária', 2010, 'L'), 'Programa de Auditório')

#Adicionando episódios
with open('.\EpisodiosSeriesProgramasTVExemplo.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=';')
    for linha in leitor_csv:
        for serie in catalogo.obterLista('Série'):
            if linha[1] == serie._titulo:
                serie.adicionarEpisodio(int(linha[3]), linha[2])
        for programa in catalogo.obterLista('Programa de Auditório'):
            if linha[1] == programa._titulo:
                programa.adicionarEpisodio(int(linha[3]), linha[2])

#Teste
#serie = Serie(0, 'Série', 'Stranger Things','Suspense',2016,16,4,[['T1E1','T1E2','T1E3','T1E4','T1E5'],['T2E1','T2E2','T2E3','T2E4','T2E5'],['T3E1','T3E2','T3E3','T3E4','T3E5'],['T4E1','T4E2','T4E3','T4E4','T4E5']])
#serie.exibirInfo()
#auditorio = Programa_TV(20,'Programa de Auditório', 'The Tonight Show Starring Jimmy Fallon','Entretenimento', 2014, 'L', ['Episódio 1', 'Episódio 2', 'Episódio 3', 'Episódio 4', 'Episódio 5'])
#auditorio.exibirInfo()
#auditorio.listarEpisodios()
#serie.adicionarEpisodio(2, 'Confuso')
#serie.listarEpisodios()

#Adicionando Usuários
usuarios = []
with open('.\ExemploUsuarios.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=';')
    next(leitor_csv)
    for linha in leitor_csv:
        usuarios.append(Usuario(linha[1], linha[2], linha[3]))

#Adicionando perfis
with open('.\ExemploPerfis.csv', mode = 'r', encoding='utf-8', newline='') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=';')
    next(leitor_csv)
    for linha in leitor_csv:
        for usuario in usuarios:
            if linha[0] == usuario._nome_usuario:
                fav = []
                ult = []
                count = 0
                while count < 10:
                    fav_uni = catalogo.buscarID(linha[count + 3])
                    ult_uni = catalogo.buscarID(linha[count + 10])
                    if fav_uni:
                        fav.append(fav_uni)
                    if ult_uni:
                        ult.append(ult_uni)
                    count += 1
                usuario.adicionarPerfil(linha[1], linha[2], fav, ult)

#Menu de Episódios
def menuEpisodios(perfil, media):
    if media._tipo == 'Série':
        menu_ep= ''
        temporada = media.listarEpisodios()
        while menu_ep != 0:
            menu_ep = int(input('Qual episódio você deseja assistir (0 para voltar)\n'))
            if menu_ep <= len(temporada) and menu_ep -1 >= 0:
                if temporada[menu_ep-1]:
                    perfil.assistirMedia(media)
                else:
                    print('Opção inválida')
            elif menu_ep == 0:
                pass
            else:
                print('Opção inválida')

    else:
        menu_ep = ''
        eps = media.listarEpisodios()
        while menu_ep != 0:
            menu_ep = int(input('Qual episódio você deseja assistir (0 para voltar)\n'))
            if menu_ep <= len(eps) and menu_ep -1 >= 0:
                if eps[menu_ep-1]:
                    perfil.assistirMedia(media)
                else:
                    print('Opção inválida')
            elif menu_ep == 0:
                pass
            else:
                print('Opção inválida')

#Menu Mídia
def menuMedia(perfil, media):
    print(media._titulo)
    print(media.exibirInfo())


    if media._tipo == 'Reality Show' or media._tipo == 'Programa de Auditório' or media._tipo == 'Série':
        menu_media = ''
        while menu_media != '3':
            menu_media = input('O que você deseja fazer?\n1 - Listar Episódios\n2 - Favoritar/Desfavoritar\n3 - Voltar\n')
            if menu_media == '1':
                menuEpisodios(perfil, media)
            elif menu_media == '2':
                perfil.favoritar(media)
            elif menu_media == '3':
                pass
            else:
                print('Opção inválida, tente novamente')
    else:
        menu_media = ''
        while menu_media != '3':
            menu_media = input('O que você deseja fazer?\n1 - Assistir\n2 - Favoritar/Desfavoritar\n3 - Voltar\n')
            if menu_media == '1':
                perfil.assistirMedia(media)
            elif menu_media == '2':
                perfil.favoritar(media)
            elif menu_media == '3':
                pass
            else:
                print('Opção inválida, tente novamente')

#Menu Listar Mídia
def menuListarMedia(perfil, medias):
    contador = 1
    for media in medias:
        if media:
            print(contador, '-', media._titulo)
            contador +=1
    acessar = int(input("Digite o número da mídia que você deseja acessar. Digite qualquer outro número para voltar\n"))
    if acessar <= len(medias) and acessar -1 >= 0:
        if medias[acessar-1]:
            print(acessar - 1)
            menuMedia(perfil, medias[acessar -1])
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')

#Menu Perfil
def menuPerfil(perfil_acessado, catalogo):
    menu = ''
    while menu != '9':
        menu = input('O que você deseja fazer?\n1 - Busca por nome\n2 - Últimos Assistidos\n3 - Favoritos\n4 - Filmes\n5 - Séries\n6 - Documentários\n7 - Animações\n8 - Programas de TV\n9 - Voltar\n')
        if menu == '1':
            procurar_titulo = input('Digite o título que você está procurando:\n')
            titulo_encontrado = perfil_acessado.buscarTitulo(procurar_titulo, catalogo)
            if titulo_encontrado:
                menuMedia(perfil_acessado, titulo_encontrado)
            else:
                print('Esse título não está no catálogo.')

        elif menu == '2':
            print('Lista de últimos assistidos')
            menuListarMedia(perfil_acessado, perfil_acessado.ultimosAssistidos())
                
        elif menu == '3':
            print('Lista de favoritos')
            menuListarMedia(perfil_acessado, perfil_acessado.favoritos())

        elif menu == '4':
            print('Lista de Filmes')
            menuListarMedia(perfil_acessado, perfil_acessado.listarMediasApropriadas('Filme', catalogo))

        elif menu == '5':
            print('Lista de Séries')
            menuListarMedia(perfil_acessado, perfil_acessado.listarMediasApropriadas('Série', catalogo))

        elif menu == '6':
            print('Lista de Documentários')
            menuListarMedia(perfil_acessado, perfil_acessado.listarMediasApropriadas('Documentário', catalogo))

        elif menu == '7':
            print('Lista de Animações')
            menuListarMedia(perfil_acessado, perfil_acessado.listarMediasApropriadas('Animação', catalogo))

        elif menu == '8':
            print('Lista de programas de TV')
            menuListarMedia(perfil_acessado, perfil_acessado.listarMediasApropriadas('Programa de Auditório', catalogo))
            
        elif menu == '9':
            pass
        else:
            print('Opção inválida, tente novamente')

#Menu Usuário
def menuUsuario(conta, catalago):
    menu = ''
    while menu != '5':
        for perfil in conta._lista_perfis:
            print(perfil._nome)
        
        menu = input('O que você deseja fazer?\n1 - Alterar assinatura\n2 - Acessar perfil\n3 - Adicionar Perfil\n4 - Remover perfil\n5 - Voltar\n')

        if menu == '1':
            novo_plano = input('O seu plano atual é {}, para qual você deseja atualizar?\n'.format(conta._tipo))
            conta.alterarPlano(novo_plano)

        elif menu == '2':
            perfil_acessando = input('Qual perfil você deseja acessar?\n')
            existe = False
            for nro in range(len(conta._lista_perfis)):
                if perfil_acessando == conta._lista_perfis[nro]._nome:
                    existe = True
                    perfil_acessado = conta._lista_perfis[nro]
                
            if existe:
                menuPerfil(perfil_acessado, catalogo)
            else:
                print('Esse perfil não existe')
                
        elif menu == '3':
            perfil_novo = input('Que nome você deseja dar ao novo perfil?\n')
            idade_perfil = input('Qual é a idade de quem utilizará o novo perfil?\n')
            conta.adicionarPerfil(perfil_novo, idade_perfil)

        elif menu == '4':
            perfil_removido = input('Qual o nome do perfil que você deseja remover?\n')
            conta.excluirPerfil(perfil_removido)              

        elif menu == '5':
            pass
        else:
            print('Opção inválida, tente novamente')

#Menu Inicial
menu = ''    
while menu != '3':
    menu = input('O que você deseja fazer?\n1 - Acessar conta\n2 - Criar conta\n3 - Sair do aplicativo\n')

    if menu == '2':
        nome = input('Defina o nome do Usuário: ')
        senha = input('Defina a senha: ')
        usuarios.append(Usuario(nome, senha))

    elif menu == '1':
        nome = input('Informe o nome do Usuário: ')
        senha = input('Informe a senha: ')
        existe = False
        for i in range(len(usuarios)):
            if usuarios[i].verificarLogin(nome, senha):
                existe = True
                conta = usuarios[i]
        
        if existe:
            menuUsuario(conta, catalogo)
        else:
            print('Nome de usuário e/ou senha incorretos')
            

    elif menu == '3':
        print('Encerrando atividades no aplicativo')

    else:
        print('Opção inválida, tente novamente')