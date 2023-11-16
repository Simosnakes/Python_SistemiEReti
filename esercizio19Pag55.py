import math

def mediaGeometrica(a, b):
    return math.sqrt(a*b)

def mediaAritmetica(a, b):
    return (a+b)/2

def main():
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))

    dizionari = {"mediaAritmetica": mediaAritmetica(num1, num2), "mediaGeometrica":mediaGeometrica(num1,num2)}
    print(dizionari)


if __name__ == "__main__":
    main()