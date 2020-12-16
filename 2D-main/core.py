import pygame
import opening
import constans
pygame.init()

#kép init
win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))
#window cím
pygame.display.set_caption(" The Hobblyat ")

opening.show(win)
#opening.text_show(win,constans.WIN_X/3,constans.WIN_Y/2,"helo 1/3")
#opening.text_show(win,(constans.WIN_X/3)*2,constans.WIN_Y/2,"helo 2/3")
opening.draw_box(win,constans.BLACK,constans.WIN_X/3,constans.WIN_Y/3,100,200,"hello")
opening.draw_box(win,constans.BLACK,(constans.WIN_X/3)*2,constans.WIN_Y/3,100,200,"hello")




def play():
	r = True
	while r:
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				r = False


		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
			r = False


		pygame.display.update()
	pygame.quit
	quit()
