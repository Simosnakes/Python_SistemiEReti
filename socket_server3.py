import socket
from threading import Thread
import csv

MY_ADDRESS = ("0.0.0.0", 43210) #myaddress funziona solo nel server
BUFFER_SIZE = 4096

class Receive(Thread):
    def __init__(self, s, rubrica):
        super().__init__()
        self.s = s
        self.rubrica = rubrica
        self.running = True
        self.sender_address= None

    def run(self):
        while self.running:
            data, self.sender_address = self.s.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"{self.sender_address}: {string}")
            string, mandante, destinatario = string.split("|")
            if string == "rubrica":
                self.s.sendto(str(self.rubrica).encode(), self.sender_address)
            else:
                string = f"{mandante}: {string}"
                string = string.encode()
                self.s.sendto(string, self.rubrica[destinatario])
  
    def kill(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    rubrica = {}
    with open('rubrica.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            rubrica[row[0]] = (row[1], int(row[2]))
    
    # Starting thread
    receiver = Receive(s, rubrica)
    receiver.start()

    while True:
        # Send message
        '''if receiver.sender_address != None:
            string = input("-> ")
            binary_string = string.encode()
            s.sendto(binary_string, receiver.sender_address)'''
        pass

if __name__ == "__main__":
    main()