lista = "ciao a tutti"
vocali = "aeiou"

listSenzaVocali = [lettera for lettera in lista if(lettera not in vocali)]

print("".join(listSenzaVocali))