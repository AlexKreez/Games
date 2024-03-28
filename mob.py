import pygame
from pygame_function import *


class mob(pygame.sprite.Sprite):
    def __init__(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.groupspriteB = pygame.sprite.OrderedUpdates()
        self.sprite = makeSprite('stand_en/' + path + '/st1.png')
        self.sprite.charasteristics(100, 30)

        self.sprite.move(600, 300)
        self.groupspriteB.add(self.sprite)

        self.x = 0
        self.y = 0

        LoadSprite('right_en/' + path, 6, self.sprite)
        LoadSprite('left_en/' + path, 6, self.sprite)
        LoadSprite('attack_en', 9, self.sprite)