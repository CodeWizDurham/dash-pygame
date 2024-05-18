#imports pygame, sys, random and pulls all functions from pygame.locals
from typing import Any
import pygame
from pygame.locals import *
import sys
import random
import time
import init as start

map = start.get_map()
char = start.get_char()
name = start.get_name()

#initializes pygame
pygame.init()

#makes a vector2 variable
vector = pygame.math.Vector2
#sets WIDTH and HEIGHT variables
HEIGHT = 600
WIDTH = 800
#makes the constant values for Acceleration, Friction and FPS 
ACC = 0.8
FRIC = -0.16
FPS = 60
#makes a clock which can be used to control how fast the game moves
FramesPerSec = pygame.time.Clock()

#makes the surface that we will use as the screen with the WIDTH and HEIGHT variables
displaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
#sets the title of the game window to be "Cheetah in Backrooms"
pygame.display.set_caption("Cheetah in Backrooms")

#sets the icon of the game to be a cheetah
icon = pygame.image.load("pygameFolder/cheetah.png")
pygame.display.set_icon(icon)

musicRef = "fnaf.mp3"
if map == 0 or map == 3:
    musicRef = "SCP-x7x.mp3"
elif map == 2:
    musicRef = "Captain Scurvy.mp3"

#initialize the mixer
mixer = pygame.mixer
mixer.init()
synth = mixer.Sound("pygameFolder/synth.wav")
jump = mixer.Sound("pygameFolder/jump.wav")
mixer.music.load("pygameFolder/" + musicRef)
mixer.music.play(1)

#setup lives
lives = 3

#defines the player class, the player sprite
class player(pygame.sprite.Sprite):
    #the function that initializes the player
    def __init__(self):
        #initializes the pygame.sprite.Sprite class used for the player
        super().__init__()
        #setups the player's surface and rect, and fills the color of the surface
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((0, 150, 255))
        self.imageRef = "cheetah.png"
        if char == 1:
            self.imageRef = "borzoi.png"
        elif char == 2:
            self.imageRef = "sillydog.png"
        elif char == 3:
            self.imageRef = "beagle.png"
        elif char == 4:
            self.imageRef = "guardchar.png"
        self.image = pygame.image.load("pygameFolder/" + self.imageRef).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.surf.get_rect()
        
        #setups the initial vectors
        self.pos = vector((10, 385))
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        #end of setup
        self.jumping = False
        self.score = 0
        
    #the function for moving the player
    def move(self):
        #math I somehow understand
        self.acc = vector(0, 0.5)
        
        #movement
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = ACC
        
        #more math, calculates the acceleration, velocity and position
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
              
        #prevents the player from going offscreen    
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        #sets the position of the player, relative to the middle of the bottom edge
        self.rect.midbottom = self.pos
    
    #makes the player jump
    def jump(self):
        hits = pygame.sprite.spritecollide(p1, platforms, False)
        if hits and not self.jumping:
            self.vel.y = -15
            self.jumping = True
            jump.play()
            
    #cancels the jump
    def Jump_cancel(self):
        if self.jumping:
            #stops the player's jump
            if self.vel.y < -3:
                self.vel.y = -3
    
    #G R A V I T Y
    def update(self):
        #test if the player is touching a platform
        hits = pygame.sprite.spritecollide(p1, platforms, False)
        if p1.vel.y > 0:
            if hits:
                #stop the player from falling
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                    self.pos.y = hits[0].rect.top+1
                    self.vel.y = 0
                    self.jumping = False

