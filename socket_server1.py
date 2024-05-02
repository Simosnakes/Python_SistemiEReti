import socket

#identifica il processo server, indirizzo ip macchina e porta
MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

#creo il socket come IPV4 e UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(MY_ADDRESS)
s.recvfrom(BUFFER_SIZE)

while True:
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    stringa = data.decode()
    print(f"Ricevuto {stringa} da {sender_address}")
    if stringa == "EXIT":
        break