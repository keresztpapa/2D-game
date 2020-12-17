import pygame
import time
import constans
pygame.init()

#screen test
def show(win):
    time.sleep(1)
    #kitölti a hátteret
    win.fill(constans.COLOR)
    pygame.display.flip()

#szöveg kiiratás
def text_show(win,x,y,str):
    #Font -- whatever ez magyarul
    font=pygame.font.SysFont('timesnewroman',  30)
    # create a text suface object,
    # on which text is drawn on it.
    text = font.render(str, True, constans.GREEN)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (x, y)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    win.blit(text, textRect)
    pygame.display.update()
    #time.sleep(5)


#doboz létre hozása amibe mehet szöveg
def draw_box(window, colour, left, top, width, height,str):
    #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    pygame.draw.rect(window,colour,(left, top, width, height))
    text_show(window, left + width/2, top + height-180,str)
    pygame.display.update()
#    time.sleep(5)


# kezdő felület
#argumentumok ABLAK || ANNAK A SZINE
def open(win):
    r = True
#végtelen cilusba a klikk ig
    while r:
        show(win)
        draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"hello")
        draw_box(win,constans.BLACK,(constans.WIN_X/3)*2,constans.WIN_Y/3,100,200,"hello")
#eventeket kipörgetve, ha klikk akkor, hol és ha jó helyen klikk akkor a box változik
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/3 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/3+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"megvagy")
                    time.sleep(2)
                    r = False
