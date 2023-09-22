def main():#definizione della funzione main
    nome = input ("come ti chiami? ")#la funzione input ritorna sempre solo stringhe
    anni = int(input("Quanti anni hai? "))
    annoCorr = int(input("In quale anno siamo? "))
    print(f"Il tuo nome è {nome} e hai {anni} anni sei nato nel {annoCorr - anni}")#la f permette di concatenare una variabile nella stringa
    #print(type(anni))#type permettere di vedere di che tipo è una variabile

if __name__ == "__main__":
    main()