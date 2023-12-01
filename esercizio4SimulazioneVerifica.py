import turtle
def quadrato(cursore):
    for lati in range(0, 4):
        cursore.forward(10)
        cursore.left(90)
    cursore.forward(10)
def main():
    finestra = turtle.Screen()
    cursore = turtle.Turtle()
    for quadrati in range (0, 4):
        for riga in range (0, 4):
            quadrato(cursore)
        cursore.backward(40)
        cursore.left(90)
        cursore.forward(10)
        cursore.right(90)
    finestra.mainloop()
if __name__ == "__main__":
    main()