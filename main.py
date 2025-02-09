import pygame
pygame.init()


#screen setup
#window  size and is resizable now
screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
pygame.display.set_caption("SPACE SHOOTER SAGA")
icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
# pygame.display.
player_img = pygame.image.load('spaceship.png')

# Player Position,Centering the spaceship
playerX = 370
playerY = 520

running=True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background, (0, 0))
    screen.blit(player_img,(playerX, playerY))
    pygame.display.update()
