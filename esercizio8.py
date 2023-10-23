#esercizio 3 pag 40
def main():
    ope = int(input("Inserisci che operazione vuoi inerire 0: somma, 1: sottrazione, 2: moltiplicazione, 3: divisione"))<
    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))

    if ope == 0:
        ris = n1 + n2
    elif ope == 1:
        ris = n1 - n2
    elif ope == 2:
        ris = n1 * n2
    else:
        if n2 == 0:
            print("l'operazione non è possibile")
        else:
            ris = n1 / n2

    if n2 != 0:
        print(f"il risultato è : {ris}")
if __name__ == "__main__":
    main()