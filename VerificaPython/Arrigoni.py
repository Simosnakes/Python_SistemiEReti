#fare una classe che rappresenti espressioni matematiche stringa composta da numeri parentesi tonde il simbolo + - * /
#il primo metodo deve verificare se l' espressione matematica è valida quando ha caratteri solo come quelli elencati primi
class Espressione():
    def __init__(self, espressione):
        self.espressione = espressione
        self.lista_car = ["+", "-", "*", "/", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.lista = ["+", "-", "*", "/"]
    
    def espressioneValida(self):
        valida = True
        for elemento in self.espressione:
            if elemento not in self.lista_car:
                valida = False
                break
        
        return valida
    
    def contaFrequenza(self):
        dizionario = {}
        
        for operazione in self.espressione:
            if operazione in self.lista and operazione not in dizionario:
                dizionario[operazione] = 0

        for elemento in self.espressione:
            if elemento in self.lista and elemento in dizionario:
                dizionario[(elemento)] += 1
        
        return dizionario
    
    def contaOperazioni(self):
        dizionario = self.contaFrequenza()
        num_tot_oper = 0
        for chiave in dizionario:
            num_tot_oper += dizionario[chiave]

        print(num_tot_oper)


def main():
    espressione = input("Inserisci un espressione matematica: ")
    esp = Espressione(espressione)

    if esp.espressioneValida():
        print("L'espressione è valida")
    else:
        print("L'espressione non è valida")
    
    print(esp.contaFrequenza())
    esp.contaOperazioni()



if __name__ == "__main__":
    main()