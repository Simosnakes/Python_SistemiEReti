class Test():
    def __init__(self, stringa):
        self.stringa = stringa
        self.lista = self.stringa.split(" ")
    
    def calcoloNcaratteri(self):
        return len(self.stringa)

    def lista_parole(self):
        return self.lista
    
    def lunghezze_parole(self):
        return [len(parola) for parola in self.lista]
    
    def ricerca(self, parola):
        return parola in self.lista #mi ritorna true se parola è in lista
    
    def salva(self, nomeFile):
        with open(nomeFile, "w") as file:
            file.write(self.stringa)

    def frequeze_parole(self):
        frequeze = {}
        for parola in self.lista:
            if parola in frequeze:
                frequeze[parola] += 1 #se è presenteaumenta la frequenza
            else:
                frequeze[parola] = 1 #se non c'è crea la chiave
        return frequeze
    
def main():
    prova = "ciao come stai? ciao tutto bene"
    t = Test(prova)
    print(t.calcoloNcaratteri())
    print(t.lista_parole())
    print(t.lunghezze_parole())
    print(t.ricerca("mario"))
    print(t.ricerca("ciao"))
    t.salva("CorrezioneVerifica.txt")
    print(t.frequeze_parole())

if __name__ == "__main__":
    main()