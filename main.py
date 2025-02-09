import pygame
pygame.init()


#screen setup
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE SHOOTER SAGA")
icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
playerimg = pygame.image.load('spaceship.png')

# Player Position,Centering the spaceship
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerimg,(x, y))

running=True
while running:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    player(playerX, playerY)
    pygame.display.update()