lettere = "abcdefghilmnopqrstuvz ?"
lettere2numeri = {}
numeri2lettere = {}
N  = len(lettere)

for posizione, lettera in enumerate(lettere):
    lettere2numeri[lettera] = posizione
    numeri2lettere[posizione] = lettera
#print(lettere2numeri)
#print(numeri2lettere)

testo_chiaro = "ciao come stai?"
chiave = "itisdelpozzo dhf hdfgteg efec dbebdfa dethfstbsdb rggn,ui d"

testo_criptato = ""
for lettera_testo, lettera in zip(testo_chiaro, chiave):
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera]) % N
    testo_criptato += numeri2lettere[numero]
print(f"il testo '{testo_chiaro}' diventa '{testo_criptato}'.")

testo_de_criptato = ""
for lettera_testo, lettera in zip(testo_criptato, chiave):
    numero = (lettere2numeri[lettera_testo] - lettere2numeri[lettera]) % N
    testo_de_criptato += numeri2lettere[numero]
print(f"Il testo da così '{testo_criptato}' diventa '{testo_de_criptato}'")