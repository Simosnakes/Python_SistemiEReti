#chiedere un numero dispari all'utente nel terminare stanpo un diamante fatto di asterischi

def main():
    num = 0
    while num % 2 == 0:
        num = int(input("Inserisci un numero dispari: "))
    
    meta = False
    nspazi = num - 1
    nasterischi = 1
    for riga in range(0, num):
        s = " " * nspazi + "*" * nasterischi
        
        if nasterischi < num and meta == False:
            nasterischi +=2
            nspazi -= 1
        elif nasterischi > 1:
            meta = True
            nasterischi -=2
            nspazi += 1
        print(s)

if __name__ == "__main__":
    main()