#the coin class
class coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        #initializes the pygame.sprite.Sprite class used for the player
        super().__init__()
        #coin image and rect
        self.type = random.randint(0, 3)
        self.image = pygame.image.load("pygameFolder/nyan.png").convert_alpha()
        self.moving = 0
        self.move = False
        if self.type == 1 and map != 3:
            self.image = pygame.image.load("pygameFolder/mrbeast.png").convert_alpha()
            self.moving = random.randint(0, 10)
            if self.moving >= 6:
                if map == 1:
                    self.type = 5
                    self.image = pygame.image.load("pygameFolder/springbonnie.jpg").convert_alpha()
                elif map == 0:
                    self.move = True
                elif map == 2:
                    self.type = 5
                    self.move = True
                    self.image = pygame.image.load("pygameFolder/napoleon.png").convert_alpha()
            else:
                self.move = False
        elif self.type == 1 and map == 3:
            self.image = pygame.image.load("pygameFolder/173.png").convert_alpha()
            self.move = True
            self.type = 5
        elif self.type == 2:
            if map != 3:
                self.image = pygame.image.load("pygameFolder/memedog.png").convert_alpha()
            elif map == 3:
                self.image = pygame.image.load("pygameFolder/guard.png").convert_alpha()
        elif self.type == 3 and map != 3:
            self.image = pygame.image.load("pygameFolder/boykisser.png").convert_alpha()
            self.move = True
            self.whatType = random.randint(0, 10)
            if self.whatType >= 6 and lives < 8:
                if map == 0:
                    self.type = 4
                    self.image = pygame.image.load("pygameFolder/pepsi.png").convert_alpha()
                elif map == 1:
                    self.type = 6
                    self.image = pygame.image.load("pygameFolder/book.jpg").convert_alpha()
                elif map == 2:
                    self.type = 6
                    self.move = True
                    self.image = pygame.image.load("pygameFolder/bavarians.jpg").convert_alpha()
        elif self.type == 3 and map == 3:
            self.image = pygame.image.load("pygameFolder/mtf.png").convert_alpha()
            self.type = 6
            self.move = True
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        #position the coin
        self.rect.topleft = pos
        
    def update(self):
        #moving
        if self.move:
            self.rect.move_ip(1.25, 0)
            if self.rect.left > WIDTH:
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = WIDTH
        #test if the coin is touching the player
        if self.rect.colliderect(p1.rect):
            #add score and destroy the platform
            global lives
            synth.play()
            if self.type == 0:
                p1.score += 5
            elif self.type == 1:
                p1.score -= 5
            elif self.type == 2:
                p1.score += 10
            elif self.type == 3:
                p1.score += random.randint(-2, 15)
            elif self.type == 4:
                p1.score += 8
                lives += 1
            elif self.type == 5:
                if lives <= 0:
                    p1.score -=10
                else:
                    lives -= 1
            elif self.type == 6:
                lives += 1
                
            self.kill()

#the platform class
class platform(pygame.sprite.Sprite):
    #initializes the platform
    def __init__(self, speed):
        #initializes the pygame.sprite.Sprite class used for the platform
        super().__init__()
        #set the speed variables of the platform
        self.speed = speed
        self.imageref = ""
        if self.speed == 2:
            self.imageref = "borzoi.png"
        elif self.speed == 3:
            self.imageref = "skibidi.png"
        elif self.speed == 4:
            self.imageref = "boykisser.jpg"
        else:
            if map == 0:
                self.imageref = "backroom.png"
            elif map == 1:
                self.imageref = "ballpit.jpg"
            elif map == 2:
                self.imageref = "grass.jpg"
            elif map == 3:
                self.imageref = "scp.jpg"
        #setups the platform's surface and rect, and fills the color of the surface
        self.surf = pygame.Surface((random.randint(100, 150), 12))
        self.surf.fill((0, 255, 150))
        self.image = pygame.image.load("pygameFolder/" + self.imageref).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.surf.get_width(), self.surf.get_height()))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 30)))
        
        #other varibles
        self.moving = True
        self.point = True
        
    #moves the platform
    def move(self):
        hits = self.rect.colliderect(p1.rect)
        if self.moving == True:
            self.rect.move_ip(self.speed, 0)
            #makes the player move with the platform
            if hits:
                p1.pos += (self.speed, 0)
            #"walls"
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed > 0 and self.rect.right < 0:
                self.rect.left = WIDTH
    
    #generates a coin
    def gen_coin(self):
        if (self.speed >= 1):
            plat_coin = coin((self.rect.centerx, self.rect.centery))
            coins.add(plat_coin) 
    
#make sure the platforms are not touching
def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity in platforms:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 60) and (abs(platform.rect.bottom - entity.rect.top) < 60):
                return True
            
            if (abs(platform.rect.top + entity.rect.bottom) < 150) and (abs(platform.rect.bottom + entity.rect.top) < 100):
                C = False
#generate platforms
def plat_gen():
    #when there are less than 20 platforms
    while len(platforms) < 20:
        #make the platform
        width = random.randrange(100, 300)
        p = platform(random.randint(0, 3))
        C = True
        #loop until the platform is in a good spot
        while C:
            p = platform(random.randint(0, 3))
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            C = check(p, platforms)
        #add the platform to groups
        p.gen_coin()
        platforms.add(p)
        all_sprites.add(p)
#makes player and platform objects
pt1 = platform(0)
p1 = player()
pt1.surf = pygame.Surface((WIDTH, 20))
pt1.surf.fill((0, 255, 150))
pt1.rect = pt1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
pt1.moving = False
pt1.point = False
pt1.image = pygame.transform.scale(pt1.image, (pt1.surf.get_width(), pt1.surf.get_height()))
 
#platform group
platforms = pygame.sprite.Group()
platforms.add(pt1)

#creates and adds p1 and pt1 to all_sprites in a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(pt1)
all_sprites.add(p1)

#coin group
coins = pygame.sprite.Group()

