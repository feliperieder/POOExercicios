class CadastroCliente:
    def __init__(self, nome, sobrenome, nasc, cpf, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nasc = nasc
        self.__cpf = cpf
        self.__senha = senha

    def exibirDados(self):
        print("Nome: ",self.__nome, " Sobrenome: ", self.__sobrenome, " Data de Nascimento: ", self.__nasc, " CPF: ", self.__cpf)

    def validarSenha(self, senhaDigitada):
        if self.__senha == senhaDigitada:
            return True
        else:
            return False   

#
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
nasc = input('Digite o a data de nascimento: ')
cpf = input('Digite o cpf:')
senha = input('Crie sua senha: ')

cliente = CadastroCliente(nome, sobrenome, nasc, cpf,senha)

tentativas = 0
acertou = False

while tentativas < 3 and acertou == False:
    senhaDigitada = input('Digite a senha: ')
    acertou = cliente.validarSenha(senhaDigitada)
    if acertou == True:
        cliente.exibirDados()
    else:
        print('errou')
    tentativas = tentativas + 1