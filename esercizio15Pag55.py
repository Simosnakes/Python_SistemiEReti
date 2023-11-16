def main():
    nome = input("inserisci il tuo nome: ")
    nome1 = nome[0] + "*" * (len(nome) - 1)
    print(nome1)

if __name__ == "__main__":
    main()