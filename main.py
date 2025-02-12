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
spaceship_img = pygame.image.load('spaceship.png')

# Player Position,Centering the spaceship
spaceshipX = 370
spaceshipY = 520
changeX=0
running=True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT: #to close the window
            running=False
        if event.type==pygame.KEYDOWN: # when a key is pressed
            if event.key == pygame.K_LEFT: # ship moves left withe left key
                changeX = -0.5
            if event.key == pygame.K_RIGHT: # ship moves right  with right  key
                changeX = 1
        if event.type==pygame.KEYUP:#when a key is released  no change is position stay there
            changeX=0

    spaceshipX+=changeX#reflect the change
    if(spaceshipX<=0): #prevent it from going out of screen from left
        spaceshipX=0
    elif (spaceshipX >= 736):  # prevent it from going out of screen from right
        spaceshipX = 736

    screen.blit(background, (0, 0))#diplay bg
    screen.blit(spaceship_img,(spaceshipX, spaceshipY))#display ship
    pygame.display.update()#update the change
