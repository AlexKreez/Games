import pygame
import math
import random
import pygame_menu
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button, ButtonArray
from pygame_widgets.slider import Slider
from hero import *
from mob import *
from pygame_function import *

pygame.init()

move = False

done = False

border_left = False
border_right = True
hits = {}
hits2 = {}

window = pygame.display.set_mode((2560, 1440))

screen = pygame.Surface((2560, 1440))


# button = Button(window, 300, 300, 50, 100, text='HI!', onClick=lambda:print('nice!'))

def set_difficulty(level, value):
    if 'Hard' and value == 2:
        orcSprite.charasteristics(+100, +30)


def game_start():
    menu._close()


# menu = pygame_menu.Menu(300, 400, 'Pause', theme=pygame_menu.themes.THEME_GREEN)
# menu.add_text_input('name', default=')')
# menu.add_selector('difficulty', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
# menu.add_button('Start', game_start)
# menu.add_button('Exit', pygame_menu.events.EXIT)
# menu.mainloop(window)

img_b = pygame.image.load('bg.png')
img_b = pygame.transform.scale(img_b, (2560, 1440))

count = 1

myfont = pygame.font.SysFont('arial black', 20)

x_m = 60
y_m = 0
'''spriteGroupBorders = pygame.sprite.OrderedUpdates()
frame = makeSprite('border/1.png')
spriteGroupBorders.add(frame)'''

right = True

# def print_shop(menu, x, y, font_color = (0, 0, 0), font_type = '19919', font_size = 10):
# font_type = pygame.font.Font(font_type, font_size)
# menu = font_type.render(menu, True, font_color)
# pygame.display.blit(menu, (x, y))


hero = hero()
groupSpriteA = hero.groupspriteA
agent = hero.agent

orc = mob('orc')
groupSpriteB = orc.groupspriteB
orcSprite = orc.sprite


# def border():
# borderCollide = pygame.sprite.groupcollide(groupSpriteA, spriteGroupBorders, False, False)
# if borderCollide:
# print('YESYESYESYESYESYESYESYES')


def updateDisplay():
    global hits, hits2
    string = myfont.render('Волна:' + str(count), 0, (0, 0, 0))
    screen.blit(string, (400, 0))
    window.blit(screen, (0, 0))
    groupSpriteA.update()
    groupSpriteB.update()
    # spriteGroupBorders.update()
    hits = pygame.sprite.groupcollide(groupSpriteA, groupSpriteB, False, False)
    hits2 = pygame.sprite.groupcollide(groupSpriteB, groupSpriteA, False, False)
    screen.blit(img_b, (0, 0))
    groupSpriteA.draw(screen)
    groupSpriteB.draw(screen)
    # spriteGroupBorders.draw(screen)
    # button.draw()
    pygame.display.update()
    pygame.display.flip()


print(groupSpriteA)
print(groupSpriteB)
# frame.move(300, 300)
pygame.time.set_timer(pygame.USEREVENT, 3000)

while done == False:
    breakpoint('while')
    # border()
    updateDisplay()
    print(hits2)
    if len(hits2) != 0 and hits:

        orcSprite.animation("attack_en", 13, orc)
        agent.hp -= orcSprite.attack

        # if agent.hp <= 0 and agent.alive():
        # agent.kill()
    else:
        print(orc.x)
        if orc.x <= 200:
            border_right = True
            border_left = False
        if border_right:
            orc.x += 5
            orcSprite.animation("right_en", 1, orc)
        if orc.x >= 1200:
            border_left = True
            border_right = False
        if border_left:
            orc.x -= 5
            orcSprite.animation("left_en", 7, orc)
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            updateDisplay()
            if orcSprite.hp <= 0 and orcSprite.alive():
                print(orcSprite.hp)
                print(orc.kill())
                orcSprite.kill()
                pygame.USEREVENT += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            menu = pygame_menu.Menu(300, 400, 'Pause', theme=pygame_menu.themes.THEME_GREEN)
            menu.add_text_input('BEST GAME EVER')
            menu.add_selector('difficulty', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
            menu.add_button('Start', game_start)
            menu.add_button('Exit', pygame_menu.events.EXIT)
            menu.mainloop(window)
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                pos = pygame.mouse.get_pos()
                move = True
                if hits:
                    orcSprite.hp -= agent.attack
                    print('- ', agent.attack)
        '''if move == True:
            while ((hero.x - pos[0] != 0) and (hero.y - pos[1] != 0)):
                if (hero.x - pos[0] > -20 and hero.x - pos[0] < 5) and (hero.y < pos[1]):
                    hero.y += 1
                    agent.animation('straight', 19, hero)
                    border()
                elif (hero.x - pos[0] > -20 and hero.x - pos[0] < 5) and (hero.y > pos[1]):
                    hero.y -= 1
                    agent.animation('back', 13, hero)
                    border()
                elif (hero.y - pos[1] > -20 and hero.y - pos[1] < 5) and (hero.x < pos[0]):
                    hero.x += 1
                    agent.animation('right', 1, hero)
                    border()
                elif (hero.y - pos[1] > -20 and hero.y - pos[1] < 5) and (hero.x > pos[0]):
                    hero.x -= 1
                    agent.animation('left', 7, hero)
                    border()
                elif hero.x < pos[0] and hero.y < pos[1]:
                    hero.y += 1
                    hero.x += 1
                    border()
                elif hero.x > pos[0] and hero.y > pos[1]:
                    hero.y -= 1
                    hero.x -= 1
                    border()
                elif hero.x > pos[0] and hero.y < pos[1]:
                    hero.y += 1
                    hero.x -= 1
                    border()
                elif hero.x < pos[0] and hero.y > pos[1]:
                    hero.y -= 1
                    hero.x += 1
                    border()
                if orc.x <= 20:
                    border_right = True
                    border_left = False
                if border_right:
                    orc.x += 0.5
                    orcSprite.animation("right_en", 1, orc)
                if orc.x >= 560:
                    border_left = True
                    border_right = False
                if border_left:
                    orc.x -= 0.5
                    orcSprite.animation("left_en", 7, orc)'''
        # updateDisplay()

pygame.quit()
