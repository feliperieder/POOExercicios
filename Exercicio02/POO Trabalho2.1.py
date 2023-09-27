import random

class Dado:

    def __init__(self, faces):
        self.faces = faces

    def Rolar(self):
        return random.randint(1, self.faces)
    
def main():
    dado6Faces = Dado(6)
    dado8Faces = Dado(8)
    dado12Faces = Dado(12)

    print('Rolagens dos dados de 6 faces:')
    for i in range(3):
        print(dado6Faces.Rolar())
    print('Rolagens dos dado de 8 faces:')
    for i in range(3):
        print(dado8Faces.Rolar())

    print('Rolagens dos dado de 12 faces:')
    for i in range(3):
        print(dado12Faces.Rolar())


if __name__ == "__main__":
    main()