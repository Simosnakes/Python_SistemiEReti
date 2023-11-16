def main():
    file = open("covid-19_gen1.txt", "r")
    stringa = ""
    for riga in file:
        riga = riga[:-1]
        stringa = stringa + riga

    print(stringa)

    file.close()
    conta = 0
    contc = 0
    contg = 0
    contt = 0

    for lettera in stringa:
        if lettera == "A":
            conta+=1
        elif lettera == "C":
            contc += 1
        elif lettera == "G":
            contg += 1
        else:
            contt += 1

    print(stringa.find("ATGTTTGTTTTT"))
    
    print(conta, contc, contg, contt)
    



if __name__ == "__main__":
    main()