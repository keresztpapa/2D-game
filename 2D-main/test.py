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
