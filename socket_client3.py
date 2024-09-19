import socket
from threading import Thread

SERVER_ADDRESS = ("192.168.1.117", 43209)
BUFFER_SIZE = 4096
MY_ADDRESS = ("0.0.0.0", 43210)
NICKNAME = "Arrigoni"

class Receiver(Thread):
    def __init__(self, socket):
        super().__init__()
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
    s.bind(MY_ADDRESS)
    ready= True
    receiver = Receiver(s)
    receiver.start()
    while True:
        message = input("-> ")
        dest = input("Inserisci il nickname del destinatario: ")
        packet = f"{message}|{NICKNAME}|{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS)

if __name__ == "__main__":
    main()