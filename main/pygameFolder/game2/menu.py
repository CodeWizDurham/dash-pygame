import pygame
import time

pygame.init()

#define screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cheetah in Backrooms 2 Menu")
cheetah = pygame.image.load("pygameFolder/cheetah.png")
cheetahpos = 0
forward = True

run = True

while run:
    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                import main
                
    screen.fill((0, 150, 255))
    screen.blit(cheetah, (cheetahpos, 135))
    if cheetahpos >= 700:
        forward = False
    elif cheetahpos <= -400:
        forward = True
        
    if forward:
        cheetahpos += 5
    else:
        cheetahpos -= 5
    f = pygame.font.SysFont("Comic Sans", 30, True, False)
    f2 = pygame.font.SysFont("Comic Sans", 75, True, False)
    text = f.render("Cheetah in Backrooms 2: the Electric Boogaloo", 1, (255, 255, 255))
    play = f2.render("Press space to play.", 1, (255, 255, 255))
    screen.blit(text, (50, 50))
    screen.blit(play, (50, 450))
    
    pygame.display.update()

pygame.quit()