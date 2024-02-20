import pygame, sys

pygame.init()

screen=pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

FPS=20
cl=pygame.time.Clock()

colore_cannone = "cannoneBluX5.0.png"

while True: 
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    cannone = pygame.image.load(colore_cannone)
    screen.blit(cannone, (50, 50))

    
    pygame.display.update()
    cl.tick(FPS)