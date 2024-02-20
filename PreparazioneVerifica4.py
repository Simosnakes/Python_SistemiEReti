stringa = "123 45678 90"
lista = [numero for numero in stringa]
print(lista)

print(".".join(stringa))

lista_senza_spazi = stringa.split(" ")
stringa_senza_spazi = ""
for numero  in lista_senza_spazi:
    stringa_senza_spazi += numero
print(stringa_senza_spazi)
