import pygame, sys, time, random

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
        self.max_hp = hp
        self.dmg = dmg
        self.deff = deff
        self.skill = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.current_HP = self.max_hp


    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_hp(self):
        return self.max_hp

    def get_dmg(self):
        return self.dmg

    def get_deff(self):
        return self.deff

    def get_skill(self):
        return self.skill

    def get_current_hp():
        return self.current_HP

    def set_current_hp(x):
        self.current_HP

    def set_hp(self, x):
        self.hp = x

    def set_dmg(self, x):
        self.dmg = x

    def set_deff(self, x):
        self.deff = x

    def set_skill(self,x):
        self.skill = x



    def Hp_Bar(self,window, left, top,hp):
        minus = self.get_hp
        #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        pygame.draw.rect(window,constans.WHITE,(left, top, hp, 25))
        #self.Hp_Bar(win, 0, 0,self.get_hp()*10)

class Hero(Character):
    def __init__(self,hp, dmg, deff, pos_x, pos_y):
        super().__init__(hp, dmg, deff, pos_x, pos_y)
        self.name = constans.NAME


    def action(self,win,bg,spr):

        step = 0
        r = True
        left = False
        right = False
        up = False
        down = False
        vel = 10
        last_dir = None
        stand = None

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

        # CHESS MECHANISM
        #DOESNT WORK YET
        # c = engine.Chest(100,300)
        #
        # def chess_int():
        #     cx = c.get_pos_x()
        #     cy = c.get_pos_y()
        #     sx = self.pos_x
        #     sy = self.pos_y
        #
        #     if cx-40 >= sx and sy >= cy-40 and sx <= cx+40 and sy <= cy+40:
        #         c.chest_show(win,'chest_w_b.png')
        #     else:
        #         c.chest_show(win,'chest.png')

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
                win.blit(Walk_Left[step], (self.pos_x,self.pos_y))
                step+=1
                last_dir = "bal"
                stand = False

            elif keys[pygame.K_RIGHT] and self.pos_x < constans.WIN_X - vel - 20:
                self.pos_x += vel
                win.blit(Walk_Right[step], (self.pos_x,self.pos_y))
                step+=1
                last_dir = "jobb"
                stand = False

            elif keys[pygame.K_UP] and self.pos_y > vel:
                self.pos_y -= vel
                win.blit(Walk_Up[step],(self.pos_x,self.pos_y))
                step+=1
                last_dir = "fel"
                stand = False

            elif keys[pygame.K_DOWN] and self.pos_y < constans.WIN_Y -vel-20:
                self.pos_y += vel
                win.blit(Walk_Down[step],(self.pos_x,self.pos_y))
                step+=1
                last_dir = "le"
                stand = False

            elif keys[pygame.K_SPACE]:
                return False

            else:
                stand = True
                if last_dir == "le":
                    win.blit(Standing,(self.pos_x,self.pos_y))
                elif last_dir == "fel":
                    win.blit(Walk_Up[0],(self.pos_x,self.pos_y))
                elif last_dir == "bal":
                    win.blit(Walk_Left[0],(self.pos_x,self.pos_y))
                elif last_dir == "jobb":
                    win.blit(Walk_Right[0],(self.pos_x,self.pos_y))
                elif last_dir == None:
                    win.blit(Standing,(self.pos_x,self.pos_y))


            if step > 1:
                step = 0
            #harc
            if random.randint(0,9) == 1 and stand == False:
                PC = Enemy(random.randint(0,20),random.randint(0,20),random.randint(0,20))
                print("battle")
                #flash effect before battle

                for i in range(2):
                    win.fill(constans.BLACK)
                    pygame.display.update()
                    time.sleep(0.1)
                    win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
                    pygame.display.update()
                    time.sleep(0.1)

                while self.current_HP > 0 or PC.get_current_hp > 0:
                    win.fill(constans.BLACK)
                    #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
                    pygame.draw.rect(win,constans.GREEN,(0, constans.WIN_Y-constans.WIN_Y/4, constans.WIN_X,constans.WIN_Y/4))
                    opening.draw_box(win, constans.WHITE, constans.WIN_X/2, constans.WIN_Y/2, 50, 50,"helo")


                    pygame.display.update()
                    time.sleep(2)
            #chess_int()

            pygame.display.update()


class Enemy(Character):
    def __init__(self,hp, dmg, deff):
        super().__init__(hp, dmg, deff, pos_x = None, pos_y = None)
