import pygame, sys, time, os

import constans, char
# x = 5
# y = 5
# vel = 1
# r = True
# walkCount = 0
# left = False
# right = False
# up = False
# down = False
# win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))
#
# bg = pygame.image.load(os.path.join('back2.jpg'))
#
# win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
# clock = pygame.time.Clock()
# Walk_Left = [pygame.image.load('mage_l1.gif'),pygame.image.load('mage_l2.gif')]
# Walk_Right = [pygame.image.load('mage_r1.gif'),pygame.image.load('mage_r2.gif')]
# Walk_Up = [pygame.image.load('mage_b1.gif'),pygame.image.load('mage_b2.gif')]
# Walk_Down = [pygame.image.load('mage_f1.gif'),pygame.image.load('mage_f2.gif')]
# Standing = pygame.image.load('mage_f1.gif')
#
# def reDraw():
#     global walkCount
#     win.blit(pygame.transform.scale(bg, (constans.WIN_X, constans.WIN_Y)), (0, 0))
#
#     if walkCount >= 2:
#         walkCount = 0
#
#     if left:
#         win.blit(Walk_Left[walkCount], (x,y))
#         walkCount+=1
#     elif right:
#         win.blit(Walk_Right[walkCount], (x,y))
#         walkCount+=1
#     elif up:
#         win.blit(Walk_Up[walkCount],(x,y))
#         walkCount+=1
#     elif down:
#         win.blit(Walk_Down[walkCount],(x,y))
#         walkCount+=1
#     else:
#         walkCount = 0
#
#     pygame.display.update()
#
#
# while r:
#     pygame.time.delay(80)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             r = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]and x>vel :
#         x -= vel
#         left = True
#         right = False
#     elif keys[pygame.K_RIGHT]and x < constans.WIN_X - vel:
#         x += vel
#         left = False
#         right = True
#     elif keys[pygame.K_UP]:
#         y -= vel
#         up = True
#         down = False
#     elif keys[pygame.K_DOWN]:
#         y += vel
#         up = False
#         down = True
#     else:
#         left = False
#         right = False
#         walkCount = 0
#     reDraw()
win = pygame.display.set_mode((constans.WIN_X, constans.WIN_Y))
pygame.display.set_caption(" The Hobblyat ")

p = char.Character(10,10,10,20,20)

p.move(win)
