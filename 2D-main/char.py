import pygame, sys

import opening
import game
import constans
pygame.init()

class Character():

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

    def move(self,win,bg):
        r = True
        left = False
        right = False
        up = False
        down = False
        vel = 10

        def reDraw(win,bg):
            #sprites
            Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
            Walk_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
            Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
            Walk_Down = [pygame.image.load('mage_f1.gif'),pygame.image.load('mage_f2.gif')]
            Standing = pygame.image.load('mage_f1.gif')
            win.fill(constans.BLACK)
            win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
            walkCount = 0
            if walkCount >= 2:
                walkCount = 0
            if left:
                win.blit(Walk_Left[walkCount], (self.pos_x,self.pos_y))
                walkCount+=1
            elif right:
                win.blit(Walk_Right[walkCount], (self.pos_x,self.pos_y))
                walkCount+=1
            elif up:
                win.blit(Walk_Up[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
            elif down:
                win.blit(Walk_Down[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
            else:
                walkCount = 0
            pygame.display.update()

        while r:
            pygame.time.delay(80)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]and self.pos_x > vel :
                self.pos_x -= vel
                left = True
                right = False
            elif keys[pygame.K_RIGHT]and self.pos_x < constans.WIN_X - vel:
                self.pos_x += vel
                left = False
                right = True
            elif keys[pygame.K_UP]:
                self.pos_y -= vel
                up = True
                down = False
            elif keys[pygame.K_DOWN]:
                self.pos_y += vel
                up = False
                down = True
            else:
                left = False
                right = False
            reDraw(win,bg)
