# List comprehesion
# Lista con i primi 5 quadrati perfetti 1 4 9 

import random

quadrati = [i**2 for i in range (1,6)] #i**2 potenza di due con i compreso tra 1 e 6 escluso

numeri_interi = [i for i in range (1,11)]# scrive nella lista i primi 10 numeri interi

stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == "c"]
print(stringhe_c)

print(quadrati)


voti = [random.randint(2,10) for _ in range (0, 10)] #randint include gli estremi al posto di mettere una variabile che non si usa per far ciclare il for si mette l'underscore _
print(voti)

voti_insuff = [voto for voto in voti if voto < 6]
print(voti_insuff)