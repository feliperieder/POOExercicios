class Pais:
    def __init__(self, codigo=None, nome=None, populacao=None, dimensao=None, vizinhos = []):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__vizinhos = vizinhos

    def __eq__(self, outro) -> bool:
        if isinstance(outro, Pais):
            return self.__codigo == outro.__codigo
        return False
    
    def codigoENome(self):
        return self.__codigo, self.__nome
    def populacao(self):
        return self.__populacao
    def dimensao(self):
        return self.__dimensao

    def imprimirInfos(self):
        print ('Nome: ',self.__nome)
        print ('Codigo: ', self.__codigo)
        print ('Populacao: ', self.__populacao)
        print ('Dimensao ', self.__dimensao, 'Km²')
        print ('Lista de paises vizinhos: ')
        for vizinho in self.__vizinhos:
            vizinhoCodigo, vizinhoNome = vizinho.codigoENome()
            print(vizinhoCodigo, '-', vizinhoNome)

    def add_vizinho(self, vizinho):
        if vizinho not in self.__vizinhos:
            self.__vizinhos.append(vizinho)

    def e_vizinho(self, outro):
        return outro in self.__vizinhos
    
    def densidade_populacional(self):
        self.densidade = self.__populacao/self.__dimensao
        return self.densidade
    
    def vizinhos_semelhantes(self, outro):
        vizinhos_comum = []
        for vizinho in self.__vizinhos:
            if outro.e_vizinho(vizinho):
                vizinhos_comum.append(vizinho)
        return vizinhos_comum
    

class Continente:
    def __init__(self, nome, paises=[]) -> None:
        self.__nome = nome
        self.__paises = paises

        self.dimensaoTotal()
        self.populacaoTotal()

    def add_pais(self, pais):
        if pais not in self.__paises:
            self.__paises.append(pais)
            self.dimensaoTotal()
            self.populacaoTotal()

    def dimensaoTotal(self):
        self.__dimensao = 0
        for pais in self.__paises:
            self.__dimensao += pais.dimensao()
        return self.__dimensao
    
    def populacaoTotal(self):
        self.__populacao = 0
        for pais in self.__paises:
            self.__populacao += pais.populacao()
        return self.__populacao
    
    def densidadePopulacional(self):
        densidadePop = self.__populacao/self.__dimensao
        return densidadePop
    
    def paisMaisPop(self):
        popPaisMaisPop = self.__paises[0].populacao()
        for pais in self.__paises:
            if pais.populacao() >= popPaisMaisPop:
                popPaisMaisPop = pais.populacao()
                paisMaisPop = pais

        return paisMaisPop

    def paisMenosPop(self):
        popPaisMenosPop = self.__paises[0].populacao()
        for pais in self.__paises:
            if pais.populacao() <= popPaisMenosPop:
                popPaisMenosPop = pais.populacao()
                paisMenosPop = pais

        return paisMenosPop

    def maiorPais(self):
        maiorPaisDimensao = self.__paises[0].dimensao()
        for pais in self.__paises:
            if pais.dimensao() >= maiorPaisDimensao:
                maiorPaisDimensao = pais.dimensao()
                self.__maiorPais = pais

        return self.__maiorPais

    def menorPais(self):
        menorPaisDimensao = self.__paises[0].dimensao()
        for pais in self.__paises:
            if pais.dimensao() <= menorPaisDimensao:
                menorPaisDimensao = pais.dimensao()
                self.__menorPais = pais

        return self.__menorPais

    def razaoMaiorMenor(self):
        razao = self.__maiorPais.dimensao()/self.__menorPais.dimensao()
        return razao
        
    def Informacoes(self):
        print('Nome:', self.__nome)
        print('Dimesão:', self.__dimensao, 'Km²')
        print('População:', self.__populacao)
        print('Países:')
        for pais in self.__paises:
            codigo, nome = pais.codigoENome()
            print(codigo, '-', nome)


# Usando valores padrao de argumentos
uruguai = Pais('URY', 'Uruguai', 3473730, 176215)
argentina = Pais('ARG', 'Argentina', 45195774, 2780400, vizinhos=[uruguai])
uruguai.add_vizinho(argentina)
paraguai = Pais('PRY', 'Paraguai', 7132538, 406752, vizinhos=[argentina])
argentina.add_vizinho(uruguai)
bolivia = Pais('BOL', 'Bolivia', 11673021, 1098581, vizinhos=[paraguai, argentina])
paraguai.add_vizinho(bolivia)
argentina.add_vizinho(bolivia)
peru = Pais('PER', 'Peru', 33050325, 1285216, vizinhos=[bolivia])
bolivia.add_vizinho(bolivia)
bra = Pais('BRA', 'Brasil', 214886771, 8515767.049, vizinhos=[uruguai, argentina, paraguai, bolivia, peru])
uruguai.add_vizinho(bra)
argentina.add_vizinho(bra)
paraguai.add_vizinho(bra)
bolivia.add_vizinho(bra)
peru.add_vizinho(bra)

bra.imprimirInfos()
print("Densidade Poplacional:", bra.densidade_populacional())


print('Vizinhos que Brasil tem com a Bolívia:')
for vizinhos in bra.vizinhos_semelhantes(bolivia):
    codigo, nome = vizinhos.codigoENome()
    print(nome)

america_sul = Continente('América do Sul', [uruguai,argentina,paraguai,bolivia,peru])
america_sul.Informacoes()
america_sul.add_pais(bra)
america_sul.Informacoes()
codigoMaior, nomeMaior = america_sul.maiorPais().codigoENome()
codigoMenor, nomeMenor = america_sul.menorPais().codigoENome()
codigoMenosPop, nomeMenosPop = america_sul.paisMenosPop().codigoENome()
codigoMaisPop, nomeMaisPop = america_sul.paisMaisPop().codigoENome()
print('Maior país:', codigoMaior, '-', nomeMaior)
print('Menor país:', codigoMenor, '-', nomeMenor)
print('País mais populoso:', codigoMaisPop, '-', nomeMaisPop)
print('País menos populoso:', codigoMenosPop, '-', nomeMenosPop)
print(america_sul.razaoMaiorMenor())