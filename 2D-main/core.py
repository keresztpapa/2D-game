import pygame
import os
pygame.init()


win = pygame.display.set_mode((900, 640))
pygame.display.set_caption("{set_caption}")


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