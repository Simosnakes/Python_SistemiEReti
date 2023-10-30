#chiedere un numero n tra 1 e 31 subnet musk in CIDR si deve scrive in notazione decimale puntato
def completa8bit(subnet):
    
    return "1"*subnet + "0" * (32 - subnet)


def main():

    trovato = False

    while trovato == False:
        subnet = int(input("Inserisci un numero compreso tra 1 e 31: "))
        if(subnet < 1 or subnet > 31):
            print("notazione cidr sbagliata")
        trovato = True
    

    subnetBin = completa8bit(subnet)
    gruppo1 = subnetBin[0:8]
    gruppo2 = subnetBin[8:16]
    gruppo3 = subnetBin[16:24]
    gruppo4 = subnetBin[24:32]
    
    print(f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}")

    gruppo1 = int(gruppo1,2)
    gruppo2 = int(gruppo2,2)
    gruppo3 = int(gruppo3,2)
    gruppo4 = int(gruppo4,2)
    
    print(f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}")



if __name__ == "__main__":
    main()