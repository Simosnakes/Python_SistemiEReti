import pygame
from pygame.locals import *

def calc_pav():
    mat = [] 
    with open("robot.csv", "r") as file:
        for riga in file.readlines():
            riga = riga.split(", ")
            mat.append([int(c) for c in riga])
    return mat

#numerare le caselle libere la prima in alto a sinistra
def numera_celle():
    pass
#creare il dizionario delle adiacenze con come chiave la posizione e elemnti le caselle in cui si può spostare
def crea_diz_adiac():
    pass

def main():
    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    pygame.init()

    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]

    k = 0
    schermo = pygame.display.set_mode((lato_x * n_x, lato_y * n_y))

    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            if casella == 1:
                surf1.fill("red")
            else:
                surf1.fill("blue")


                k += 1
            
            rect1 = surf1.get_rect()
            rect1.topleft = (lato_x - 100, lato_y -100)
            schermo.blit(surf1, rect1)

            pygame.display.flip()
            lato_x += 100
        lato_x = 100
        lato_y += 100

    k = 1

    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0:
                matrice[indice_riga][indice_colonna] = k
                k += 1
            
    diz = {}

    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0:

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    pygame.quit()
if __name__ == "__main__":
    main()