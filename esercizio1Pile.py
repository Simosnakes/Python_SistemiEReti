def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x

def main():
    parentesi_aperte = ["{", "[", "("]
    parentesi_chiuse = ["}", "]", ")"]
    dizionario = {"{":"}", "[":"]", "(":")"}
    stringa = "{[()]}"
    pila = []
    cont = 0
    pos = None
    errore = False
    for poscarattere, carattere in enumerate(stringa):
        if carattere in parentesi_aperte:
            push(pila, carattere)
            cont += 1
        
        if carattere in parentesi_chiuse:
            if cont > 0:
                parentesi = pop(pila)
                if parentesi != None:
                    if dizionario[parentesi] !=carattere:
                        errore = True
                        pos = poscarattere
                    else:
                        cont -= 1
                else:
                    errore = True
                    pos = poscarattere
            else:
                errore = True
                pos = poscarattere

    if errore or cont > 0:
        print(f"Errore in posizione: {cont}")
    else:
        print("Corretto!")


if __name__ == "__main__":
    main()