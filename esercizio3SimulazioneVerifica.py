import random
#random.choise(lista di oggetti)

def movimento(lista):
    return random.choice(lista)


def main():
    tempo = 60 * 60 * 24 * 5
    lista = [1, -1]
    movimenti = []

    for spost in range(0, tempo):
        mov = movimento(lista)
        movimenti = [mov for _ in range (0, tempo)]
        #print(movimenti)


    movTot = 0
    for spost in movimenti:
        movTot += movimenti[spost]
    print(movTot)
    
if __name__ == "__main__":
    main()