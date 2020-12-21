import pygame, sys, os, time

import char
import opening
import constans
pygame.init()

bg = pygame.image.load(os.path.join('house1.gif'))
#sprites

Walk_Left = []
Wlak_Right = []
Walk_Up = []
Walk_Down = []



#ply_spr === sprite választás
#ply_st === player skill pointok

def phase_1(win ,ply_spr ,ply_st):
    # win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
    # if ply_spr != None:
    #     if ply_spr == "bal":
    #         Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
    #         Wlak_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
    #         Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
    #         Walk_Down = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
    #         return "működik?"
    #
    #     if ply_spr == "jobb":
    #         Walk_Left = [pygame.image.load('witch_l1.gif'),pygame.image.load('witch_l2.gif')]
    #         Wlak_Right = [pygame.image.load('witch_r1.gif'),pygame.image.load('witch_r2.gif')]
    #         Walk_Up = [pygame.image.load('witch_b1.gif'),pygame.image.load('witch_b2.gif')]
    #         Walk_Down = [pygame.image.load('witch_r1.gif'),pygame.image.load('witch_r2.gif')]
    #         return "not yet"
    # else:
    #     return "nagy a baj"
    ply_st.move(win,bg)
    return 0
