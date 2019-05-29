import pygame, random, Player1
from Shooting import Projectile
from Player1 import Player
from Enemies import Mob
from random import randint
import os, sys

pygame.init()

#The code below sets up the window size also providing the win with a variable
win = pygame.display.set_mode((500,500))
#Gives a title for my game.
pygame.display.set_caption("Dungeon Crawler")

bg = pygame.image.load('imgs/BasicBG.png')

#The code below is for the clock. This allows me to set the FPS for the game etc.
clock = pygame.time.Clock()

bulletSound1 = pygame.mixer.Sound("Sounds/Pew.wav")
hitSound = pygame.mixer.Sound("Sounds/bruh.wav")

music = pygame.mixer.music.load("Sounds/Music2.mp3")
pygame.mixer.music.play(-1)
score = 0

#Used as variables for boundrys etc
screenwidth = 500
screenheight = 500

#class defining all stuff to do with player

#Projectiles class


#drawing the game window and sprites etc on the window
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = scoreFont.render("Score:" + str(score),1, (255,255,255))
    win.blit(text,(10,10))
    Zombie.draw(win)
    for bullet in LRbullets:
        bullet.draw(win)
    
    for bullet in UDbullets:
        bullet.draw(win)
    cowboy.draw(win)

    pygame.display.update()
    

#mainloop
scoreFont = pygame.font.SysFont("comicsans", 30, True)
mobs = pygame.sprite.Group()
Zombie = Mob(100, 410 , 40, 57, 450)
LRbullets = []
UDbullets = []
cowboy = Player(300, 410 , 28, 56)
SlowShoot = 0
run = True
while run:
    clock.tick(27)
    
    if Zombie.visible == True:
        if cowboy.hitbox[1] < Zombie.hitbox[1] + Zombie.hitbox[3] and cowboy.hitbox[1] + cowboy.hitbox[3] > Zombie.hitbox[1]:
            if cowboy.hitbox[0] + cowboy.hitbox[2] > Zombie.hitbox[0] and cowboy.hitbox[0] < Zombie.hitbox[0] + Zombie.hitbox[2]:
                cowboy.hit()
                score -= 5
    
    if SlowShoot > 0:
            SlowShoot += 1 
    if SlowShoot > 15:
        SlowShoot = 0
    #when you press the close button game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #defining weather the bullets on on the screen
    keys = pygame.key.get_pressed()
    for bullet in LRbullets:
        if Zombie.visible == True:
            if bullet.y - bullet.radius < Zombie.hitbox[1] + Zombie.hitbox[3] and bullet.y + bullet.radius > Zombie.hitbox[1]:
                if bullet.x + bullet.radius > Zombie.hitbox[0] and bullet.x - bullet.radius < Zombie.hitbox[0] + Zombie.hitbox[2]:
                    Zombie.hit()
                    hitSound.play()
                    score += 1
                    LRbullets.pop(LRbullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            LRbullets.pop(LRbullets.index(bullet))

    for bullet in UDbullets:
        if Zombie.visible == True:
            if bullet.y - bullet.radius < Zombie.hitbox[1] + Zombie.hitbox[3] and bullet.y + bullet.radius > Zombie.hitbox[1]:
                if bullet.x + bullet.radius > Zombie.hitbox[0] and bullet.x - bullet.radius < Zombie.hitbox[0] + Zombie.hitbox[2]:
                    Zombie.hit()
                    hitSound.play()
                    score += 1
                    UDbullets.pop(UDbullets.index(bullet))

        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            UDbullets.pop(UDbullets.index(bullet))

    keys = pygame.key.get_pressed()
            # shooting left with left key facing any direction
    if keys [pygame.K_LEFT] and SlowShoot == 0:
        bulletSound1.play()
        if cowboy.left:
            facing = x  = - 1
        else: 
            facing = x  = -1
        if len (LRbullets) < 6:
            LRbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1    
    #shooting right with right key facing any direction
    if keys [pygame.K_RIGHT] and SlowShoot == 0:
        bulletSound1.play()
        if cowboy.right:
            facing = x  = 1
        else:
            facing = x  = 1
        if len (LRbullets) < 6:
            LRbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1 

     #shooting up with up key facing any direction
    if keys [pygame.K_UP] and SlowShoot == 0:
        bulletSound1.play()
        if cowboy.up:
            facing = x  = 1
        else:
            facing = x  = 1
        if len (UDbullets) < 6:
            UDbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1 

    #shooting down with down key facing any direction
    if keys [pygame.K_DOWN] and SlowShoot == 0:
        bulletSound1.play()
        if cowboy.down:
            facing = x  = -1
        else:
            facing = x = -1
        if len (UDbullets) < 6:
            UDbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1 

         
    #Movement
    if keys [pygame.K_a] and cowboy.x > cowboy.vel:
        cowboy.x -= cowboy.vel
        cowboy.left = True
        cowboy.right = False
        cowboy.up = False
        cowboy.down = False
        cowboy.standing = False
    elif keys [pygame.K_d] and cowboy.x < screenwidth - cowboy.width - cowboy.vel:
        cowboy.x += cowboy.vel
        cowboy.left = False
        cowboy.right = True
        cowboy.up = False
        cowboy.down = False
        cowboy.standing = False
    elif keys [pygame.K_w] and cowboy.y > cowboy.vel:
        cowboy.y -= cowboy.vel
        cowboy.left = False
        cowboy.right = False
        cowboy.up = True
        cowboy.down = False
        cowboy.standing = False
    elif keys [pygame.K_s] and cowboy.y < screenheight - cowboy.height - cowboy.vel:
        cowboy.y += cowboy.vel
        cowboy.left = False
        cowboy.right = False
        cowboy.up = False
        cowboy.down = True
        cowboy.standing = False
    else:
        cowboy.standing = True
        cowboy.walkCount = 0

    redrawGameWindow()

pygame.quit()
        