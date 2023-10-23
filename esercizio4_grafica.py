import turtle

def main():
    x = int (input("Inserisci il numero di punte"))

    finestra = turtle.Screen()#creazone finestra
    alice = turtle.Turtle()#creazione cursore

    alice.color('red')

    alice.fillcolor('yellow')
    alice.begin_fill()

    angolo = 180 / x

    for k in range (0, x):
        alice.forward(100)
        alice.left(180 - angolo) 

    alice.fillcolor('red')
    alice.end_fill()

    finestra.mainloop()#mantiene la finestra aperta

if __name__ == "__main__":
    main()