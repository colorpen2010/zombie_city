import pygame, help, model
from pygame import draw

screen = pygame.display.set_mode([1300, 700])

# загружаем картинку фона
fon = pygame.image.load('skins_and_world/world_1_1_1.png')

draw.rect(fon,[0,0,0],model.sdanie)

house = pygame.image.load('skins_and_world/s_fire_station_2.png')

fon.blit(house, [100, 100])

player_ran_1 = pygame.image.load('skins_and_world/survivor.png').convert()
player_ran_1 = help.izmeni_kartinku(player_ran_1, 42, 82, [0, 0, 0], 20)


def paint_1():
    # рисуем кадр

    screen.blit(fon, [0, 1])

    screen.blit(player_ran_1, model.rect)

    pygame.display.flip()
