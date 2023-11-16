import turtle


def nord(c):
    c.seth(90)
    c.forward(100)

def sud(c):
    c.seth(270)
    c.forward(100)

def est(c):
    c.seth(0)
    c.forward(100)

def ovest(c):
    c.seth(180)
    c.forward(100)



def main():
    dizionario = {"n":nord, "s":sud, "e":est, "o":ovest}

    finestra = turtle.Screen()#creazone finestra
    cursore = turtle.Turtle()#creazione cursore
    while True: 
        dir = input("Scrivi n per nord, s per sud, e per est, o per ovest (exit per uscire): ")

        if dir in dizionario:
            
            dizionario[dir](cursore)

        elif dir == "exit":
            break
        else:
            print("Errore")
            break
    
    finestra.mainloop()#mantiene la finestra aperta

if __name__ == "__main__":
    main()