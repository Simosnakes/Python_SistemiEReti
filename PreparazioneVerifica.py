import random
import turtle
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    cursore = turtle.Turtle()
    finestra = turtle.Screen()

    percorso = {0: Punto(0,0)}

    for tempo in range(1, 60):
        #simulare movimenti casuali
        mov = random.randint(0, 3)
        if mov == 0:
            percorso[tempo] = Punto(percorso[tempo - 1].x, percorso[tempo-1].y -10)
        elif mov == 1:
            percorso[tempo] = Punto(percorso[tempo - 1].x, percorso[tempo-1].y +10)
        elif mov == 2:
            percorso[tempo] = Punto(percorso[tempo - 1].x -10, percorso[tempo-1].y)
        elif mov == 3:
            percorso[tempo] = Punto(percorso[tempo - 1].x +10, percorso[tempo-1].y)
        #disegnare percorso con turtle
        cursore.goto(percorso[tempo].x, percorso[tempo].y)
        
        #BONUS controllo passaggio in un punto già visitato
        for tempo_p in range(0, tempo):
            if percorso[tempo_p]. x == percorso[tempo].x and percorso[tempo_p].y == percorso[tempo].y:
                print(percorso[tempo_p]. x, percorso[tempo_p].y)
        
        if percorso[tempo].x == percorso[0].x and percorso[tempo].y == percorso[0].y:
            print("E' tornato al punto di partenza")
            

    #scrittura su file del percorso
    #COLONNE: miuto, x, y
    with open("percorso.csv", "w") as file:
        file.write("minuto, posx, posy \n")
        #ciclo su dizionario percorso
        for minuto in percorso:
            posx = percorso[minuto].x
            posy = percorso[minuto].y
            file.write(f"{minuto}, {posx}, {posy} \n")

    finestra.mainloop()

        

if __name__ == "__main__":
    main()