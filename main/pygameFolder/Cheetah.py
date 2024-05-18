import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
cheetahImg = pygame.image.load("pygame/cheetah.png")
cheetahImg = cheetahImg.convert_alpha()
pygame.display.set_icon(cheetahImg)
cheetahImg = pygame.transform.scale(cheetahImg, (75, 50))
play = True
screen.fill((0, 150, 255))
pygame.display.set_caption("Cheetah")
mixer = pygame.mixer
jump = mixer.Sound("pygame/synth.wav")
jump.set_volume(0.05)
class Sprite:
    size = (50, 50)
    platformImg = pygame.image.load("pygame/grass.png")
    platformImg = platformImg.convert_alpha()
    platformImg = pygame.transform.scale(platformImg, size)
    
    def show(self, x, y):
        screen.blit(self.platformImg, (x, y)) 
    

def cheetah(x, y):
    
    global cheetahImg
    screen.blit(cheetahImg, (x, y))
       
x = -249
y = 300
gravity = 0.5
grassRect = pygame.Rect((0, 300), (800, 300))
jumped = False

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    screen.fill((0, 200, 255))
    screen.fill((0, 255, 150), grassRect)
    cheetah(x, y)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:   
        x -= 0.5
            
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
         x += 0.5
            
    if keys[pygame.K_UP] or keys[pygame.K_SPACE] and jumped == False:
        y -= 1
        jump.play(0, 500, 100)
        jumped = True
    else:
        jumped = False
            
    if keys[pygame.K_g]:
        gravity = 0.1
    else:
        gravity = 0.5

    if jumped:
        y += gravity
    
    if x >= 750:
        x = -249
    elif x <= -250:
        x = 749
    #platforms
    #platform(50, 150)
        
    pygame.display.update()