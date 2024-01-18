import random

class Nemico():
    def __init__(self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
    def stampa(self):
        print(f"nemico in posizione {self.pos_x},\{self.pos_y} con {self.n_vite} vite")


def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    lista_nemici = []
    random.seed(1234) #seleziona il seme del generatore di numero pseudocasuali
    for _ in range(N_NEMICI):
        pos_x = random.randint(0, WIDTH - 1)
        pos_y = random.randint(0, HEIGHT - 1)
        nemico = Nemico(pos_x, pos_y, 5)
        lista_nemici.append(nemico)
    
    personaggio = {"posizione_x":100, "posizione_y":200}
    for nemico in lista_nemici:
        nemico.stampa()
        if (nemico.pos_x == personaggio["posizione_x"]) and (nemico.pos_y == personaggio["posizione_y"]):
            print("COLLISIONE")

if __name__ == "__main__":
    main()