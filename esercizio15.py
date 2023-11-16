#dizionario è una collezione di coppie chiave valore
#il dizionario non ha indici si indiciza per chiave la chiave deve essere UNIVOCA
#la chiave deve essere di un solo tipo

dizionario = {"nome": "Mario", "cognome": "Rossi"}#contiene due elementi
print(dizionario["nome"])
dizionario["data nascita"] = "01/01/1900"#aggiunge un nuovo elemento
dizionario["età"] = 123#si può scrivere anche interi
dizionario["nome"] = "Luca"

print(dizionario)

#ciclo for su dizionario 1
for chiave in dizionario:
    print(f"Chiave: {chiave} - Valore: {dizionario[chiave]}")

rubrica = [38189192: "Mario Rossi", 3367195681:"Alice Bianchi", 345323325: "Luca Verdi"]