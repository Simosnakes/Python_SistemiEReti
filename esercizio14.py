def conversioneDec(ip_binario):
    gruppiDec = []
    for i in range(0, 32, 8): # l'ultimo 8 serve per ciclare a blocchi di 8 e non 1
        ottetto = ip_binario[i:i+8]
        gruppiDec.append(str(int(ottetto, 2)))
    return ".".join(gruppiDec)

def main():
    ip_address = input("Inserisci l'ip di un dispositivo: ")
    cidr = int(input("Inserisci la cidr: "))
    subnet = "1" * cidr +"0" * (32 -cidr)
    wild_card = "0" * cidr + "1" * (32 - cidr)

    subnetDec = '.'.join(str(int(subnet[i:i+8], 2)) for i in range (0, 32, 8))
    wild_cardDec = '.'.join(str(int(wild_card[i:i+8], 2)) for i in range (0, 32, 8))

    print(f"subnetMask {subnetDec}")
    print(f"Wild_card {wild_cardDec}")

    ip_binary_groups = [format(int(x), '08b') for x in ip_address.split('.')]
    ip_binary = ''.join(ip_binary_groups)
    print(ip_binary_groups)
    print(ip_binary)

    ip_network = ip_binary[0:cidr] + "0" * (32 - cidr)
    ip_broadcast = ip_binary[0:cidr] + "1" * (32 - cidr)

    print(f"Ip di rete: {conversioneDec(ip_network)}")
    print(f"Ip di broadcast {conversioneDec(ip_broadcast)}")





if __name__ == "__main__":
    main()