import pygame, random

heart = 3

zombie_heart=3

zona_ataki = None

sdanie = pygame.Rect([100, 300, 262, 216])

sdanie1 = pygame.Rect([500, 500, 386, 380])

zombie_rect = pygame.Rect(450, 150, 46, 80)

player_rect = pygame.Rect([5000/2,5000/2, 42, 82])
ak1 = 1
ak2 = -1
poworot = 'up'

playerincar=False


treex1=pygame.Rect([2500,2500],[160,165])
treex2=pygame.Rect([2200,2200],[160,165])
treex3=pygame.Rect([2500,2200],[160,165])
treex4=pygame.Rect([2200,2500],[160,165])

tavriax=pygame.Rect([2000,2500],[150,150])

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
    global zona_ataki,zombie_heart
    zona_ataki = pygame.Rect([player_rect.x-23,player_rect.y-40, 46+player_rect.w, 80+player_rect.h])
    if zona_ataki.colliderect(zombie_rect):
        zombie_heart-=1
