import turtle

def main():
    x = int (input("Inserisci il numero di lati"))
    y = int(input("Inserisci la lunghezza del lato"))

    finestra = turtle.Screen()#creazone finestra
    alice = turtle.Turtle()#creazione cursore

    angolo = 360 / x
    alice.color('red')

    alice.fillcolor('yellow')
    alice.begin_fill()

    for k in range (0, x):
        alice.forward(y)
        alice.left(angolo)

    alice.fillcolor('red')
    alice.end_fill()

    finestra.mainloop()#mantiene la finestra aperta

if __name__ == "__main__":
    main()