class CodiceABarre():
    def __init__(self):
        self.spess = 4
        self.lung = 100
        self.numbarre = 64
    
    def stampaBarra(self, stringa):
        codiceAscii = ""

        for carattere in stringa:
            dec_bin(ord(carattere))
        

def main():
    lung = False
    codice = CodiceABarre()

    while(lung == False):
        stringa = input("Inserisci una stringa alfanumerica (di 8 caratteri): ")
        if len(stringa) == 8:
            lung = True
    
    codice.stampaBarra(stringa)

if __name__ == "__main__":
    main()