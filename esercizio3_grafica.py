#creare 11 poligoni regolari colorati
import turtle

def disegnaPoligono(t, lati, lato):
    angolo = 360/lati
    for z in range (0, lati):
        t.forward(lato)
        t.left(angolo)

def posizionaTurtle(base, x):
    alice.penup()
    if (x == 2):
        alice.sety(alice.ycor() - 150)
        alice.setx(-base)
        x = 0
    else:
        alice.forward(200)
        x = x + 1
    alice.pendown()
    return x

def main():

    base = 250
    lung = 25
    x = 0
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape('turtle')
    alice.color('red')#colore della linea
    alice.speed('slow')#velocità della turtle
    alice.penup()#turtle smette di scrivere
    alice.setposition(-base, 200)#si muove in alto a sinistra
    alice.pendown()#turtle ricomincia a scrivere
    for i in range(3, 12):
        disegnaPoligono(alice, i, lung)
        x = posizionaTurtle(base, x)
    #alice.hideturtle()
    finestra.mainloop()

if __name__ == '__main__':
    main()