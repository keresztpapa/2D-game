import pygame,sys,os,time

import char
import game
import constans
pygame.init()

bg = pygame.image.load(os.path.join('back2.jpg'))


#screen test
def show(win):

#kitölti a hátteret
    win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
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
    #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], str)
    pygame.draw.rect(window,colour,(left, top, width, height))
    text_show(window, left + width/2, top + height/2,str)
    pygame.display.update()



#ez nyitja a programot
def welcome(win):

    r = True
    show(win)
    #draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*1.5,200,50,"Load Game")
    #draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*2,200,50,"Settings")

    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
            if event.type == pygame.MOUSEMOTION:

                #new game gomb
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+50:
                    draw_box(win,constans.WHITE,constans.WIN_X/2-100,constans.WIN_Y/3,200,50,"New Game")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/2-100,constans.WIN_Y/3,200,50,"New Game")

                #load game gomb
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/3)*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/3)*1.5+50:
                    draw_box(win,constans.WHITE,constans.WIN_X/2-100,(constans.WIN_Y/3)*1.5,200,50,"Load Game")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*1.5,200,50,"Load Game")

                #setting gomb
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/3)*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/3)*2+50:
                    draw_box(win,constans.WHITE,constans.WIN_X/2-100,(constans.WIN_Y/3)*2,200,50,"Settings")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/2-100,(constans.WIN_Y/3)*2,200,50,"Settings")


            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+50:
                    return "new_game"
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/3)*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/3)*1.5+50:
                    return "load_game"
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/2-100 and pygame.mouse.get_pos()[1] >= (constans.WIN_Y/3)*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/2+100 and pygame.mouse.get_pos()[1]<=(constans.WIN_Y/3)*2+50:
                    return "settings"

#karakter választó felület (2box ------ 1 működik)
#argumentumok ABLAK || ANNAK A SZINE
def char_selection(win):

    r = True
    char_exist = None
#végtelen cilusba a klikk ig
    show(win)

    while r:
#eventeket kipörgetve, ha klikk akkor, hol és ha jó helyen klikk akkor a box változik
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
#klikkre figyel, visszatér egy string el
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/3 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/3+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,125,200,"bal")
                    char_exist = "bal"
                    return char_exist

                if pygame.mouse.get_pos()[0] >= (constans.WIN_X/3)*2 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/3)*2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.BLACK,(constans.WIN_X/3)*2,constans.WIN_Y/3,125,200,"jobb")
                    char_exist = "jobb"
                    return char_exist

#egér mozgásra figyel:// HOVER css -be, nem tudom magyarul
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/3 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/3+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.WHITE,constans.WIN_X/3,constans.WIN_Y/3,100,200,"bal")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"bal")

                if pygame.mouse.get_pos()[0] >= (constans.WIN_X/3)*2 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= (constans.WIN_X/3)*2+100 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+200:
                    draw_box(win,constans.WHITE,(constans.WIN_X/3)*2,constans.WIN_Y/3,125,200,"jobb")
                else:
                    draw_box(win,constans.BLACK,(constans.WIN_X/3)*2,constans.WIN_Y/3,125,200,"jobb")
    return char_exist


def stats(win):
    show(win)
    r = True
    player = char.Hero(50,50,50,pos_x=80,pos_y=250)
    while r:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
            if event.type == pygame.MOUSEMOTION:
                #hp blokk
                # -- HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5-75,constans.WIN_Y/3,50,100," - ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5-75,constans.WIN_Y/3,50,100," - ")

                # HP HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+200 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5,constans.WIN_Y/3,200,100," HP ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5,constans.WIN_Y/3,200,100," HP ")

                # ++ HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5+225,constans.WIN_Y/3,50,100," + ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5+225,constans.WIN_Y/3,50,100," + ")


                #DMG BLOKK
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*1.5+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5-75,constans.WIN_Y/3*1.5,50,100," - ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5-75,constans.WIN_Y/3*1.5,50,100," - ")

                # HP HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+200 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*1.5+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5,constans.WIN_Y/3*1.5,200,100," DMG ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5,constans.WIN_Y/3*1.5,200,100," DMG ")

                # ++ HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*1.5+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5+225,constans.WIN_Y/3*1.5,50,100," + ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5+225,constans.WIN_Y/3*1.5,50,100," + ")


                #deff
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*2+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5-75,constans.WIN_Y/3*2,50,100," - ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5-75,constans.WIN_Y/3*2,50,100," - ")


                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+200 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*2+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5,constans.WIN_Y/3*2,200,100," DEFF ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5,constans.WIN_Y/3*2,200,100," DEFF ")

                # ++ HOVER
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*2+100:
                    draw_box(win,constans.WHITE,constans.WIN_X/5+225,constans.WIN_Y/3*2,50,100," + ")
                else:
                    draw_box(win,constans.BLACK,constans.WIN_X/5+225,constans.WIN_Y/3*2,50,100," + ")


            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+100:
                    #HP--
                    print("hp-")
                    player.set_hp(player.get_hp()-10)
                    player.set_skill(player.get_skill()+10)
                    pass
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3+100:
                    #hp++
                    print("hp+")
                    player.set_hp(player.get_hp()+10)
                    player.set_skill(player.get_skill()-10)
                    pass

                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*1.5+100:
                    #dmg--
                    print("dmg-")
                    player.set_dmg(player.get_dmg()-10)
                    player.set_skill(player.get_skill()+10)
                    pass
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*1.5 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*1.5+100:
                    #dmg++
                    print("dmg+")
                    player.set_dmg(player.get_dmg()+10)
                    player.set_skill(player.get_skill()-10)
                    pass

                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5-75 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5-25 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*2+100:
                    #deff--
                    print("deff-")
                    player.set_deff(player.get_deff()-10)
                    player.set_skill(player.get_skill()+10)
                    pass
                if pygame.mouse.get_pos()[0] >= constans.WIN_X/5+225 and pygame.mouse.get_pos()[1] >= constans.WIN_Y/3*2 and pygame.mouse.get_pos()[0] <= constans.WIN_X/5+275 and pygame.mouse.get_pos()[1]<=constans.WIN_Y/3*2+100:
                    #deff++
                    print("deff+")
                    player.set_deff(player.get_deff()+10)
                    player.set_skill(player.get_skill()-10)
                    pass
            if(player.get_skill() == 0):
                return player

            #a stat- értékek kiiratása
            draw_box(win,constans.BLACK,constans.WIN_X/5,constans.WIN_Y/3-100,250,50,"Remaining points:")
            draw_box(win,constans.BLACK,constans.WIN_X/5+300,constans.WIN_Y/3-100,40,50,str(player.get_skill()))
            draw_box(win,constans.BLACK,constans.WIN_X/5+300,constans.WIN_Y/3,40,100,str(player.get_hp()))
            draw_box(win,constans.BLACK,constans.WIN_X/5+300,constans.WIN_Y/3*1.5,40,100,str(player.get_dmg()))
            draw_box(win,constans.BLACK,constans.WIN_X/5+300,constans.WIN_Y/3*2,40,100, str(player.get_deff()))

    time.sleep(1)



    return 0
