import math

def main():
    num = int(input("Inserisci un numero: "))
    esponente = int(math.log2(num))
    lista = [2**i for i in range(0, esponente  + 1)]

    print(lista)

if __name__ == "__main__":
    main()
