import pygame
import random
pygame.init()


#screen setup
#window  size and is resizable now
screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
pygame.display.set_caption("SPACE SHOOTER SAGA")
icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
playerimg = pygame.image.load('spaceship.png')

# Player Position,Centering the spaceship
spaceshipX = 370
spaceshipY = 520
changeX=0
running=True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    player(playerX, playerY)
    pygame.display.update()