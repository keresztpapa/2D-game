import pygame, sys

import opening
import game
import constans
pygame.init()

class Character():
    def __init__(self, hp, dmg, deff):
        self.hp = hp
        self.dmg = dmg
        self.deff = deff

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
