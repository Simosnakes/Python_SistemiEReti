import pygame
import sys
import random

class Giocatore:
    def __init__(self, x, y, raggio, colore, larghezza, altezza):
        self.x = x
        self.y = y
        self.raggio = raggio
        self.colore = colore
        self.proiettili = []
        self.ritardo_sparo = 0.3  #Tempo di ritardo tra gli spari in secondi
        self.ultimo_tempo_sparo = pygame.time.get_ticks()
        self.larghezza = larghezza
        self.altezza = altezza

        self.x_cann = x
        self.y_cann = y

    def disegna(self, schermo):
        cannone = pygame.image.load('cannone.png')
        schermo.blit(cannone, (0,0))

    def muovi(self, direzione):
        self.x += direzione * 3
        #controllo che il giocatore rimanga all'interno dei limiti della finestra
        self.x = max(self.raggio, min(self.x, self.larghezza - self.raggio))

    def spara(self):
        tempo_attuale = pygame.time.get_ticks()
        if tempo_attuale - self.ultimo_tempo_sparo > self.ritardo_sparo * 1000:#Converto il ritardo in millisecondi
            raggio_proiettile = 10  #dimensione dei proiettili
            proiettile = Proiettile(self.x, self.y - self.raggio, raggio_proiettile, (100, 0, 180), -5, self.larghezza, self.altezza)#crea proiettile
            self.proiettili.append(proiettile)#aggiungi proiettile
            self.ultimo_tempo_sparo = tempo_attuale

class Palla:
    def __init__(self, x, y, raggio, colore, velocita, larghezza, altezza):
        self.x = x
        self.y = y
        self.raggio = raggio
        self.colore = colore
        self.velocita = velocita
        self.larghezza = larghezza
        self.altezza = altezza
    
    def disegna(self, schermo):
        pygame.draw.circle(schermo, self.colore, (int(self.x), int(self.y)), self.raggio)

class Proiettile:
    def __init__(self, x, y, raggio, colore, velocita, larghezza, altezza):
        self.x = x
        self.y = y
        self.raggio = raggio
        self.colore = colore
        self.velocita = velocita
        self.larghezza = larghezza
        self.altezza = altezza
    
    def disegna(self, schermo):
        pygame.draw.circle(schermo, self.colore, (int(self.x), int(self.y)), self.raggio)

class Terreno:
    def __init__(self, colore, altezza, larghezza):
        self.colore = colore
        self.altezza = altezza
        self.larghezza = larghezza

    #disegna il terreno
    def disegna(self, schermo):
        pygame.draw.rect(schermo, self.colore, (0, self.altezza, self.larghezza, self.altezza))

class Sfondo:
    def __init__(self, colore, larghezza, altezza):
        self.colore = colore
        self.larghezza = larghezza
        self.altezza = altezza

    #disegna lo sfondo
    def disegna(self, schermo):
        schermo.fill(self.colore)

