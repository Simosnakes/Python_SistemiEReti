import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stringa = input("-> ")
    binary_string = stringa.encode()
    s.sendto(binary_string, SERVER_ADDRESS)