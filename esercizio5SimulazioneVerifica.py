def main():
    ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    #file = open("mask.txt", "w")
    with open("mask.txt", "w") as file:         #crea l'oggetto e tiene aperto il file per tutto il codice contenuto nel with
        subnets = [ip [-3:] for ip in ip_address]
        file.write(f"{subnets}\n")
    #file.close()

if __name__ == "__main__":
    main()