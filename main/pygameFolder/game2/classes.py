import pygame
import time

class character(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pygameFolder/" + img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.minPos = (self.pos[0], self.pos[1])
        self.maxPos = (self.pos[0] * 2, self.pos[1] * 2)
        self.clicked = False
        self.on = True
        
    def clickedOn(self, mouse, sound, mouse2):
        if self.on:
            if mouse[0] >= self.minPos[0] and mouse[0] <= self.maxPos[0]:
                if mouse[1] >= self.minPos[1] and mouse[1] <= self.maxPos[1]:
                    if mouse2[0] and self.clicked == False:
                        print("Clicked on! " + str(self.rect.center))
                        sound.play()
                        self.clicked = True
                        return(True)
        
    def update(self, screen):
        #self.clickedOn(mouse, sound, mouse2)
        if self.on:
            screen.blit(self.image, self.rect.center)
            
    def changeImg(self, ref):
        self.image = pygame.image.load("pygameFolder/" + ref).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
        
class level():
    def __init__(self, img, size):
        self.size = size
        self.image = self.getImg(img)
        
    def getImg(self, img):
        self.imgSurf = pygame.image.load("pygameFolder/" + img).convert_alpha()
        self.imgSurf = pygame.transform.scale(self.imgSurf, self.size)
        return(self.imgSurf)
        
    def update(self, screen, newImg):
        self.image = self.getImg(newImg)
        screen.blit(self.image, (0, 0))
        
class object(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pygameFolder/" + img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 600))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        
    def update(self, screen):
        screen.blit(self.image, self.rect.center)