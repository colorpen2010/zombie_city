import pygame, random

heart = 3

zona_ataki = None

sdanie = pygame.Rect([100, 300, 262, 216])

sdanie1 = pygame.Rect([500, 500, 386, 380])

zombie_rect = pygame.Rect(400, 100, 46, 80)

player_rect = pygame.Rect([10, 10, 42, 82])
ak1 = 1
ak2 = -1
poworot = 'right'


def right(shag):
    global heart
    player_rect.x += shag
    what = player_rect.colliderect(sdanie)
    if what == 1:
        player_rect.x -= shag

    what = player_rect.colliderect(sdanie1)
    if what == 1:
        player_rect.x -= shag

    what = player_rect.colliderect(zombie_rect)
    if what == 1:
        player_rect.x -= shag * 10
        heart -= 1


def up(fly):
    global heart
    player_rect.y += fly
    what = player_rect.colliderect(sdanie)
    if what == 1:
        player_rect.y -= fly

    what = player_rect.colliderect(sdanie1)
    if what == 1:
        player_rect.y -= fly

    what = player_rect.colliderect(zombie_rect)
    if what == 1:
        player_rect.y -= fly * 10
        heart -= 1


def ataka_player1():
    global zona_ataki
    zona_ataki = pygame.Rect([player_rect.x,player_rect.y, 100, 100])
    if zona_ataki.colliderect(zombie_rect):
        print('show youself')
