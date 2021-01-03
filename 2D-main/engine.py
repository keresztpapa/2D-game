import pygame, sys, os, time


import constans


class Chest():

    def __init__(self,pos_x,pos_y):
            self.pos_x = pos_x
            self.pos_y = pos_y

    def chest_show(self,win):
        chest_pic = pygame.image.load(os.path.join('chest.png'))
        win.blit(chest_pic, (self.pos_x, self.pos_y))
        pygame.display.update()


    def get_pos_x():
        return self.pos_x

    def get_pos_y():
        return self.pos_y
