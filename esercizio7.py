def main():
    num = int(input("Inserisci un numero: "))

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print("Il numro è divisibile per 2, 3 o 5")
    else:
        print("Il numero non è divisibile per nessuna delle opzioni")

if __name__ == "__main__":
    main()
