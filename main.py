import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Pet")

char = pygame.image.load('yoda2.png')
# bg = pygame.image.load('')
barra1 = pygame.image.load('barra1.png')
barra2 = pygame.image.load('barra1.png')
fome = pygame.image.load('fome.png')
energia = pygame.image.load('energia.png')
comida = pygame.image.load('comida.png')
dormir = pygame.image.load('dormir.png')
comendo = pygame.image.load('yoda-comendo.png')

fome_width = 0
energia_width = 0

def janela():
    # win.blit(bg, (0,0))
    # win.blits(bg, (1))
    win.fill((255, 255, 255))
    win.blit(char, (35, 20))

    win.blit(barra1, (90, 10))
    win.blit(fome, (115, 30))
    win.blit(barra2, (300, 10))
    win.blit(energia, (320, 30))
    win.blit(comida, (10, 470))
    win.blit(dormir, (110, 458))

    pygame.draw.rect(win, (51, 204, 51), (93, 25, fome_width, 15))
    pygame.draw.rect(win, (51, 204, 51), (303, 25, energia_width, 15))

    pygame.display.update()


run = True
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if fome_width <= 110:
            fome_width = fome_width + 5
        janela()
        print('Alimentado')

    if keys[pygame.K_w]:
        if energia_width <= 110:
            energia_width = energia_width + 5
        janela()
        print('Descansado')

    janela()
pygame.quit()
