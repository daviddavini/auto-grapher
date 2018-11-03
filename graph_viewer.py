import pygame
from pygame.locals import*

white = (255, 64, 64)
w = 780
h = 780
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = True

power = 2
mod = 1

img = pygame.image.load('graph_pics/tetration/'+str(power)+"m"+str(mod)+".jpg")

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                power = max(1, power-1)
            if event.key == pygame.K_RIGHT:
                power += 1
            if event.key == pygame.K_UP:
                mod = max(1, mod-1)
            if event.key == pygame.K_DOWN:
                mod += 1
            try:
                img = pygame.image.load('graph_pics/'+str(power)+"_"+str(mod)+".jpg")
            except:
                img = pygame.image.load("graph_pics/default.jpg")
    screen.blit(img,(0,0))
    pygame.display.update()

