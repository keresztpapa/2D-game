import pygame, sys, os, time

import char
import opening
import constans
pygame.init()

bg = pygame.image.load(os.path.join('house1.gif'))
#sprites
Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
Wlak_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
Walk_Down = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]


def phase_1(win):
        win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
        pygame.display.update()
        time.sleep(5)
