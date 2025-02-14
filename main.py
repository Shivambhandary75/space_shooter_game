import pygame
import random
import math
import numpy
import cv2
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
background = pygame.image.load('background.jpg')
# pygame.display.
spaceship_img = pygame.image.load('spaceship.png')

#soldier aliens
alien_soldier_img = []
alien_soldier_position_x = []
alien_soldier_position_y = []
alien_soldier_speed_x = [0.5]
alien_soldier_speed_y = [0.5]

no_of_aliens = 7

game_over_flag = False

font_gameover = pygame.font.SysFont('Arial', 64, 'bold')

def gameover():
    global game_over_flag
    game_over_flag = True
    screen.fill((0, 0, 0))  # Clear the screen before displaying game over
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (220, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()
    
for i in range(no_of_aliens):  #display multiple aliens
    alien_soldier_img.append(pygame.image.load('alien_solider_ship.png'))
    alien_soldier_position_x.append(random.randint(0,736))
    alien_soldier_position_y.append(random.randint(30,150))
    alien_soldier_speed_x.append(0.20)  # alien speed
    alien_soldier_speed_y.append(40)

score=0

# Player Position,Centering the spaceship
spaceshipX = 370
spaceshipY = 520
changeX=0
# Bullet position
bullet_img = pygame.image.load('spaceship_laser.png')
bullets = []
bullet_speed = -2.5

running=True

font = pygame.font.SysFont('Arial',32,'bold')

def display_score():  #defining function for showing score
  img = font.render(f'score:{score}',True,'white')
  screen.blit(img,(10,10))
   
while running:
    if not game_over_flag:
        screen.blit(background, (0, 0))
        #display background
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #to close the window
            running=False
        if event.type == pygame.KEYDOWN:  # when a key is pressed
            if event.key == pygame.K_F11:  # for fullscreen mode
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
            if event.key == pygame.K_ESCAPE:  # for default mode
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
        if event.type==pygame.KEYDOWN: # when a key is pressed
            if event.key in [pygame.K_LEFT,pygame.K_a]: # ship moves left with the left key
                changeX = -2.5
            if event.key in [pygame.K_RIGHT,pygame.K_d]: # ship moves right with the right key
                changeX = 2.5
            if event.key == pygame.K_SPACE and not game_over_flag:
                bullets.append([spaceshipX + 16, spaceshipY])
        
        if event.type==pygame.KEYUP:#when a key is released, no change in position
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_a,pygame.K_d,]:
                changeX=0
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
    if not game_over_flag:
        spaceshipX+=changeX#reflect the change
        if(spaceshipX<=0): #prevent it from going out of screen from left
            spaceshipX=0
        elif (spaceshipX >= 736):  # prevent it from going out of screen from right
            spaceshipX = 736
        
        for i in range(no_of_aliens):
            if alien_soldier_position_y[i] > 420:
                gameover()

                for j in range(no_of_aliens):
                    alien_soldier_position_y[j] = 2000                #to disappear the alien when game get over
                break   
            alien_soldier_position_x[i]+=alien_soldier_speed_x[i]
            if alien_soldier_position_x[i]<=0:
                alien_soldier_speed_x[i]=1
                alien_soldier_position_y[i]+=alien_soldier_speed_y[i]  #alien moves downwards when it touches edge
            elif alien_soldier_position_x[i]>=736:
                alien_soldier_speed_x[i]=-1
                alien_soldier_position_y[i]+=alien_soldier_speed_y[i]  #alien moves downwards when it touches edge
            
            screen.blit(alien_soldier_img[i], (alien_soldier_position_x[i],alien_soldier_position_y[i]))#display soldier alien
        
        for bullet in bullets[:]:
            bullet[1] += bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)
        
        for bullet in bullets[:]:  #create multiple bullet at same time
            for i in range(no_of_aliens):
                distance = math.sqrt(math.pow(bullet[0] - alien_soldier_position_x[i],2) + math.pow(bullet[1] - alien_soldier_position_y[i],2))
                if distance <27:
                    bullets.remove(bullet)
                    alien_soldier_position_x[i]=random.randint(0,736)
                    alien_soldier_position_y[i]=random.randint(30,150)
                    score+=1
                    break  
            
        for bullet in bullets:
            screen.blit(bullet_img, (bullet[0], bullet[1]))
    
    if not game_over_flag:
        screen.blit(spaceship_img,(spaceshipX, spaceshipY))#display ship
        display_score()
    
    pygame.display.update()#update the change
video.release()