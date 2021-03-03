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
        self.skill = 100
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.current_HP = hp
        self.potion_count = 3
        self.min_deff = deff


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

    def get_current_hp(self):
        return self.current_HP

    def set_current_hp(self, x):
        self.current_HP = x

    def set_hp(self, x):
        self.max_hp = x

    def set_dmg(self, x):
        self.dmg = x

    def set_deff(self, x):
        self.deff = x

    def set_skill(self,x):
        self.skill = x

    def get_potion(self):
        return self.potion_count

    def set_potion(self,x):
        self.potion_count = x

    def set_min_deff(self,x):
        self.min_deff = x

    def get_min_deff(self):
        return self.min_deff

    def Hp_Bar(self,window, left, top,c_hp,max_hp):
        #pygame.draw.rect(screen, color, [left, top, width, height], filled)
        pygame.draw.rect(window,constans.WHITE,(left, top, (max_hp/200)*300+20, 35))
        pygame.draw.rect(window,constans.RED,(left+10, top+5, (c_hp/200)*300, 25))
        pygame.display.update()

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
            if random.randint(0,20) == 1 and stand == False:
                #enemy
                PC = Enemy(random.randint(50,150),random.randint(50,100),random.randint(50,150))
                enemy_sprite = pygame.image.load('rouge.gif') if random.randint(0,1) == 0 else pygame.image.load('knight.gif')
                print("battle")

                #flash effect before battle
                for i in range(2):
                    win.fill(constans.BLACK)
                    pygame.display.update()
                    time.sleep(0.1)
                    win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
                    pygame.display.update()
                    time.sleep(0.1)


                win.fill(constans.BLACK)
                #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
                pygame.draw.rect(win,constans.WHITE,(0, constans.WIN_Y-constans.WIN_Y/4, constans.WIN_X,constans.WIN_Y/4))
                win.blit(pygame.transform.scale(Standing,(80, 100)), (constans.WIN_X-400,80))
                win.blit(pygame.transform.scale(enemy_sprite,(80, 100)), (90,300))
                pygame.display.update()



                fled = None
                fortify = False
                round_counter = 0
                round_counter_enemy = 0
                fortify_enemy = False
                self.set_current_hp(self.get_hp())
                self.set_potion(3)
                #amig a pc nek es az ellensegnek nagyobb a hp mint 0
                while self.get_current_hp() > 0 and PC.get_current_hp() > 0:


                    #my hp bar
                    # Hp_Bar(window, left, top,c_hp,max_hp):
                    self.Hp_Bar(win, 20, 45, self.get_current_hp(),self.get_hp())
                    # enemys hp bar
                    PC.Hp_Bar(win, constans.WIN_X-400, (constans.WIN_Y-constans.WIN_Y/4)-60, PC.get_current_hp(), PC.get_hp())

                    event = pygame.event.wait()

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEMOTION:

                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4) and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+20 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+200 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+70:
                            opening.draw_box(win, constans.ORANGE, (constans.WIN_X/2-constans.WIN_X/4), (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"attack")
                        else:
                            opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4), (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"attack")


                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4) and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+90 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+200 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+140:
                            opening.draw_box(win, constans.ORANGE, (constans.WIN_X/2-constans.WIN_X/4), (constans.WIN_Y/2+constans.WIN_Y/4)+90, 200, 50,"fortify")
                        else:
                            opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4), (constans.WIN_Y/2+constans.WIN_Y/4)+90, 200, 50,"fortify")

                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+20 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+70:
                            opening.draw_box(win, constans.ORANGE, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"use potion ")
                        else:
                            opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"use potion ")
                            opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4)+600, (constans.WIN_Y/2+constans.WIN_Y/4)+20, 50, 50, str(self.get_potion()))


                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+90 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+140:
                            opening.draw_box(win, constans.ORANGE, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+90, 200, 50,"flee")
                        else:
                            opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+90, 200, 50,"flee")


                    if event.type == pygame.MOUSEBUTTONUP:
                        #attack
                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4) and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+20 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+200 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+70:
                            if random.randint(0,4) != 3:
                                PC.set_current_hp(PC.get_current_hp() - self.get_dmg()/10)
                                print("hit")
                            else:
                                print("miss")

                        #fortify
                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4) and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+90 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+200 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+140:
                            fortify = True
                            self.set_deff(self.get_deff()+20)

                        #use potion
                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+20 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+70:
                            if self.get_potion() > 0:
                                self.set_potion(self.get_potion()-1)
                                if self.get_current_hp()+20 > self.get_hp():
                                    self.set_current_hp(self.get_hp())
                                else:
                                    self.set_current_hp(self.get_current_hp()+20)
                            else:
                                print("no more potion available")

                        #flee
                        if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+90 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+140:
                            if random.randint(0,11) == 5:
                                PC.set_current_hp(0)
                                fled = True
                                print("fled")


                        #in-combat passive effect check
                        if fortify == True:
                            #kör számlálás
                            if round_counter > 1:
                                round_counter = 0
                                fortify = False
                                self.set_deff(self.get_min_deff())
                            else:
                                round_counter += 1


                        #röhzitem az action -öket, visszamenőleges keresésre
                        act_list = []
                        #attack
                        if len(act_list) < 1 and PC.get_current_hp() >= PC.get_current_hp()*0.8:
                            self.set_current_hp(self.get_current_hp() - PC.get_dmg()/10)
                            act_list.append("attack")
                        #heal
                        elif PC.get_current_hp() >= PC.get_current_hp()*0.8:
                            PC.set_current_hp(PC.get_current_hp()*0.2)
                            act_list.append("heal")
                        else:
                            fortify_enemy = True
                            PC.set_deff(PC.get_deff()+20)
                            if len(act_list) >= 3:
                                act_list.clear()



                        #in-combat passive effect check for the enemy
                        if fortify_enemy == True:
                            #kör számlálás
                            if round_counter_enemy > 1:
                                round_counter_enemy = 0
                                fortify_enemy = False
                                PC.set_deff(PC.get_min_deff())
                            else:
                                round_counter_enemy += 1
                        print(fortify)
                        print(self.get_deff())
                        print(f"round: {round_counter}")




            pygame.display.update()


class Enemy(Character):
    def __init__(self,hp, dmg, deff):
        self.max_hp = hp
        self.dmg = dmg
        self.deff = deff
        self.current_HP = hp
