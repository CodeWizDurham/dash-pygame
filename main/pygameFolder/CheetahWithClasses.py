#setup
import pygame

from pygame.locals import (
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cheetah")

cheetahImg = pygame.image.load("pygame/cheetah.png")
pygame.display.set_icon(cheetahImg)

mixer = pygame.mixer
jump = mixer.Sound("pygame/synth.wav")
jump.set_volume(0.05)

gravity = 0.5
grassRect = pygame.Rect((0, 300), (800, 300))
play = True

transparent = (0, 0, 0, 0)
clock = pygame.time.Clock()

#player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Image = pygame.image.load("pygame/cheetah.png").convert_alpha()
        self.Image = pygame.transform.scale(self.Image, (75, 50))
        self.rect = self.Image.get_rect()
        self.x = 300
        self.y = 250
        
    def moveLeft(self):
        self.x -= 1
        
    def moveRight(self):
        self.x += 1
        
    def jump(self):
        self.y -= 15
        
    def spawn(self, x, y):
        screen.blit(self.Image, (x, y))

#platforms
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame/grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def showPlatform(self, x, y):
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, (self.rect.x, self.rect.y))

platform1 = platform()
platform2 = platform()
platform3 = platform()
platform4 = platform()
platform5 = platform()
platform6 = platform()
platform7 = platform()
platform8 = platform()
platform9 = platform()

platformGroup = pygame.sprite.Group()
pygame.sprite.Group.add(platformGroup, platform1)
pygame.sprite.Group.add(platformGroup, platform2)
pygame.sprite.Group.add(platformGroup, platform3)
pygame.sprite.Group.add(platformGroup, platform4)
pygame.sprite.Group.add(platformGroup, platform5)
pygame.sprite.Group.add(platformGroup, platform6)
pygame.sprite.Group.add(platformGroup, platform7)
pygame.sprite.Group.add(platformGroup, platform8)
pygame.sprite.Group.add(platformGroup, platform9)

cheetah = Player()
cheetahGroup = pygame.sprite.Group(cheetah)
print(cheetahGroup)
def checkPlatform(platformInput):
    global gravity
    if cheetah.x == platformInput.rect.x and cheetah.y == platformInput.rect.y:
        gravity = 0

#main loop
while play:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                play = False
                
            if event.key == K_UP or event.key == pygame.K_SPACE:
                cheetah.jump()
                jump.play(0, 500, 100)
        if event.type == QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[pygame.K_a]:   
        cheetah.moveLeft()
            
    if keys[K_RIGHT] or keys[pygame.K_d]:
        cheetah.moveRight()
    
    screen.fill((0, 200, 255))
    screen.fill((0, 255, 150), grassRect)
    
    #more platforms
    platform1.showPlatform(50, 200)
    platform2.showPlatform(100, 150)
    platform3.showPlatform(150, 100)
    platform4.showPlatform(200, 50)
    platform5.showPlatform(300, 50) 
    platform6.showPlatform(400, 50)
    platform7.showPlatform(500, 100)
    platform8.showPlatform(565, 150)
    platform9.showPlatform(610, 100)
        
    cheetah.spawn(cheetah.x, cheetah.y)
    
    if cheetah.x >= 750:
        cheetah.x = -49
    elif cheetah.x <= -50:
        cheetah.x = 749
         
    if cheetah.y <= -50:
        cheetah.y = 250
        
    if cheetah.y <= 249:
        cheetah.y += gravity
    
    gravity = 1.5
    checkPlatform(platform1)
    checkPlatform(platform2)
    checkPlatform(platform3)
    checkPlatform(platform4)
    checkPlatform(platform5)
    checkPlatform(platform6)
    checkPlatform(platform7)
    checkPlatform(platform8)
    checkPlatform(platform9)
    check = pygame.sprite.spritecollideany(cheetah, platformGroup)
    if check: 
        print("coliding")
    clock.tick(60)
    pygame.display.update()