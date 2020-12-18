import pygame,sys,os
import time
import constans
pygame.init()

bg = pygame.image.load(os.path.join('assets','back2.jpg'))

#screen test
def show(win):

#kitölti a hátteret
    win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
    #win.fill(constans.COLOR)
    pygame.display.update()


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



#doboz létre hozása amibe mehet szöveg
def draw_box(window, colour, left, top, width, height,str):
    #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    pygame.draw.rect(window,colour,(left, top, width, height))
    text_show(window, left + width/2, top + height/2,str)
    pygame.display.update()


# kezdő felület
#argumentumok ABLAK || ANNAK A SZINE
def char_selection(win):
    pygame.display.update()
    r = True
    char_exist = None
#végtelen cilusba a klikk ig
    show(win)
    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"hello")
    draw_box(win,constans.BLACK,(constans.WIN_X/3)*2,constans.WIN_Y/3,100,200,"hello")
    while r:
#eventeket kipörgetve, ha klikk akkor, hol és ha jó helyen klikk akkor a box változik
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
#klikkre figyel, visszatér egy string el
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/3 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/3+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,125,200,"megvagy")
                    char_exist = "bal"
                    return char_exist
#egér mozgásra figyel:// HOVER css -be, nem tudom magyarul
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/3 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/3+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.WHITE,constans.WIN_X/3,constans.WIN_Y/3,100,200,"hello")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"hello")
    return char_exist



def welcome(win):

    r = True
    show(win)
    draw_box(win,constans.BLACK,constans.WIN_X/2-100,constans.WIN_Y/3,200,50,"New Game")
    draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*1.5,200,50,"Load Game")
    draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*2,200,50,"Settings")
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+50:
                    draw_box(win,constans.WHITE,constans.WIN_X/2-100,constans.WIN_Y/3,200,50,"New Game")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/2-100,constans.WIN_Y/3,200,50,"New Game")
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+50:
                    char_selection(win)
                    r = False