#make the first platforms
for i in range(random.randint(15, 20)):
    #make the platform
    P1 = platform(random.randint(0, 3))
    P1.gen_coin()
    #add the platform to groups
    platforms.add(P1)
    all_sprites.add(P1)
    
#sky image
if map == 0:
    sky = pygame.image.load("pygameFolder/backrooms.png")
elif map == 1:
    sky = pygame.image.load("pygameFolder/pitback.jpg")
elif map == 2:
    sky = pygame.image.load("pygameFolder/napback.png")
elif map == 3:
    sky = pygame.image.load("pygameFolder/scpback.png")

sky = pygame.transform.scale(sky, (800, 600))

#life function
def showLives():
    lifeImg = pygame.image.load("pygameFolder/sillydog.png").convert_alpha()
    if map == 1:
        lifeImg = pygame.image.load("pygameFolder/bonbon.png").convert_alpha()
    elif map == 2:
        lifeImg = pygame.image.load("pygameFolder/borzoi.png").convert_alpha()
    lifeImg = pygame.transform.scale(lifeImg, (50, 50))
    lifePos = 0
    for life in range(lives):
        displaySurf.blit(lifeImg, (lifePos, 0))
        lifePos += 100

def showEverything():
    #fills the screen a color
    displaySurf.fill((0, 200, 255))
    skyRect = pygame.rect.RectType(0, 0, WIDTH, HEIGHT)
    displaySurf.blit(sky, (0, 0), skyRect)
    f = pygame.font.SysFont("Courier New", 50, True, False)
    g = f.render(str(p1.score), True, (255, 255, 255))
    displaySurf.blit(g, (WIDTH/2, 10))
    #a for-loop to show the sprites
    for entity in all_sprites:
        displaySurf.blit(entity.image, entity.rect)
        entity.move()
    #loop for coins
    for entity in coins:
        displaySurf.blit(entity.image, entity.rect)
    #shows lives
    showLives()
    #makes the player move and show on screen
    p1.update()
    #update the display   
    pygame.display.update()

#main loop
while True:
    #gets the events that just happened
    for event in pygame.event.get():
        #test if the "X" is pressed
        if event.type == QUIT:
            #quit the game
            pygame.quit()
            sys.exit()
        #test if a key is pressed
        if event.type == KEYDOWN:
            #test if escape is pressed
            if event.key == K_ESCAPE:
                #quit the game
                pygame.quit()
                sys.exit()
            #test if space is pressed
            if event.key == pygame.K_SPACE:
                p1.jump()
                
        if event.type == KEYUP:
            p1.Jump_cancel()
        
    #test if the player is at the last 3rd of the screen
    if p1.rect.top <= HEIGHT/3:
        #scroll the screen up
        p1.pos.y += abs(p1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(p1.vel.y)
            #test to destroy the platform
            if plat.rect.top >= HEIGHT:
                #kill the platform
                plat.kill()
        plat_gen()
                
        for c in coins:
            c.rect.y += abs(p1.vel.y)
            #test to destroy the platform
            if c.rect.top >= HEIGHT:
                #kill the platform
                c.kill()
    
    #shows everything
    showEverything()
    
    #a loop for the coins
    for c in coins:
        displaySurf.blit(c.image, c.rect)
        c.update()
    
    #if the player falls of the screen
    if p1.rect.top > HEIGHT and lives <= 0:
        #kill every entity
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        #score text
        ScoreFile = open("pygameFolder/game/scores/scores.txt", "a")
        ScoreFile.write(name + ": " + str(p1.score) + "\n")
        
        ScoreFile2 = open("pygameFolder/game/scores.txt", "r")
        scoreListText = ScoreFile2.read()
        if len(scoreListText) >= 15:
            ScoreFile[0] = ""
        ScoreFile.close()
        ScoreFile2.close()
        leaderboardFile = open("pygameFolder/game/scores/scores.txt", "r")
        scores = leaderboardFile.readlines()
        
        #gameover screen
        displaySurf.fill((255, 100, 0))
        f = pygame.font.SysFont("Courier New", 20, True, False)
        g = f.render("FINAL SCORE: " + str(p1.score), True, (255, 255, 255))
        scoretext = f.render("Scores (Old at the top):", True, (255, 255, 255))
        scoreY = 50
        displaySurf.blit(scoretext, (400, scoreY))
        for i in scores:
            scoreY += 30
            scoretext = f.render(i.strip(), True, (255, 255, 255))
            displaySurf.blit(scoretext, (400, scoreY))
        displaySurf.blit(g, (0, HEIGHT/2.5))
        pygame.display.update()
        #quit the game
        time.sleep(3)
        pygame.quit()
        sys.exit()
    elif p1.rect.top > HEIGHT and lives >= 1:
        lives -= 1
        p1.pos.y = 0
        p1.update
        
    FramesPerSec.tick(FPS)