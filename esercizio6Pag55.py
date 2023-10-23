x = input("Inserisci una parola: ")

lung = len(x)
for elemento in range (lung):
    if elemento % 2 != 0:
        print(x[elemento], end = ' ')


print(x[1::2])