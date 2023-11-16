def somma(a,b):
    return a+b

def prodotto(a,b):
    return a*b

def sottrazione(a,b):
    if b<a:
        ris = a-b
    else:
        ris = b-a
    
    return ris

def divisione(a,b):
    return a/b

def main():
    dizionario = {"+":somma, "*":prodotto, "-":sottrazione, "/":divisione}
    oper = input("Scrivi + per la somma, * per il prodotto, - per la sottrazione, / per la divisione: ")
    a = float(input("Srivi il primo numero: "))
    b = float(input("Scrivi il secondo numero: "))
    
    print(dizionario[oper](a, b)) #dizionario di oper è una funzione perciò gli passo i parametri per l'operazione da fare
    #pass # serve arendere il codice corretto

if __name__ == "__main__":
    main()