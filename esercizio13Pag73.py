class Robot():
    def __init__(self, nome, massa, tipo):
        self.nome = nome
        self.massa = massa
        self.tipo = tipo
    
    def stampaNome(self):
        print(self.nome)

    def isPericoloso(self):
        return (self.massa > 100 and self.tipo == 'umanoide')

def main():
    mio = Robot("rb18", 112, 'umanoide')

    mio.stampaNome()

    if(mio.isPericoloso() == True):
        print("Il robot umanoide è pericoloso")
    else:
        print("Il robot umanoide non è pericoloso")


if __name__ == "__main__":
    main()