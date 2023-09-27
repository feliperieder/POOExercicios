class Calculadora:

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1*n2

    def dividir(self, n1, n2):
        if n2 == 0:
            print('Erro: divisão por 0')
            return -1
        else:
            return n1/n2

def main():
    calculadora = Calculadora()
    soma =calculadora.somar(2, 3)
    subtracao = calculadora.subtrair(7,2)
    multiplicacao = calculadora.multiplicar(3,4)
    divisao0 = calculadora.dividir(3, 0)
    divisao = calculadora.dividir(4,2)

    print('Resultado da soma: {}\nResultado da subtração: {}\nResultado da multiplicação: {}\nResultado da divisão por zero: {}\nResultado da divisão: {}'.format(soma, subtracao, multiplicacao, divisao0, divisao))


if __name__ == "__main__":
    main()