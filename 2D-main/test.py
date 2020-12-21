import pygame, sys, time, os

import constans
Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
Wlak_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
Walk_Down = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]

win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))
pygame.display.set_caption(" The Hobblyat ")

r = True
while r:
    pygame.time.delay(100)

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        r = False
    if key[pygame.K_a]:
        win.blit(Walk_Left[0])

    pygame.display.update()
