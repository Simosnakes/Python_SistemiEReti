import pygame, sys

pygame.init()

YELLOW=(255, 255, 0)

screen=pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

ball=pygame.image.load('cannone.png')
x=0
y=0
d=1

FPS=20
cl=pygame.time.Clock()

while True: 
    screen.fill(YELLOW)
    screen.blit(ball, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if d==1:  #va a destra
        x += 10
        if x==300:
            d=2 #imposta la direzione per andare giù
    elif d==2: #va giù
        y+=10
        if y==300:
            d=3 #imposta la direzione per andare a sinistra
    elif d==3: #va a sinistra
        x-=10
        if x==0:
            d=4 #imposta la direzione per andare sotto
    elif d==4: #va su
        y -= 10
        if y==0:
            d=1

    pygame.display.update()
    cl.tick(FPS)