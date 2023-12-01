def contaNucleotiti(stringa):
    dizNucleotiti = {"A":0, "C":0, "G":0, "T":0}
    for char in stringa:
        dizNucleotiti[char] += 1
    return dizNucleotiti

def contaNucleotiti2(stringa, nucleotide):
    return len([x for x in string if x == nucleotide])

def main():
    file = open("covid-19_gen1.txt", "r")
    stringa = ""
    for riga in file:
        riga = riga[:-1]
        stringa = stringa + riga

    file.close()

    print(stringa)

    conta, contc, contg, contt = 0, 0, 0, 0

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
    print(contaNucleotiti(stringa))
    



if __name__ == "__main__":
    main()