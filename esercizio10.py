#LE LISTE
def print_list(l):
    print("La lista è: ", end=' ')
    for elemento in l:
        print(elemento, end = ' ')
    print("\n")

def main():
    #l = [1, 2, 3, 4, "c", 3.14, "python"]
    #r = [10, 11, 12]
    #print(l)
    #print(l[-1])
    #print_list(l+r)#concatena le due liste
    #print_list(3*r)#concatena per tre volte la lista


    #vogliamo permettere all'utente di caricare una lista

    lista = []

    num = 1
    while num > 0:
        num = int(input("Scrivi un numero (-1 per interrompere): "))
        if num > 0:
            lista.append(num)#append serve ad aggiungere un numero alla lista
    print(lista)


if __name__ == "__main__":
    main()