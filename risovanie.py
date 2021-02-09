import pygame, help, model
from pygame import draw



screen = pygame.display.set_mode([1300, 700])
pygame.display.set_caption("zombie city")

# загружаем картинку фона
fon = pygame.image.load('skins_and_world/world_1_1_1.png')

house = pygame.image.load('skins_and_world/zombie house 1.jpg')

house = help.izmeni_kartinku(house, 262, 216, [255, 255, 255], 0)

player_ran_1 = pygame.image.load('skins_and_world/survivor.png').convert()
player_ran_1 = help.izmeni_kartinku(player_ran_1, 42, 82, [0, 0, 0], 20)

player_heart=pygame.image.load('skins_and_world/zombie_game_heart.png')

player_heart=help.izmeni_kartinku(player_heart,73,69,[255,255,255],1)

zombie_heart=pygame.transform.scale(player_heart,[30,30])

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
    player_heerd()

    screen.blit(zombie1,sdvig(model.zombie_rect))
    zombie_heerd()

    pygame.display.flip()

def player_heerd():
    screen.blit(player_heart,[1150,0])
    screen.blit(player_heart,[1050,0])
    screen.blit(player_heart,[950,0])

def zombie_heerd():
    x=model.zombie_rect.x-10
    y=model.zombie_rect.y-50
    screen.blit(zombie_heart,sdvig([x,y]))




def sdvig(rect):
    if isinstance(rect, pygame.Rect):
        rect = pygame.Rect(rect)
    rect[0] += sdvig_x
    rect[1] += sdvig_y
    return rect
