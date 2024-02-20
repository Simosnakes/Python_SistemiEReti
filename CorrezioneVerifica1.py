def main():
    for numero in range(1, 1000):
        numero_str = str(numero)
        lista_cifre = [int(cifra) ** 3 for cifra in numero_str]
        somma_cubi = sum(lista_cifre)
        if somma_cubi == numero:
            print(f"il numero {numero} è narcisista")

if __name__ == "__main__":
    main()