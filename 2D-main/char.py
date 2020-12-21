import pygame, sys

import opening
import game
import constans
pygame.init()

class Character():
    def __init__(self, hp, dmg, deff, pos_x, pos_y):
        self.hp = hp
        self.dmg = dmg
        self.deff = deff
        self.skill = 11
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def get_hp(self):
        return self.hp

    def get_dmg(self):
        return self.dmg

    def get_deff(self):
        return self.deff

    def set_hp(self, x):
        self.hp = x

    def set_dmg(self, x):
        self.dmg = x

    def set_deff(self, x):
        self.deff = x

    def set_skill(self,x):
        self.skill = x

    def get_skill(self):
        return self.skill
