"""
robot che si può spostare con ostacoli

definire una mappa (es. con un file csv)
0 se piastrella libera, 1 se occupata
0 e 1 vanno in un file csv
che dato il file, creare la matrice che rappresenta il pavimento
facoltativo: disegnarlo poi in pygame
scrivere una funzione che numeri le celle libere
in questo modo: 
0 1 -1 2
-1 3 4 5
poi da questa matrice restituire il dizionario delle adiacenze
"""
import pygame

LATOX = 100
LATOY = 100

class Cella():
    def __init__(self, n):
        self.size = (LATOX, LATOY)
        self.num = n
        self.numerata = True
        if n != 0:
            self.color = "red"
            self.numerata = False
        else:
            self.color = "white"
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)

def mat2d_adiacenze(m: list[list]):
    return {i: [j for j, n in enumerate(m[i]) if n != 0] for i in range(len(m))}

def matrice_da_file(nome_file: str):
    mat = []
    with open(nome_file, "r") as file:
        for riga in file.readlines():
            t = riga.split(", ")
            mat.append([int(stringa[0]) for stringa in t])
    return mat

def disegna_matrice(screen: pygame.Surface, mat: list[list[Cella]]):
    text = pygame.font.Font(size = LATOX // 2)
    numero_in_cella = 0
    for i, riga in enumerate(mat):
        y = LATOY * i
        for j, cella in enumerate(riga):
            screen.blit(cella.surf, (LATOX * j, y))
            if cella.numerata:
                surf = text.render(f"{numero_in_cella}", True, "black")
                rect = surf.get_rect()
                rect.topleft= (LATOX * j + 8, y + 8)
                screen.blit(surf, rect)
                numero_in_cella += 1
    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    m = matrice_da_file("robot.csv")

    screen = pygame.display.set_mode((LATOX * len(m), LATOY * len(m[0])))
    celle = [[Cella(n) for n in riga] for riga in m]
    disegna_matrice(screen, celle)
    diz = {}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(60)

if __name__ == "__main__":
    main()