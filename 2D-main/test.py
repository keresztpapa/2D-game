class Chest():
    chest_pic = pygame.image.load(os.path.join('chest.png'))

    def __init__(self,pos_x,pos_y):
            self.pos_x
            self.pos_y

    def chest_show(self,win):
        win.blit(chest_pic, (self.pos_x, self.pos_y)), (0, 0)
        pygame.display.update()



--------------------------------------
print(f"player x:{self.pos_x} \nplayer y: {self.pos_y}")
print(f"player x:{self.pos_x} \nplayer y: {self.pos_y}")
print(f"player x:{self.pos_x} \nplayer y: {self.pos_y}")
print(f"player x:{self.pos_x} \nplayer y: {self.pos_y}")
---------------------------------------
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
                #projectiles
                pass

            else:
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


            if walkCount > 1:
                walkCount = 0
            c.chest_show(win)
            pygame.display.update()


----------------------------------------------------------------------


    for event in pygame.event.get():

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
                opening.draw_box(win, constans.ORANGE, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"use item ")
            else:
                opening.draw_box(win, constans.RED, (constans.WIN_X/2-constans.WIN_X/4)+400, (constans.WIN_Y/2+constans.WIN_Y/4)+20, 200, 50,"use item ")


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

            #use item
            if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+20 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+70:
                pass

            #flee
            if pygame.mouse.get_pos()[0] >= (constans.WIN_X/2-constans.WIN_X/4)+400 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/2+constans.WIN_Y/4)+90 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/2-constans.WIN_X/4)+600 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/2+constans.WIN_Y/4)+140:
                pass










        
