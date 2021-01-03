import pygame, sys, os, time

import engine
import char
import opening
import constans
pygame.init()


#ply_spr === sprite választás
#ply_st === player skill pointok




def phase_1(win ,ply_spr ,ply_st):
    bg = pygame.image.load(os.path.join('house1.gif'))
    r = ply_st.action(win,bg,ply_spr)
    pygame.display.update()
