#CIFRARIO DI VERNAM

#fare una classe testo che quando la istanziamo deve contenere un testo in chiaro sia uno codificato
#classe con testo chiave e un bool che dice se è codificato o no
lettere = "abcdefghilmnopqrstuvz ?"
lettere2numeri = {}
numeri2lettere = {}
N  = len(lettere)

class Testo:
    def __init__(self, testo, chiave, codificato):
        self.testo_chiaro = testo.lower()
        self.chiave = chiave.lower()
        self.codificato = codificato
        self.testo_criptato = ""
        self.testo_de_criptato = ""
    
    def traduci(self, lettere2numeri, numeri2lettere):
        if self.testo_chiaro == "":
            for lettera_testo, lettera in zip(self.testo_chiaro, self.chiave):
                numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera]) % N
                self.testo_criptato += numeri2lettere[numero]
            print(f"il testo '{self.testo_chiaro}' diventa '{self.testo_criptato}'.")
        else:
            print("la stringa è già cifrata")

    def decifra(self, lettere2numeri, numeri2lettere):
        if self.testo_criptato == "":
            for lettera_testo, lettera in zip(testo_criptato, chiave):
                numero = (lettere2numeri[lettera_testo] - lettere2numeri[lettera]) % N
                self.testo_de_criptato += numeri2lettere[numero]
            print(f"Il testo da così '{self.testo_criptato}' diventa '{self.testo_de_criptato}'")
        else:
            print("la stringa è già cifrata")



def main():
    
    for posizione, lettera in enumerate(lettere):
        lettere2numeri[lettera] = posizione
        numeri2lettere[posizione] = lettera
    
    testo = Testo("ciao", "bv efh c uefbbc auic rhvbjsh ", codificato = False)
    testo.traduci(lettere2numeri, numeri2lettere)
    testo.decifra(lettere2numeri, numeri2lettere)
    

if __name__ =="__main__":
    main()
