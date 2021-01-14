import pygame,model
pygame.init()
pygame.key.set_repeat(1000//60)
def control_1():
    # обработка событий
    coffin_dance = pygame.event.get()
    for e in coffin_dance:
        if e.type == pygame.MOUSEMOTION:
            pass
        if e.type==pygame.KEYDOWN and e.key==pygame.K_RIGHT:
            model.right(model.ak1)
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_LEFT:
            model.right(model.ak2)
        if e.type==pygame.KEYDOWN and e.key==pygame.K_UP:
            model.up(model.ak2)
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_DOWN:
            model.up(model.ak1)