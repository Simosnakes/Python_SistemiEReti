class Quadrato():
    def __init__(self, lato):
        self.lato = lato
    
    def calcoloArea(self):
        return (self.lato*self.lato)
    
    def calcolaPerimetro(self):
        return (self.lato*4)

    def puntoInterno(self, x, y):
        if(x > 0 and x < self.lato and y > 0 and y < self.lato):
            return True
        else:
            return False

def main():
    quad = Quadrato(3)
    print(quad.calcoloArea())
    print(quad.calcolaPerimetro())

    quad1 = Quadrato(7)
    print(quad1.calcoloArea())
    print(quad1.calcolaPerimetro())


if __name__ == "__main__":
    main()