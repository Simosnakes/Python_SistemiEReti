dizionario = {"a":"albero", "b":"brutto", "c":"casa"}

print(dizionario["b"])
dizionario["d"] = "dado" #aggiunge un alemento al dizionario metto nelle quadre la chiave
dizionario["a"] = "alto" #sostituisce la parola alla chiave scritta tra le quadre
print(dizionario)

for chiave in dizionario:
    print(f"La chiave {chiave} ha valore: {dizionario[chiave]}")
if "a" in dizionario:
    print("a è presente nel dizionario")
