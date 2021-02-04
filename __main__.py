import pygame, time, risovanie, controller, model

pygame.init()

while 1 < 10:
    # задержка
    time.sleep(1 / 60)

    controller.control_1()

    risovanie.paint_1()

