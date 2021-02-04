import pygame, help, model
from pygame import draw



screen = pygame.display.set_mode([1300, 700])

# загружаем картинку фона
fon = pygame.image.load('skins_and_world/world_1_1_1.png')

house = pygame.image.load('skins_and_world/zombie house 1.jpg')

house = help.izmeni_kartinku(house, 262, 216, [255, 255, 255], 0)

player_ran_1 = pygame.image.load('skins_and_world/survivor.png').convert()
player_ran_1 = help.izmeni_kartinku(player_ran_1, 42, 82, [0, 0, 0], 20)

zombie1=pygame.image.load('skins_and_world/zombie_BETA_VERSION.png')
zombie1=help.izmeni_kartinku(zombie1,42,82,[0,0,0],60)

house1=pygame.image.load('skins_and_world/house_11.jpg')

house1=help.izmeni_kartinku(house1,386,380,[48,50,45],10)

sdvig_x = 100

sdvig_y = 200

def paint_1():
    global sdvig_x,sdvig_y

    # рисуем кадр
    screen.fill([0, 0, 0])
    sdvig_x = 650 - model.rect.centerx
    sdvig_y = 350 - model.rect.centery
    screen.blit(fon, sdvig([0, 1]))

    screen.blit(house, sdvig(model.sdanie))

    screen.blit(house1,sdvig(model.sdanie1))

    screen.blit(player_ran_1, sdvig(model.rect))

    screen.blit(zombie1,sdvig([0,100]))

    pygame.draw.rect(screen,[255,0,0],sdvig(model.sdanie),2)
    pygame.draw.rect(screen,[255,0,0],sdvig(model.sdanie1),2)

    pygame.display.flip()


def sdvig(rect):
    if isinstance(rect, pygame.Rect):
        rect = pygame.Rect(rect)
    rect[0] += sdvig_x
    rect[1] += sdvig_y
    return rect
