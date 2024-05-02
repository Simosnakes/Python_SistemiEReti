import socket

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096 #byte

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(MY_ADDRESS)
while True:
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    string = data.decode()
    print(f"Ricevuto {string} da {sender_address}")
    s.sendto(data, sender_address)
    if string == "EXIT":
        break