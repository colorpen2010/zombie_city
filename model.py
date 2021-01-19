import pygame, random

sdanie=pygame.Rect([100,300,262,216])

rect = pygame.Rect([10, 10, 42, 82])
ak1=10
ak2=-10

def right(shag):
    rect.x += shag
    what=rect.colliderect(sdanie)
    if what==1:
        rect.x -= shag


def up(fly):
    rect.y += fly
    what = rect.colliderect(sdanie)
    if what == 1:
        rect.y -= fly

