a = float(input("inserisci un numero"))
b = float(input("inserisci un numero"))

    if a < b:
        a, b = b, a
    
print(f"{a}, {b}")