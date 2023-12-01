import ipaddress

def main():
    IP = input("Inserisci un indirizzo ip: ")
    subnet = input("Inserisci una subnet mask: ")
    ipSubnet = IP + subnet
    IPv4 = ipaddress.ip_address(IP)

    print(IPv4)

    if(IPv4.is_private):
        print(f"l' indirizzo {IPv4} è privato")
    else:
        print(f"l' indirizzo {IPv4} non è privato")
    
    if (IPv4.is_loopback):
        print(f"l' indirizzo {IPv4} è di loopback")
    else:
        print(f"l' indirizzo {IPv4} non è di loopback")

    ipRete = ipaddress.IPv4Network(ipSubnet, strict = False) #posso passare qualsiasi ip anche non di rete, lui calcola ugualmente quello di rete

    if str(ipRete) == ipSubnet:  
        print(f"L' ip è di rete perchè {ipSubnet} coincide con {ipRete}")
    else:
        print(f"Non è di rete perchè {ipSubnet} coincide con {ipRete}")
    
    hosts = list(ipRete.hosts())

    print(f"il primo ip utilizzabile è: {hosts[0]}")
    print(f"l'ultimo ip utilizzabile è: {hosts[-1]}")

    



if __name__ == "__main__":
    main()