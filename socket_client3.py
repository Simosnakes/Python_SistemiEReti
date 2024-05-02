import socket
from threading import Thread

SERVER_ADDRESS = ("192.168.1.132", 9000)
BUFFER_SIZE = 4096
NICKNAME = "Arrigoni"

class Receiver(Thread):
    def __init__(self, socket):
        super()._init_()
        self.socket = socket
        self.running = True
    def run(self):
        while self.running:
            data, sender_address = self.socket.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"{sender_address}: {string}")
    def kill(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ready= True
    receiver = Receiver(s)
    while True:
        message = input("-> ")
        dest = input("Inserisci il nickname del destinatario: ")
        packet = f"{message}|{NICKNAME}|{dest}"
        s.sendto(string.encode(), SERVER_ADDRESS)
        if ready:
            receiver.start()
            ready= False

if __name__ == "_main_":
    main()