import random
#random.choise(lista di oggetti)

def movimento(lista):
    return random.choice(lista)

#def movimento(lista[1, -1]):
    #pass

def main():
    tempo = 60 * 60 * 24 * 5
    lista = [1, -1]

    movimenti = [movimento(lista) for _ in range (tempo)]
    #movimenti = [movimento() for _ in range (tempo)] passaggio di parametri con valore di default
    print(movimenti)

    movTot = 0
    for spost in movimenti:
        movTot += spost
    print(movTot)
    
if __name__ == "__main__":
    main()