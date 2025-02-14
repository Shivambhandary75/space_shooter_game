import pygame
import random
import cv2
import numpy
pygame.init()


#screen setup
#window  size and is resizable now
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#background video
video=cv2.VideoCapture("game_background_video.mp4")
pygame.display.set_caption("SPACE SHOOTER SAGA")
icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
# background = pygame.image.load('background.jpg')
# pygame.display.
spaceship_img = pygame.image.load('spaceship.png')
#soldier aliens
alien_soldier_img = pygame.image.load('alien_solider_ship.png')
alien_soldier_position_x=random.randint(0,736)
alien_soldier_position_y=random.randint(30,150)
alien_soldier_speed_x=1# alien soldier speed
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
            if event.key == pygame.K_F11:#for fullscreen mode
                screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
            if event.key==pygame.K_ESCAPE:#for default mode
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            if event.key in [pygame.K_LEFT,pygame.K_a]: # ship moves left withe left key
                changeX = -2
            if event.key in [pygame.K_RIGHT,pygame.K_d] : # ship moves right  with right  key
                changeX = 2
        if event.type==pygame.KEYUP:#when a key is released  no change is position stay there
            changeX=0
    spaceshipX+=changeX#reflect the change
    if(spaceshipX<=0): #prevent it from going out of screen from left
        spaceshipX=0
    elif (spaceshipX >= 736):  # prevent it from going out of screen from right
        spaceshipX = 736
    alien_soldier_position_x+=alien_soldier_speed_x
    if alien_soldier_position_x<=0:
        alien_soldier_speed_x=1
    elif alien_soldier_position_x>=736:
        alien_soldier_speed_x=-1
    read_frame_status, frame = video.read()#checks and returns if a frame is read and its contents
    if not read_frame_status:  # If video reaches the end
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart from the beginning
        read_frame_status, frame = video.read()  # Read the first frame again
    # Convert OpenCV frame (BGR to RGB)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (WIDTH, HEIGHT))  # Resize to fit screen
    frame = numpy.rot90(frame)  # Rotate if needed
    frame = pygame.surfarray.make_surface(frame)  # Convert to Pygame surface
    screen.blit(frame, (0, 0))

    # screen.blit(background, (0, 0))
    #diplay bg
    screen.blit(spaceship_img,(spaceshipX, spaceshipY))#display ship
    screen.blit( alien_soldier_img, (alien_soldier_position_x,alien_soldier_position_y))#display soldier aline
    pygame.display.update()#update the change
video.release()