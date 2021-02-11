import pygame, random

heart = 3

sdanie = pygame.Rect([100, 300, 262, 216])

sdanie1 = pygame.Rect([500, 500, 386, 380])

zombie_rect = pygame.Rect(400, 100, 46, 80)

rect = pygame.Rect([10, 10, 42, 82])
ak1 = 1
ak2 = -1


def right(shag):
    global heart
    rect.x += shag
    what = rect.colliderect(sdanie)
    if what == 1:
        rect.x -= shag

    what = rect.colliderect(sdanie1)
    if what == 1:
        rect.x -= shag

    what = rect.colliderect(zombie_rect)
    if what == 1:
        rect.x -= shag*10
        heart -= 1


def up(fly):
    global heart
    rect.y += fly
    what = rect.colliderect(sdanie)
    if what == 1:
        rect.y -= fly

    what = rect.colliderect(sdanie1)
    if what == 1:
        rect.y -= fly

    what = rect.colliderect(zombie_rect)
    if what == 1:
        rect.y -= fly*10
        heart -= 1
