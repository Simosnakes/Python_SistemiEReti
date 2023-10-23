"""def print_list(l):
    print("La lista è: ", end=' ')
    for elemento in l:
        if elemento != 0 or elemento != l - 1:
            if elemento == 4:
                l[4] = 10
            print(elemento, end = ' ')
    print("\n")"""

def main():
    lista = []
    nVoti = 0
    while True:
        num = int(input("Scrivi un numero (-1 per interrompere): "))
        if (num < 0 and nVoti >= 6):
            break
        
        lista.append(num)
        nVoti += 1

    
    print(lista[1:-1])

    lista[4] = 10

    print(lista[4])

    print(f"I primi tre voti sono: {lista[0:3]}")

if __name__ == "__main__":
    main()