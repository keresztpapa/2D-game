import pygame, sys, os, time

import opening
import constans
pygame.init()

bg = pygame.image.load(os.path.join('assets','house1.gif'))

def phase_1(win):
        win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
        pygame.display.update()
        time.sleep(5)
