import pygame
import classes
import time
import random

pygame.init()
clock = pygame.time.Clock()

#define screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cheetah in Backrooms 2: the Electric Boogaloo")

borzoi = classes.character("borzoi.png", (400, 400))
cheetah = classes.character("cheetah.png", (150, 400))
mainChars = [borzoi, cheetah]

airplane = classes.character("airplane_outside.png", (400, 200))
otherChars = [airplane]

#values for later
guard = None
button = None
door = None
noob = None
oreo = None
pepsi = None
nuke = None
scp = None
water = None
boat = None
submarine = None
beagle = None
part = None
parts = 4
noobHealth = 3

#add to groups
charGroup = pygame.sprite.Group()
charGroup.add(mainChars, otherChars)

objGroup = pygame.sprite.Group()

mixer = pygame.mixer
mixer.init()
sound = mixer.Sound("pygameFolder/synth.wav")
pilotVoice = mixer.Sound("pygameFolder/pilot.mp3")
yumSound = mixer.Sound("pygameFolder/yumyumyum.mp3")
nukeSound = mixer.Sound("pygameFolder/nukesound.mp3")
nukeSound.set_volume(10000)
helloSound = mixer.Sound("pygameFolder/hello.mp3")
alarmSound = mixer.Sound("pygameFolder/alarm.mp3")

music = pygame.mixer_music
music.load("pygameFolder/fnaf.mp3")
music.set_volume(20)

curLvl = "backrooms.png"
lvl = classes.level(curLvl, screen.get_size())

run = True

def voice():
    global curLvl
    
    voiceNum = pilotVoice.get_length()
    pilotVoice.play()
                
    screen.fill((0, 0, 0))
    lvl.update(screen, curLvl)
    for char in charGroup:
        char.update(screen)
    
    pygame.display.update()
                
    time.sleep(voiceNum)
                
    curLvl = "scpback.png"

def updateScreen():
    screen.fill((0, 150, 255))
    lvl.update(screen, curLvl)
    for obj in objGroup:
        obj.update(screen)
    for char in charGroup:
        char.update(screen)
    pygame.display.update()

def win():
    f = pygame.font.SysFont("Comic Sans", 150, True, False)
    text = f.render("You win!", 1, (10, 255, 50))
    screen.blit(text, (100, 100))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()

music.play(1)

