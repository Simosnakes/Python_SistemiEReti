def main():
    ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]

    file = open("mask.txt", "w")

    subnets = [ip [-3:] for ip in ip_address]

    file.write(f"{subnets}")
    file.close()

if __name__ == "__main__":
    main()