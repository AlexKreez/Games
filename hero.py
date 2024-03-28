import pygame
from pygame_function import *

class hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.groupspriteA = pygame.sprite.OrderedUpdates()
        self.agent = makeSprite('stand/st1.png')
        self.agent.charasteristics(300, 100)

        self.agent.move(1000, 400)
        self.groupspriteA.add(self.agent)

        self.x = 0
        self.y = 0

        LoadSprite('right', 6, self.agent)
        LoadSprite('left', 6, self.agent)
        LoadSprite('sword_punch', 6, self.agent)

