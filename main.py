import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE SHOOTER SAGA")
icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
print("test message")