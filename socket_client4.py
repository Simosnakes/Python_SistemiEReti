import socket
SERVER_ADDRESS = ("192.168.1.128", 9090)
BUFFER_SIZE = 4096
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(SERVER_ADDRESS)
    while True:
        s.sendall(f"Messaggio dal client".encode())
        message = s.recv(BUFFER_SIZE)
        print(f"Ricevuto <{message.decode()}> dal server")

    s.close()

if __name__ == "__main__":
    main()