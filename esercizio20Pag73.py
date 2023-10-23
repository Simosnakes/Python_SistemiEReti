def main():
    max = 10

    tavola = [[k * i for i in range(1, max + 1)] for k in range(1, max + 1)]
    #print(tavola)

    for k, tabellina in enumerate(tavola): #enumerate è una funzione che numera le liste e ritorna indice e elemento
        #tabellina è una lista tavola è una lista di liste
        print(f"Tabellina del: {k + 1}: {tabellina}")

    file = open("esercizio20pag73.txt", "w")

    for tabellina in tavola:
        file.write(f"{tabellina}\n")

    file.close()


if __name__ == "__main__":
    main()