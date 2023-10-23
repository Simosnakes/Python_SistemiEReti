#SLICING
s = "ciao come stai?" #0 1 2 3 oppure al contrario -4 -3 -2 -1 l'ultimo carattere ha indice -1
print(f"Il primo carattere è: {s[0]}")
print(f"L' ultimo carattere è: {s[-1]}")
print(f"Il penultimo carattere è: {s[-2]}")
# C style più complicato DA NON USARE
#print(f"L' ultimo carattere è: {s[len(s)-1]}")

print(s[3:7]) #dal carattere 3 incluso al carattere 7 escluso
print(f"stampa la stringa tranne il primo e ultimo carattere: {s[1:-1]}") #stampa la stringa tranne il primo e ultimo carattere
print(f"non stampa solo l'ultimo carattere: {s[1:]}")#non stampa solo l'ultimo carattere
print(f"non stampa solo il primo carattere: {s[:-1]}")#non stampa solo l'ultimo carattere
print(s[::-1]) #stampa al contrario ?iats emoc oaic