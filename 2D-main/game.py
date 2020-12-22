import pygame, sys, os, time

import engine
import char
import opening
import constans
pygame.init()

bg = pygame.image.load(os.path.join('house1.gif'))

#ply_spr === sprite választás
#ply_st === player skill pointok


def phase_1(win ,ply_spr ,ply_st):
    ply_st.move(win,bg,ply_spr)
    return 0
