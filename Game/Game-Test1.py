import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

Player_width = 62

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Test game')
clock = pygame.time.Clock()



Spriteimg = pygame.image.load('imgs/rightstand1.png')

pygame.draw.rect(gameDisplay, black, (300, 300, 100,100))


def Sprite(x,y):
    gameDisplay.blit(Spriteimg,(x,y))

def game_loop():
    x = (display_width * 0.2)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
       

        Sprite(x,y)
      

        if x > display_width - Player_width or x < 0:
            x

        
        pygame.display.update()
        gameDisplay.fill(white)
        clock.tick(60)

game_loop()
pygame.quit()
quit()