import pygame, sys

import engine
import opening
import game
import constans
pygame.init()


class Character():

    Walk_Left = []
    Walk_Right = []
    Walk_Up = []
    Walk_Down = []

    #constructor
    def __init__(self, hp, dmg, deff, pos_x, pos_y):
        self.name = constans.NAME
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

    def move(self,win,bg,spr):
        walkCount = 0
        r = True
        left = False
        right = False
        up = False
        down = False
        vel = 10
        if spr == "bal":
            Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
            Walk_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
            Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
            Walk_Down = [pygame.image.load('mage_f1.gif'),pygame.image.load('mage_f2.gif')]
            Standing = pygame.image.load('mage_f1.gif')
        if spr == "jobb":
            Walk_Left = [pygame.image.load('witch_l1.gif'),pygame.image.load('witch_l2.gif')]
            Walk_Right = [pygame.image.load('witch_r1.gif'),pygame.image.load('witch_r2.gif')]
            Walk_Up = [pygame.image.load('witch_b1.gif'),pygame.image.load('witch_b2.gif')]
            Walk_Down = [pygame.image.load('witch_f1.gif'),pygame.image.load('witch_f2.gif')]
            Standing = pygame.image.load('witch_f1.gif')


        while r:
            win.fill(constans.BLACK)
            win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
            pygame.time.delay(80)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.pos_x > vel :
                self.pos_x -= vel
                win.blit(Walk_Left[walkCount], (self.pos_x,self.pos_y))
                walkCount+=1

            elif keys[pygame.K_RIGHT] and self.pos_x < constans.WIN_X - vel - 20:
                self.pos_x += vel
                win.blit(Walk_Right[walkCount], (self.pos_x,self.pos_y))
                walkCount+=1
            elif keys[pygame.K_UP] and self.pos_y > vel:
                self.pos_y -= vel
                win.blit(Walk_Up[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
            elif keys[pygame.K_DOWN] and self.pos_y < constans.WIN_Y -vel-20:
                self.pos_y += vel
                win.blit(Walk_Down[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
            else:
                win.blit(Standing,(self.pos_x,self.pos_y))

            if walkCount > 1:
                walkCount = 0
            pygame.display.update()



class Hero(Character):


    def cast(pos_x, pos_y, vel, direction, rng, hitmark):


        return 0
