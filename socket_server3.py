import socket
from threading import Thread

MY_ADDRESS = ("0.0.0.0", 43211)
BUFFER_SIZE = 4096 #byte

class Ricevere(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.sender_address = None
        self.running = True
    
    def run(self):
        while self.running:
            data, self.sender_address = self.s.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"Ricevuto '{string}' da {self.sender_address}")

            ip_client, string = string.split("|")
            string = string.encode()
            self.s.sendto(string, (ip_client, 9000))

    def kill(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)

    threadRicevere = Ricevere(s)
    threadRicevere.start()

    with open("rubrica.csv", "r") as file:

        csv.reader(file, delimiter = ", ")

    while True:
        '''if threadRicevere.sender_address != None:
            string = input("-> ")
            binary_string = string.encode()
            s.sendto(binary_string, threadRicevere.sender_address)'''

if __name__ == "__main__":
    main()

