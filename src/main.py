import time

import pygame
import random
import math
import numpy
import cv2
from pygame import mixer
def run_game():
    pygame.init()
    mixer.init()

    mixer.music.load("../assets/audios/game_bgm.mp3")  # background game music
    mixer.music.play(-1)
    # screen setup
    # window  size and is resizable now

    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # background video
    video = cv2.VideoCapture("../assets/videos/game_background_video.mp4")
    pygame.display.set_caption("SPACE SHOOTER SAGA")
    icon = pygame.image.load("../assets/images/game_icon.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load('../assets/images/start_screen_background_img.jpg')
    # pygame.display.
    spaceship_img = pygame.image.load('../assets/images/spaceship.png')
    # alien_death_explosion
    alien_soldier_death_img = pygame.image.load("../assets/images/alien_soldier_death_image.png")
    soldier_explosion = []
    # alien_death_explosion
    alien_monster_death_img = pygame.image.load("../assets/images/alien_monster_death_image.png")
    monster_explosion = []
    # boss_alien explosion
    alien_boss_ship_img = pygame.image.load("../assets/images/alien_boss_ship.png")
    scaled_boss_ship_img = pygame.transform.scale(alien_boss_ship_img, (100, 100))
    alien_boss_death_img = pygame.image.load("../assets/images/alien_boss_death_image.png")
    scaled_boss_death_img = pygame.transform.scale(alien_boss_death_img, (100, 100))
    boss_explosion = []
    # soldier aliens
    alien_soldier_img = []
    alien_soldier_position_x = []
    alien_soldier_position_y = []
    alien_soldier_speed_x = [0.5]
    alien_soldier_speed_y = [0.5]
    no_of_aliens = 8
    # octopus_monster_alien
    alien_monster_img = []
    alien_monster_position_x = []
    alien_monster_position_y = []
    alien_monster_speed_x = [1]
    alien_monster_speed_y = [1]
    no_of_monster_aliens = 4
    # boss alien
    alien_boss_img = []
    alien_boss_position_x = []
    alien_boss_position_y = []
    alien_boss_speed_x = [0.5]
    alien_boss_speed_y = [0.5]
    no_of_boss_aliens = 1
    boss_health = 100  # Initial health of the boss
    MAX_BOSS_HEALTH = 100  # Store max health to calculate the width of the health bar
    # game over status
    game_over_flag = False

    font_gameover = pygame.font.SysFont('Arial', 64, 'bold')

    def show_start_screen():
        screen.fill((0, 0, 0))  # Clear screen with black

         # Load and scale background image
        background = pygame.image.load("../assets/images/start_screen_background_img.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize to screen dimensions
        screen.blit(background, (0, 0))


        font = pygame.font.SysFont('Arial', 48, 'bold')
        title_text = font.render("SPACE SHOOTER SAGA", True, (118, 38, 145))
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        button_width, button_height = 200, 60
        button_x, button_y = (WIDTH - button_width) // 2, HEIGHT // 2.3
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        spaceship_top = pygame.image.load("../assets/images/spaceship.png")  # Load the spaceship
        spaceship_top = pygame.transform.scale(spaceship_top, (100, 100))  # Resize if needed
        spaceship_rect = spaceship_top.get_rect(center=(800 // 2, 600 // 5))

        # Button for start the game

        button_font = pygame.font.SysFont('Arial', 36, 'bold')
        button_text = button_font.render("Start Game", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(spaceship_top, spaceship_rect.topleft)
        screen.blit(title_text, title_rect)
        pygame.draw.rect(screen, (255, 255, 0), button_rect)  # Yellow button
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

        # Wait for button click to start the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mouse_x, mouse_y):  # If clicked on button
                        return True



    def draw_boss_health_bar(x, y, health):
        bar_width = 100  # Total width of health bar
        bar_height = 10  # Height of the health bar

        # Calculate the green bar width based on health percentage
        health_percentage = max(health / MAX_BOSS_HEALTH, 0)  # Prevent negative values
        green_bar_width = int(bar_width * health_percentage)

        # Draw the red background bar
        pygame.draw.rect(screen, (255, 0, 0), (x, y - 20, bar_width, bar_height))

        # Draw the green health portion
        pygame.draw.rect(screen, (0, 255, 0), (x, y - 20, green_bar_width, bar_height))



    font_gameover = pygame.font.Font(None, 150)  # Large bold font for "GAME OVER"
    font_score = pygame.font.Font(None, 50)  # ✅ Defined before use
    font_button = pygame.font.Font(None, 40)



    def gameover():
        global game_over_flag


        # Clear the screen first
        screen.fill((0, 0, 0))

        # Load and display background
        background = pygame.image.load("../assets/images/game_over_bg_img.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize to screen dimensions
        screen.blit(background, (0, 0))  # Now blit after clearing the screen

        game_over_flag = True
        mixer.music.load("../assets/audios/gameover_bgm.mp3")  # Play game over music
        mixer.music.play(-1)

        # Display GAME OVER text
        img_gameover = font_gameover.render("GAME OVER", True, (255, 255, 255))  # Orange color
        screen.blit(img_gameover, (WIDTH//2 - img_gameover.get_width()//2, HEIGHT//3))

        # Display obtained score
        score_text = font_score.render(f"Score: {score}", True, (255, 255, 0))  # Yellow
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//5))

        # Restart button
        button_width, button_height = 200, 60
        button_x, button_y = (WIDTH - button_width) // 2, HEIGHT // 1.6

        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, (200, 0, 0), button_rect, border_radius=10)  # Red button with rounded corners
        # Button glow effect
        pygame.draw.rect(screen, (255, 50, 50), button_rect, 3, border_radius=10)
        button_text = font_button.render("Restart", True, (255, 255, 255))
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

        pygame.display.update()  # Ensure updates are reflected on the screen

        # Wait for player input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mouse_x, mouse_y):  # Restart the game

                        restart_game()
                        return  # Exit the gameover function


    for i in range(no_of_aliens):  # display multiple aliens
        alien_soldier_img.append(pygame.image.load('../assets/images/alien_solider_ship.png'))
        alien_soldier_position_x.append(random.randint(0, 736))
        alien_soldier_position_y.append(random.randint(30, 150))
        alien_soldier_speed_x.append(0.20)  # alien speed
        alien_soldier_speed_y.append(40)
    for i in range(no_of_monster_aliens):  # display multiple monster_aliens
        alien_monster_img.append(pygame.image.load('../assets/images/alien_monster_image.png'))
        alien_monster_position_x.append(random.randint(0, 736))
        alien_monster_position_y.append(random.randint(30, 150))
        alien_monster_speed_x.append(2.5)  # alien monster speed
        alien_monster_speed_y.append(40)
    for i in range(no_of_boss_aliens):  # display boss alien
        alien_boss_img.append(scaled_boss_ship_img)
        alien_boss_position_x.append(random.randint(0, 736))
        alien_boss_position_y.append(random.randint(30, 150))
        alien_boss_speed_x.append(2.5)  # alien monster speed
        alien_boss_speed_y.append(40)
    score = 0

    # Player Position,Centering the spaceship
    spaceshipX = 370
    spaceshipY = 520
    changeX = 0
    # Bullet position
    bullet_img = pygame.image.load('../assets/images/spaceship_laser.png')
    bullets = []
    bullet_speed = -2.5


    font = pygame.font.SysFont('Arial', 32, 'bold')


    def restart_game():
        run_game()
        #  Reset game variables to restart the game
        # global game_over_flag, score, spaceshipX, spaceshipY, bullets, alien_soldier_position_x, alien_soldier_position_y
        # # global no_of_boss_aliens, alien_boss_position_x, alien_boss_position_y, alien_boss_speed_x, alien_boss_speed_y
        # # global boss_health
        # game_over_flag = False
        # score = 0
        # spaceshipX = 370
        # spaceshipY = 520
        # bullets = []
        # # # Reset boss aliens
        # # no_of_boss_aliens = 1 # Remove existing boss aliens
        # # alien_boss_position_x= [random.randint(0,736)]
        # # alien_boss_position_y = [random.randint(30,150)]
        # # alien_boss_speed_x = [2.5]
        # # alien_boss_speed_y = [40]
        # # boss_health = 100  # Reset boss health
        # # Reset alien positions
        # for i in range(no_of_aliens):
        #     alien_soldier_position_x[i] = random.randint(0, 736)
        #     alien_soldier_position_y[i] = random.randint(30, 150)
        #
        # # for i in range(no_of_boss_aliens):
        # #     alien_boss_position_x[i] = random.randint(0, 736)
        # #     alien_boss_position_y[i] = random.randint(30, 150)
        # mixer.music.load("../assets/audios/game_bgm.mp3")  # Restart background music
        # mixer.music.play(-1)


    def display_score():  # defining function for showing score
        img = font.render(f'score:{score}', True, 'white')
        screen.blit(img, (10, 10))

    if show_start_screen():
        running = True
    while running:
        if not game_over_flag:
            screen.blit(background, (0, 0))
            # display background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # to close the window
                running = False
            if event.type == pygame.KEYDOWN:  # when a key is pressed
                if event.key == pygame.K_F11:  # for fullscreen mode
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:  # for default mode
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
            if event.type == pygame.KEYDOWN:  # when a key is pressed
                if event.key in [pygame.K_LEFT, pygame.K_a]:  # ship moves left with the left key
                    changeX = -2.5
                if event.key in [pygame.K_RIGHT, pygame.K_d]:  # ship moves right with the right key
                    changeX = 2.5
                if event.key == pygame.K_SPACE and not game_over_flag:
                    laser_sound = mixer.Sound("../assets/audios/spaceship_laser_bgm.mp3")  # laser sound effect
                    laser_sound.play()
                    bullets.append([spaceshipX + 16, spaceshipY])  # shooting bullets

            if event.type == pygame.KEYUP:  # when a key is released, no change in position
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d, ]:
                    changeX = 0
        read_frame_status, frame = video.read()  # checks and returns if a frame is read and its contents
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
            spaceshipX += changeX  # reflect the change
            if (spaceshipX <= 0):  # prevent it from going out of screen from left
                spaceshipX = 0
            elif (spaceshipX >= 736):  # prevent it from going out of screen from right
                spaceshipX = 736
            # alien_soldiers_movement and display
            for i in range(no_of_aliens):
                if alien_soldier_position_y[i] > 470:
                    gameover()

                    for j in range(no_of_aliens):
                        alien_soldier_position_y[j] = 2000  # to disappear the alien when game get over
                    break
                alien_soldier_position_x[i] += alien_soldier_speed_x[i]
                if alien_soldier_position_x[i] <= 0:
                    alien_soldier_speed_x[i] = 1
                    alien_soldier_position_y[i] += alien_soldier_speed_y[i]  # alien moves downwards when it touches edge
                elif alien_soldier_position_x[i] >= 736:
                    alien_soldier_speed_x[i] = -1
                    alien_soldier_position_y[i] += alien_soldier_speed_y[i]  # alien moves downwards when it touches edge

                screen.blit(alien_soldier_img[i],
                            (alien_soldier_position_x[i], alien_soldier_position_y[i]))  # display soldier alien
            if (score > 10):
                # alien_monsters display and movement
                for i in range(no_of_monster_aliens):
                    if alien_monster_position_y[i] > 470:
                        gameover()

                        for j in range(no_of_monster_aliens):
                            alien_monster_position_y[j] = 2000  # to disappear the alien when game get over
                        break
                    alien_monster_position_x[i] += alien_monster_speed_x[i]
                    if alien_monster_position_x[i] <= 0:
                        alien_monster_speed_x[i] = 2
                        alien_monster_position_y[i] += alien_monster_speed_y[
                            i]  # alien moves downwards when it touches edge
                    elif alien_monster_position_x[i] >= 736:
                        alien_monster_speed_x[i] = -2
                        alien_monster_position_y[i] += alien_monster_speed_y[
                            i]  # alien moves downwards when it touches edge

                    screen.blit(alien_monster_img[i],
                                (alien_monster_position_x[i], alien_monster_position_y[i]))  # display soldier alien
            # boss aliens display and movement
            if (score > 20):

                for i in range(no_of_boss_aliens):
                    if alien_boss_position_y[i] > 470:
                        gameover()





                        for j in range(no_of_boss_aliens):
                            alien_boss_position_y[j] = 2000  # to disappear the alien when game get over
                        break
                    alien_boss_position_y[i] += alien_boss_speed_y[i]
                    alien_boss_position_x[i] += alien_boss_speed_x[i]
                    if alien_boss_position_x[i] <= 0:
                        alien_boss_speed_x[i] = 2
                        # alien_boss_position_y[i] += alien_boss_speed_y[i]  # alien moves downwards when it touches edge
                    elif alien_boss_position_x[i] >= 700:
                        alien_boss_speed_x[i] = -2
                        # alien_boss_position_y[i] += alien_boss_speed_y[i]  # alien moves downwards when it touches edge

                    screen.blit(alien_boss_img[i],
                                (alien_boss_position_x[i], alien_boss_position_y[i]))  # display soldier alien
                    draw_boss_health_bar(alien_boss_position_x[i], alien_boss_position_y[i], boss_health)

            # fired bullets/lasers from spaceship
            for bullet in bullets[:]:
                bullet[1] += bullet_speed
                if bullet[1] < 0:
                    bullets.remove(bullet)

            for bullet in bullets[:]:  # create multiple bullet at same time
                for i in range(no_of_aliens):  # if bullet hit alien_soldiers
                    distance = math.sqrt(math.pow(bullet[0] - alien_soldier_position_x[i], 2) + math.pow(
                        bullet[1] - alien_soldier_position_y[i], 2))
                    if distance < 27:
                        alien_soldier_death_sound = mixer.Sound("../assets/audios/alien_death_bgm.mp3")  # alien_soldier_death sound effect
                        alien_soldier_death_sound.play()

                        soldier_explosion.append((alien_soldier_position_x[i], alien_soldier_position_y[i],
                                                  time.time()))  # adds explosion placeholders
                        # ie alien death
                        try:
                            bullets.remove(bullet)
                        except ValueError:
                            pass
                        alien_soldier_position_x[i] = random.randint(0, 736)
                        alien_soldier_position_y[i] = random.randint(30, 150)
                        score += 1
                        break  # a bullet checked for hitting multiple aliens,breaks loop if one alien is hit
                if (score > 10):
                    for j in range(no_of_monster_aliens):  # if bullet hit  alien_monsters
                        distance = math.sqrt(math.pow(bullet[0] - alien_monster_position_x[j], 2) + math.pow(
                            bullet[1] - alien_monster_position_y[j], 2))
                        if distance < 27:
                            alien_monster_death_sound = mixer.Sound(
                                "../assets/audios/alien_monster_death_bgm.mp3")  # alien_soldier_death sound effect
                            alien_monster_death_sound.play()

                            monster_explosion.append((alien_monster_position_x[j], alien_monster_position_y[j],
                                                      time.time()))  # adds explosion placeholders
                            # ie monster death
                            try:
                                bullets.remove(bullet)
                            except ValueError:
                                pass
                            alien_monster_position_x[j] = random.randint(0, 736)
                            alien_monster_position_y[j] = random.randint(30, 150)
                            score += 2
                            break  # a bullet checked for hitting multiple monsters,breaks loop if one alien is hit
                if (score > 20 or score > 40 or score > 60 or score > 80 or score > 100):
                    for k in range(no_of_boss_aliens):  # if bullet hit  alien_monsters
                        distance = math.sqrt(math.pow(bullet[0] - alien_boss_position_x[k], 2) + math.pow(
                            bullet[1] - alien_boss_position_y[k], 2))
                        if distance < 27:
                            try:
                                bullets.remove(bullet)
                            except ValueError:
                                pass

                            boss_health -= 10  # Reduce boss health when hit

                            # If boss health reaches zero, remove it and reset position
                            if boss_health <= 0:

                                boss_explosion.append((alien_boss_position_x[k], alien_boss_position_y[k], time.time()))
                                alien_boss_death_sound = mixer.Sound("../assets/audios/alien_boss_death_bgm.mp3")
                                alien_boss_death_sound.play()
                                alien_boss_position_x[k] = random.randint(0, 736)
                                alien_boss_position_y[k] = random.randint(30, 150)
                                boss_health = 100  # Reset health for next boss
                                score += 10  # Bonus points for killing the boss
            current_time = time.time()
            # alien explosion
            soldier_explosion = [(x, y, t) for x, y, t in soldier_explosion if
                                 current_time - t < 0.5]  # Show for 0.5 seconds and keeps new deletes
            # older explosion placeholders ie alien death
            for x, y, _ in soldier_explosion:  # t is not needed as we need to draw here just
                screen.blit(alien_soldier_death_img, (x, y))
            if (score > 10):
                # monster explosion
                monster_explosion = [(x, y, t) for x, y, t in monster_explosion if
                                     current_time - t < 0.5]  # Show for 0.5 seconds and keeps new deletes
                # older explosion placeholders ie alien death
                for x, y, _ in monster_explosion:  # t is not needed as we need to draw here just
                    screen.blit(alien_monster_death_img, (x, y))
            if (score > 20):
                # boss explosion
                boss_explosion = [(x, y, t) for x, y, t in boss_explosion if
                                  current_time - t < 0.5]  # Show for 0.5 seconds and keeps new deletes
                # older explosion placeholders ie alien death
                for x, y, _ in boss_explosion:  # t is not needed as we need to draw here just
                    screen.blit(scaled_boss_death_img, (x, y))
            # append bullets
            for bullet in bullets:
                screen.blit(bullet_img, (bullet[0], bullet[1]))
        if not game_over_flag:
            screen.blit(spaceship_img, (spaceshipX, spaceshipY))  # display ship
            display_score()

        pygame.display.update()  # update the change
    video.release()
run_game()