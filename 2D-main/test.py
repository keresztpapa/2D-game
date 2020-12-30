class Chest():
    chest_pic = pygame.image.load(os.path.join('chest.png'))

    def __init__(self,pos_x,pos_y):
            self.pos_x
            self.pos_y

    def chest_show(self,win):
        win.blit(chest_pic, (self.pos_x, self.pos_y)), (0, 0)
        pygame.display.update()
