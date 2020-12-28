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
        self.skill = 0
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_hp(self):
        return self.hp

    def get_dmg(self):
        return self.dmg

    def get_deff(self):
        return self.deff

    def get_skill(self):
        return self.skill

    def set_hp(self, x):
        self.hp = x

    def set_dmg(self, x):
        self.dmg = x

    def set_deff(self, x):
        self.deff = x

    def set_skill(self,x):
        self.skill = x


class Hero(Character):
    def __init__(self,hp, dmg, deff, pos_x, pos_y):
        super().__init__(hp, dmg, deff, pos_x, pos_y)
        self.name = constans.NAME

    def cast(self,win,pos_x, pos_y, vel, direction):
    #pygame.draw.circle(screen, color, (x, y), radius, thickness)
        not_hit = True
        if direction == "bal":
            while not_hit:
                pos_x = pos_x - vel
                pygame.draw.circle(win,constans.RED,(pos_x,pos_y),5,5)
                if pos_x <= 0:
                    not_hit = False

        if direction == "jobb":
            while not_hit:
                pos_x = pos_x + vel
                pygame.draw.circle(win,constans.RED,(pos_x,pos_y),5,5)
                if pos_x >= constans.WIN_X:
                    not_hit = False

        if direction == "fel":
            while not_hit:
                pos_y = pos_y - vel
                pygame.draw.circle(win,constans.RED,(pos_x,pos_y),5,5)
                if pos_y <= 0:
                    not_hit = False

        if direction == "le":
            while not_hit:
                pos_y = pos_y + vel
                pygame.draw.circle(win,constans.RED,(pos_x,pos_y),5,5)
                if pos_y >= constans.WIN_Y:
                    not_hit = False



    def move(self,win,bg,spr):
        walkCount = 0
        r = True
        left = False
        right = False
        up = False
        down = False
        vel = 10
        last_dir = None

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
                last_dir = "bal"

            elif keys[pygame.K_RIGHT] and self.pos_x < constans.WIN_X - vel - 20:
                self.pos_x += vel
                win.blit(Walk_Right[walkCount], (self.pos_x,self.pos_y))
                walkCount+=1
                last_dir = "jobb"

            elif keys[pygame.K_UP] and self.pos_y > vel:
                self.pos_y -= vel
                win.blit(Walk_Up[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
                last_dir = "fel"

            elif keys[pygame.K_DOWN] and self.pos_y < constans.WIN_Y -vel-20:
                self.pos_y += vel
                win.blit(Walk_Down[walkCount],(self.pos_x,self.pos_y))
                walkCount+=1
                last_dir = "le"

            elif keys[pygame.K_SPACE]:
                #cast(win,pos_x, pos_y, vel, direction):
                self.cast(win,self.get_pos_x()+10,self.get_pos_y()+10,vel,last_dir)
            else:
                if last_dir == "le":
                    win.blit(Standing,(self.pos_x,self.pos_y))
                elif last_dir == "fel":
                    win.blit(Walk_Up[0],(self.pos_x,self.pos_y))
                elif last_dir == "bal":
                    win.blit(Walk_Left[0],(self.pos_x,self.pos_y))
                elif last_dir == "jobb":
                    win.blit(Walk_Right[0],(self.pos_x,self.pos_y))


            if walkCount > 1:
                walkCount = 0
            pygame.display.update()
