def ricerca(dizionario):
    c = -1
    numeri = "0123456789"
    a = input("Inserisci il nome o numero di telefono: ")
    if(a[0] in numeri):
        for x in dizionario:
            if(x == int(a)):
                print(dizionario[x])
                c = 0
    else:
        for x in dizionario:
            if(dizionario[x] == a):
                print(x)
                c = 0
    if c == -1:
        print("Nome o numero non trovato")
 
def main():
    dizionario = {}
    file = open("esercizio16.txt", "r")

    righe = file.readlines()

    for riga in righe:
        campi = riga.split(", ")
        chiave = int(campi[1].replace("\n", "")) #sostituisce il primo carattere con il secondo
        nome = (campi[0])
        dizionario[chiave] = nome
        
    file.close()
    ricerca(dizionario)


    print(dizionario)

    

if __name__ == "__main__":
    main()