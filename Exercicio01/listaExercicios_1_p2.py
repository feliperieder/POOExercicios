import random

baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

class Musica:
    def __init__(self, musica, banda, estilo, lancamento, tempo):
        self.musica = musica
        self.banda = banda
        self.estilo = estilo
        self.lancamento = lancamento
        self.tempo = tempo
    
    def informarEstilo(self):
        print('O estilo de música de {} é {}'.format(self.musica, self.estilo))
    def informarBanda(self):
        print('A banda da música "{}" é {}'.format(self.musica, self.banda))
    def informarlancamento(self):
        print('O ano de lançamento da música "{}" é {}'.format(self.musica, self.lancamento))
    def informarTempo(self):
        print('O tempo de duração da música "{}" é {}'.format(self.musica, self.tempo))


       
fafefi = Musica('Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05')
sofre = Musica('Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58')
rock = Musica('Rock’n Rolo', 'The Buns','Rock',	1984, '4:01')
grif = Musica('Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' )
outra = Musica('Outra musica', 'Anira', 'Funk', 2019, '3:05')




def ExibirBaseDados():
    id = 0
    for i in baseDeDados:
        for j in i:
            print (id, '\t',j, end = '\t')
        id = id + 1
        print() #quebra de linha
    
    print('\n--------------------------------------------------\n')


#mMontar a playlist
playlist = []
IDrecord = []
def MontarPlaylist():
    montando = True
    while montando == True:
        ID = int(input('Informe o ID do da música: \n0 - Fa fe fi fo Funk\n1 - Sofrência de programar\n2 - Rock’n Rolo\n3 - Grifinoria Girls\n4 - Outra musica\n'))
        if ID in IDrecord:
            print('Já está na playlist')
        elif ID == 0:
            playlist.append(fafefi)
            IDrecord.append(ID)
        elif ID == 1:
            playlist.append(sofre)
            IDrecord.append(ID)
        elif ID == 2:
            playlist.append(rock)
            IDrecord.append(ID)

        elif ID == 3:
            playlist.append(grif)
            IDrecord.append(ID)
        elif ID == 4:
            playlist.append(outra)
            IDrecord.append(ID)
        opcao = ''
        while opcao != 'S' and opcao != 'N':
            opcao = input('Deseja adicionar nova música? (S/N): ')
            opcao = opcao.capitalize()
            if opcao == 'N':
               montando = False
            else:
                print('Opção inválida, tente novamente')
        
    #print para debug
    #print(playlist)

def visulizarPlaylist():
    print('Músicas na playlist:')
    for obj in playlist:
        print(obj.musica)
def embaralharPlaylist():
    random.shuffle(playlist)
    #debug
    #print(playlist)
def tempoPlaylist():
    minTotal, segTotal = 0, 0
    for obj in playlist:
        tempoStr = obj.tempo
        tempo = []
        tempo = tempoStr.split(':')
        min = float(tempo[0])
        seg = float(tempo[1])
        minTotal += min
        segTotal += seg
    minTotal += segTotal//60
    segTotal += - 60*(segTotal//60)

    print('O tempo de duração da playlist é de {}:{}'.format(int(minTotal), segTotal))



# a) Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela com todas as músicas

def __main__() -> None:
    fafefi.informarEstilo()
    rock.informarEstilo()
    grif.informarBanda()
    outra.informarBanda()
    sofre.informarlancamento()
    outra.informarTempo()

    MontarPlaylist()
    visulizarPlaylist()
    tempoPlaylist()


__main__()