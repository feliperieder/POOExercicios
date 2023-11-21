class Assinatura:
    def __init__(self) -> None:
        print('Assinatura feita')

    def calcular_preco(self, preco):
        print('Preco da assinatura: R$', preco)

    def exibir_detalhes(self, info):
        print(info)


class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        precoFixo = 29.99
        return super().calcular_preco(precoFixo)

    
    def exibir_detalhes(self):
        info = 'Assinatura básica que fornece acesso a filmes e séries em qualidade padrão.'
        return super().exibir_detalhes(info)

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        preco = 49.99
        return super().calcular_preco(preco)
    
    def exibir_detalhes(self):
        info = 'Assinatura avançada que oferece acesso a filmes e séries em qualidade HD e Ultra HD.'
        return super().exibir_detalhes(info)
    
simples = AssinaturaSimples()
premium = AssinaturaPremium()

assinaturas = []
assinaturas.append(simples)
assinaturas.append(premium)

for assinatura in assinaturas:
    assinatura.calcular_preco()
    assinatura.exibir_detalhes()