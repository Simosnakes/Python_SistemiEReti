class Quadrato():
    def __init__(self, lato): #costruttore __init__ nome di tutti i costruttori self parametro da passare sempre
        self.lato = lato

    def calcolaArea(self): 
        return self.lato**2

    def stampaLato(self):
        print(f"Il lato è: {self.lato}")

def main():
    q = Quadrato(4) #creo l'istanza ma chiamo il nome della classa la quale si riferisce al costruttore
    print(f"L'area del quadrato è: {q.calcolaArea()}")
    print(q.lato) #nessun attributo è privato posso leggerlo direttamente o modificarlo
    q.lato = 5
    print(f"L'area del quadrato è: {q.calcolaArea()}")
    q.stampaLato()

if __name__ == "__main__":
    main()