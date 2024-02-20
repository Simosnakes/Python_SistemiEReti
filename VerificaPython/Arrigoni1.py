def main():
    for numero in range(0, 999):
        numero_string = str(numero)

        if len(numero_string) == 1:
            print(f"il numero {numero_string} è palindromo")
        else:
            if numero_string[0] == numero_string[len(numero_string) - 1]:
                print(f"il numero {numero_string} è palindromo")

if __name__ == "__main__":
    main()
            
