import pygame, sys
import opening
import constans
pygame.init()

#kép init
win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))
#window cím
pygame.display.set_caption(" The Hobblyat ")
#opening screen

print(opening.open(win))


pygame.quit()
sys.exit()


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
