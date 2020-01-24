import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Pet")

char = pygame.image.load('yoda2.png')
bg = pygame.image.load('forest.png')
barra1 = pygame.image.load('barra1.png')
barra2 = pygame.image.load('barra1.png')
fome = pygame.image.load('fome.png')
energia = pygame.image.load('energia.png')

x = 100
y = 100
width = 50
height = 50
vel = 5

def janela():
    # win.blit(bg, (0,0))
    # win.blits(bg, (1))
    win.fill((255,255,255))
    win.blit(char, (35,20))

    win.blit(barra1, (90, 10))
    win.blit(fome, (115,30))
    win.blit(barra2, (300, 10))
    win.blit(energia, (320, 30))


    pygame.draw.rect(win, (51,204,51), (93,25 ,20, 15))

    pygame.display.update()


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]:

    janela()
pygame.quit()