def crea_palla(colore, larghezza, altezza):
    raggio_palla = 20
    colore_palla = colore
    #creo le cordinate x e y in modo randomico
    x_palla = random.randint(raggio_palla, larghezza - raggio_palla)
    y_palla = random.randint(0, altezza // 2)
    #creo la velocità della palla in modo randomico
    velocita_palla = random.uniform(1, 3)
    #restituisco la palla creata
    return Palla(x_palla, y_palla, raggio_palla, colore_palla, velocita_palla, larghezza, altezza)

def visualizza_game_over(schermo, font, punteggio, larghezza, altezza):
    dimensione_font = 50
    #creo il testo e il colore di fine gioco
    testo_game_over = font.render("Game Over", True, (0, 0, 0))
    testo_punteggio = font.render(f"Punteggio: {punteggio}", True, (0, 0, 0))

    #stampo le scritte
    schermo.blit(testo_game_over, (larghezza // 2 - testo_game_over.get_width() // 2, altezza // 2 - dimensione_font))
    schermo.blit(testo_punteggio, (larghezza // 2 - testo_punteggio.get_width() // 2, altezza // 2 + 20))

    pygame.display.flip()
    pygame.time.delay(3000)  #Pausa di 3 secondi prima di uscire dal gioco

def disegnaPunteggio(schermo, punteggio, font):
    testo_punteggio = font.render(f"Punteggio: {punteggio}", True, (0, 0, 0))
    schermo.blit(testo_punteggio, (10, 10))

def visualizzaSchermoIniziale(schermo, font, altezza, larghezza, miglior_punteggio):
    dimensione_font = 70
    testo = font.render("Premi S per iniziare", True, (255,255,255))
    testo_punt = font.render(f"Miglior punteggio: {miglior_punteggio}", True, (255,255,255))
    schermo.blit(testo, (testo.get_width() // 2 + dimensione_font, larghezza // 2 - dimensione_font))
    schermo.blit(testo_punt, (testo.get_width() // 2 + dimensione_font, altezza // 2 - dimensione_font))
    pygame.display.flip()
    #pygame.time.delay(3000)

def main():
    pygame.init()
    #Impostazioni del gioco
    larghezza, altezza = 600, 700
    fps = 120
    RAGGIO_PALLA = 20
    VELOCITA_PALLA = 5
    AZZURRO = (135, 206, 250)
    DIMENSIONE_FONT = 36
    miglior_punteggio = 0

    font = pygame.font.Font(None, 36)

    #Creazione della finestra di gioco
    schermo = pygame.display.set_mode((larghezza, altezza))
    pygame.display.set_caption("Ball Blast")

    #Creazione del terreno
    terreno = Terreno((0, 128, 0), altezza - 50, larghezza)

    # Creazione dello sfondo
    sfondo = Sfondo(AZZURRO, larghezza, altezza)

    #Ciclo di gioco
    clock = pygame.time.Clock()

    running = False
    inizio = True
    while inizio:
        schermo.fill((0,0,0))
        #Punteggio iniziale
        punteggio = 0
        #Creazione del giocatore
        cannone = Giocatore(larghezza // 2, altezza - 50, 15, (0, 0, 255), larghezza, altezza)

        #Creazione delle palle
        palle = [crea_palla((255, 0, 0), larghezza, altezza)]  # Palla rossa e palla blu iniziali

        with open("miglior_punteggio.txt", "r") as file:
            contenuto = file.read()
            if len(contenuto) > 0:
                miglior_punteggio = int(contenuto)

        visualizzaSchermoIniziale(schermo, font, altezza, larghezza, miglior_punteggio)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_s:
                    running = True
                    inizio = False
            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                inizio = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                    visualizza_game_over(schermo, font, punteggio, larghezza, altezza)
                    running = False

            #controlla i tasti premuti
            tasti = pygame.key.get_pressed()
            giocatore.muovi(tasti[pygame.K_RIGHT] - tasti[pygame.K_LEFT])

            #gestisce gli spari del giocatore
            if tasti[pygame.K_SPACE]:
                giocatore.spara()

            #imposta velocità palle
            for palla in palle:
                if(punteggio < 30):
                    palla.y += palla.velocita
                elif punteggio >= 30 and punteggio < 50:
                    palla.y += palla.velocita * 1.25
                elif punteggio >= 50 and punteggio < 60:
                    palla.y += palla.velocita * 1.50
                elif punteggio >= 60 and punteggio < 70:
                    palla.y += palla.velocita * 1.75
                elif punteggio >= 70:
                    palla.y += palla.velocita * 2

                #Controlla la collisione con il giocatore
                distanza = ((giocatore.x - palla.x)**2 + (giocatore.y - palla.y)**2)**0.5

            #Aggiorna la posizione delle palle
            for palla in palle:
                palla.y += palla.velocita

                #Controlla la collisione con il giocatore
                distanza = ((giocatore.x - palla.x)**2 + (giocatore.y - palla.y)**2)**0.5
                if distanza < giocatore.raggio + palla.raggio:
                    if palla.colore == (255, 0, 0):  #palla rossa
                        visualizza_game_over(schermo, font, punteggio, larghezza, altezza)
                        #leggo dal file il miglior punteggio
                        with open("miglior_punteggio.txt", "r") as file:
                            contenuto = file.read()
                            if len(contenuto) > 0:
                                miglior_punteggio_letto = int(contenuto)
                            else:
                                miglior_punteggio_letto = 0

                        #controllo che il punteggio sia superiore al migliore
                        if(punteggio > miglior_punteggio_letto):
                            miglior_punteggio = punteggio
                            miglior_punteggio_str = str(miglior_punteggio)
                            #salvo il nuovo miglior punteggio
                            with open("miglior_punteggio.txt", "w") as file:
                                file.write(miglior_punteggio_str)

                        running = False
                        inizio = True
                    else:
                        palle.remove(palla)

            #Aggiorna la posizione dei proiettili del giocatore
            for proiettile in giocatore.proiettili:
                proiettile.y += proiettile.velocita

                #Controlla la collisione dei proiettili con le palle
                for palla in palle:
                    distanza = ((proiettile.x - palla.x)**2 + (proiettile.y - palla.y)**2)**0.5
                    if distanza < proiettile.raggio + palla.raggio:
                        giocatore.proiettili.remove(proiettile)
                        palle.remove(palla)
                        if palla.colore == (255, 0, 0): #Palla rossa
                            punteggio += 1  #Incrementa il punteggio quando una palla rossa viene colpita da un proiettile

            #Crea nuove palle rosse casualmente
            if random.random() < 0.03:
                palle.append(crea_palla((255, 0, 0), larghezza, altezza))

            #Disegna lo sfondo
            sfondo.disegna(schermo)

            #Disegna il terreno
            terreno.disegna(schermo)

            #Disegna il giocatore
            giocatore.disegna(schermo)

            #Disegna le palle
            for palla in palle:
                palla.disegna(schermo)

            #Disegna i proiettili del giocatore
            for proiettile in giocatore.proiettili:
                proiettile.disegna(schermo)

            #Disegna il punteggio corrente
            disegnaPunteggio(schermo, punteggio, font)

            #Aggiorna lo schermo
            pygame.display.flip()

            #Imposta il frame rate
            clock.tick(fps)

    #Uscita dal gioco
    pygame.quit()

if __name__ == "__main__":
    main()
