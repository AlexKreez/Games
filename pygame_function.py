import pygame, math, sys, os

from IGRA2 import groupSpriteB, groupSpriteA


def loadImage(filename, useColorKey = False):
    if os.path.isfile(filename):
        image = pygame.image.load(filename)
        image = image.convert_alpha()
        return image
    else:
        raise Exception('Ошибка загрузки изображения'+ filename)

    
class newSprite(pygame.sprite.Sprite):
    def __init__(self, filename, frames = 1):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename)
        self.originalWidth = img.get_width()
        self.originalHeight = img.get_height()
        frameSurface = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurface = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
            frameSurface.blit(img, (x, 0))
            self.images.append(frameSurface.copy())
            x -= self.originalWidth
        self.image = pygame.Surface.copy(self.images[0])
        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1
        self.imagenow = 0


    def move(self, x_pos, y_pos, centre = False):
        if centre:
            self.rect.centre = [x_pos, y_pos]
        else:
            self.rect.topleft = [x_pos, y_pos]

    def addImage(self, filename):
        self.images.append(loadImage(filename))
        
    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pygame.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pygame.mask.from_surface(self.image)

    def charasteristics(self, hp, attack):
        self.hp = hp
        self.attack = attack

    def animation(self, direction, firstImage, member):
        global hit, hits2
        hits2 = pygame.sprite.groupcollide(groupSpriteB, groupSpriteA, False, False)
        if self.imagenow < firstImage:
            self.imagenow = firstImage
        if direction == 'right' or direction == "right_en":
            if self.imagenow > 6:
                self.imagenow = 1
        if direction == 'left' or direction == "left_en":
            if self.imagenow > 12:
                self.imagenow = 7
        if direction == 'sword_punch':
            if self.imagenow > 18:
                self.imagenow = 13
        if direction == 'attack_en':
            if self.imagenow > 21:
                self.imagenow = 13
        changeSpriteImage(self, round(self.imagenow))
        self.imagenow += 0.5
        print(self.imagenow)
        self.move(member.x, member.y)
def makeSprite(filename, frames=1):
    thisSprite = newSprite(filename, frames)
    return thisSprite


def addSpriteImage(sprite, image):
    sprite.addImage(image)

    
def changeSpriteImage(sprite, index):
    sprite.changeImage(index)

def clock():
    current_time = pygame.time.get_ticks()
    return current_time

def LoadSprite(direction, c, object):
    for n in range(c):
        Pp = direction + "/" + str(n+1) + ".png"
        addSpriteImage(object, Pp)
