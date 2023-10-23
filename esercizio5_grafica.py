#chiede all'utente il comando da dare F, R o L i comandi sono salvati in una lista

import turtle

def main():
    list = []
    comandiPossibili = ['F', 'R', 'L']
    num = 'F'

    while num in comandiPossibili:
        num = input("Scrivi F per andare avati R per girare a destra e L per girare a sinstra: (-1 per interrompere): ")
        if num in comandiPossibili:
            list.append(num)#append serve ad aggiungere un numero alla lista


    finestra = turtle.Screen()#creazone finestra
    alice = turtle.Turtle()#creazione cursore

    for elemento in list:
        if elemento == 'F' :
            turtle.forward(100)
        elif elemento == 'R':
            turtle.right(90)
        else:
            turtle.left(90)

    finestra.mainloop()#mantiene la finestra aperta


if __name__ == "__main__":
    main()