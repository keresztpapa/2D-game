import pygame, sys, time

import engine
import char
import opening
import game
import constans
pygame.init()

#kép init
win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))

#window cím
pygame.display.set_caption(" The Hobblyat ")

#opening screen

screen = opening.welcome(win)
if screen == "new_game":
	char_spr = opening.char_selection(win)
	char_stat = opening.stats(win)
	print(game.phase_1(win,char_spr,char_stat))
if screen == "load_game":
	pass
if screen == "settings":
	pass

pygame.quit()
sys.exit()



def play():
	while r:
	    pygame.time.delay(10)
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            r = False
	    keys = pygame.key.get_pressed()
	    if keys[pygame.K_LEFT]:
	        x -= vel
	    if keys[pygame.K_RIGHT]:
	        x += vel
	    if keys[pygame.K_UP]:
	        y -= vel
	    if keys[pygame.K_DOWN]:
	        y += vel

	    pygame.draw.rect(win,constans.COLOR,(x,y,20,20))
	    pygame.display.update()