while run:
    clock.tick(30)
    
    mouse = pygame.mouse.get_pos()
    mouse2 = pygame.mouse.get_pressed()
    
    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                
    screen.fill((0, 150, 255))
    lvl.update(screen, curLvl)
    for obj in objGroup:
        obj.update(screen)
    for char in charGroup:
        char.update(screen)
        if char.clickedOn(mouse, sound, mouse2):
            if char == airplane:
                borzoi.changeImg("096.png")
                borzoi.clicked = False
                           
                airplane.on = False
                airplane.remove(charGroup)
                airplane = None
                curLvl = "airplane.png"
                
            if char == borzoi and curLvl == "airplane.png":
                borzoi.changeImg("borzoi.png")
                voice()
                guard = classes.character("guardchar.png", (300, 100))
                charGroup.add(guard)
                char.clicked = False
                
            if char == guard:
                helpsound = mixer.Sound("pygameFolder/help.mp3")
                helpsound.play()
                guard.changeImg("blood.png")
                button = classes.character("button.png", (400, 300))
                charGroup.add(button)
                
            if char == button:
                guard.on = False
                guard.remove(charGroup)
                guard = None
                
                button.on = False
                button.remove(charGroup)
                button = None
                
                door = classes.object("door.png", (150, 0))
                objGroup.add(door)
                for obj in objGroup:
                    obj.update(screen)
                for char in charGroup:
                    char.update(screen)
                pygame.display.update()
                
                time.sleep(1.5)
                
                door.remove(objGroup)
                door = None
                curLvl = "pitback.jpg"
                
                noob = classes.character("noob.png", (400, 200))
                charGroup.add(noob)
                
            if char == noob:
                if noobHealth == 3:
                    oreo = classes.character("oreo.png", (350, 175))
                    charGroup.add(oreo)
                elif noobHealth == 2:
                    pepsi = classes.character("pepsi.png", (200, 200))
                    charGroup.add(pepsi)
                elif noobHealth == 1:
                    nuke = classes.character("nuke.png", (400, 50))
                    charGroup.add(nuke)
                    nuke.clicked = False
                    
            if char == oreo:
                if noobHealth == 3:
                    yumSound.play()
                    length = yumSound.get_length()
                    time.sleep(length)
                    
                    noobHealth -= 1
                    oreo.remove(charGroup)
                    oreo = None
                    noob.clicked = False
                    
            if char == pepsi:
                if noobHealth == 2:
                    yumSound.play()
                    length = yumSound.get_length()
                    time.sleep(length)
                    
                    noobHealth -= 1
                    pepsi.remove(charGroup)
                    pepsi = None
                    noob.clicked = False
                    
            if char == nuke:
                print(noobHealth)
                if noobHealth == 1:
                    helpsound.play()
                    length = helpsound.get_length()
                    time.sleep(length)
                    
                    nukeSound.play()
                    length = nukeSound.get_length()
                    time.sleep(0.19)
                    
                    noobHealth -= 1
                    nuke.remove(charGroup)
                    nuke = None
                    noob.remove(charGroup)
                    noob = None
                    curLvl = "grass.jpg"
                    
                    scp = classes.character("173.png", (300, 250))
                    charGroup.add(scp)
                    water = classes.object("water.png", (400, 100))
                    water.image = pygame.transform.scale(water.image, (200, 200))
                    objGroup.add(water)
                    
            if char == scp:
                scp.changeImg("explode.png")
                nukeSound.play()
                time.sleep(0.15)
                nukeSound.stop()
                time.sleep(0.30)
                scp.remove(charGroup)
                scp = None
                
                boat = classes.character("ship.png", (400, 150))
                charGroup.add(boat)
            
            if char == boat:
                water.remove(objGroup)
                water = None
                
                curLvl = "beach.png"
                time.sleep(0.5)
                boat.remove(charGroup)
                boat = None
                time.sleep(0.3)
                submarine = classes.character("submarine.png", (300, 300))
                charGroup.add(submarine)
                
            if char == submarine:
                submarine.remove(charGroup)
                submarine = None
                
                curLvl = "underwater.jpg"
                updateScreen()
                time.sleep(1)
                curLvl = "beach.png"
                updateScreen()
                time.sleep(0.8)
                curLvl = "rocket.png"
                updateScreen()
                time.sleep(0.8)
                nukeSound.play()
                time.sleep(nukeSound.get_length())
                curLvl = "space.jpg"
                updateScreen()
                time.sleep(1)
                curLvl = "station.png"
                beagle = classes.character("beagle.png", (200, 250))
                charGroup.add(beagle)
                helloSound.play()
                updateScreen()
                
            if char == beagle:
                beagle.remove(charGroup)
                beagle = None
                
                alarmSound.play()
                time.sleep(1)
                alarmSound.stop()
                nukeSound.play()
                curLvl = "mars.jpg"
                part = classes.character("gear.png", (random.randint(50, 600), random.randint(0, 400)))
                part.image = pygame.transform.scale(part.image, (50, 50))
                charGroup.add(part)
                
            if char == part:
                if parts >= 2:
                    parts -= 1
                    part.remove(charGroup)
                    part = classes.character("gear.png", (random.randint(50, 600), random.randint(0, 400)))
                    part.image = pygame.transform.scale(part.image, (50, 50))
                    charGroup.add(part)
                if parts == 1:
                    parts = 0
                    part.remove(charGroup)
                    part = None
                    time.sleep(0.1)
                    curLvl = "backrooms.png"
                    updateScreen()
                    win()
                
    pygame.display.flip()
        
pygame.quit()