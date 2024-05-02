#data una lista di valori creare un funzione che passata una lista crea un albero bilanciato

class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def inserisci(self, valore):
        if self.valore is not None: #se nel nodo c'è un valore
            #capire se inserire il valore nel figlio sinistro o destro
            if valore > self.valore:
                if self.destro is None:
                    self.destro = Node(valore)
                else:
                    self.destro.inserisci(valore)
            else:
                if self.sinistro is None:
                    self.sinistro = Node(valore)
                else:
                    self.sinistro.inserisci(valore)
        else:
            self.valore = valore
    
    def stampa(self):
        if self.valore is None:
            print("Nessun elemento\n")
        else:
            if self.sinistro is not None:
                self.sinistro.stampa()
            print(self.valore)          #se il print viene messo in mezzo stampa in ordine crescente se messo in fondo stampa in ordine decrescente
            if self.destro is not None:
                self.destro.stampa()
    
    def cerca(self, valore):
        if self.valore == valore:
            return True
        elif self.destro is not None and self.valore < valore:
            return self.destro.cerca(valore)
        elif self.sinistro is not None and self.valore > valore:
            return self.sinistro.cerca(valore)
        else:
            return False

def albero_bilanciato(lista):
    lista.sort()

    lung = len(lista)
    meta = lung // 2
    n = Node(lista[meta])
    
    if lung > 1:
        albero_bilanciato(lista[0:meta])
    else:
        n.inserisci(lista)
    
    n.stampa()
    


def main():
    lista = [5, 6, 2, 20, 28, 16]
    albero_bilanciato(lista)

    
    

if __name__ == "__main__":
    main()