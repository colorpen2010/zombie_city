import pygame, random

rect = pygame.Rect([random.randint(1, 400), random.randint(1, 400), 42, 82])
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


sdanie=100,100,777,574