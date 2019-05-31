import pygame, random
from Projectiles import Projectile
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
FullHealth = pygame.image.load("imgs/Fullheart.png")
HalfHealth = pygame.image.load("imgs/HalfHeart.png")
NoHealth = pygame.image.load("imgs/EmptyHeart.png")

#The code below is for the clock. This allows me to set the FPS for the game etc.
clock = pygame.time.Clock()

#bulletSound1 = pygame.mixer.Sound("Sounds/Pew.wav")
#hitSound = pygame.mixer.Sound("Sounds/bruh.wav")
#Playerdmg = pygame.mixer.Sound("Sounds/oof.wav")

#music = pygame.mixer.music.load("Sounds/Music2.mp3")
#pygame.mixer.music.play(-1)
score = 0

#Used as variables for boundrys etc
screenwidth = 500
screenheight = 500

#class defining all stuff to do with player

#Projectiles class


#drawing the game window and sprites etc on the window
def redrawGameWindow():
    win.blit(bg, (0,0))
    win.blit(FullHealth, (350, 10))
    win.blit(FullHealth, (400, 10))
    win.blit(FullHealth, (450, 10))
    text = scoreFont.render("Kills:" + str(score),1, (255,255,255))
    win.blit(text,(10,10))
    Zombie.draw(win)
    Zombie1.draw(win)
    for bullet in bullets:
        bullet.draw(win)
        
    cowboy.draw(win)
    pygame.display.update()
    


#mainloop
scoreFont = pygame.font.SysFont("comicsans", 30, True)
mobs = pygame.sprite.Group()
cowboy = Player(60, 410 , 28, 56)
Zombie = Mob(300, 410 , 40, 57, 450)
Zombie1 = Mob(200, 410 , 40, 57, 450)
bullets = []
SlowShoot = 0
run = True
while run:
    clock.tick(27)
    
    #First zombie hitbox (contact with player)
    if Zombie.visible == True:
        if cowboy.hitbox[1] < Zombie.hitbox[1] + Zombie.hitbox[3] and cowboy.hitbox[1] + cowboy.hitbox[3] > Zombie.hitbox[1]:
            if cowboy.hitbox[0] + cowboy.hitbox[2] > Zombie.hitbox[0] and cowboy.hitbox[0] < Zombie.hitbox[0] + Zombie.hitbox[2]:
                #Playerdmg.play()
                cowboy.hit()
    #Second zombie Hitbox (contact with player)
    if Zombie1.visible == True:
        if cowboy.hitbox[1] < Zombie1.hitbox[1] + Zombie1.hitbox[3] and cowboy.hitbox[1] + cowboy.hitbox[3] > Zombie1.hitbox[1]:
            if cowboy.hitbox[0] + cowboy.hitbox[2] > Zombie1.hitbox[0] and cowboy.hitbox[0] < Zombie1.hitbox[0] + Zombie1.hitbox[2]:
                #Playerdmg.play()
                cowboy.hit()

    if SlowShoot > 0:
            SlowShoot += 1 
    if SlowShoot > 15:
        SlowShoot = 0
    #when you press the close button game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #defining weather the bullets appear on the screen
    #first bullet hitbox (contact with zombie)
    keys = pygame.key.get_pressed()
    for bullet in bullets:
        if Zombie.visible == True:
            if bullet.y - bullet.radius < Zombie.hitbox[1] + Zombie.hitbox[3] and bullet.y + bullet.radius > Zombie.hitbox[1]:
                if bullet.x + bullet.radius > Zombie.hitbox[0] and bullet.x - bullet.radius < Zombie.hitbox[0] + Zombie.hitbox[2]:
                    Zombie.hit()
                    #hitSound.play()
                    bullets.pop(bullets.index(bullet))
                if Zombie.visible == False:
                    score += 1
    #Bullet hitbox (contact with second zombie)
    for bullet in bullets:
        if Zombie1.visible == True:
            if bullet.y - bullet.radius < Zombie1.hitbox[1] + Zombie1.hitbox[3] and bullet.y + bullet.radius > Zombie1.hitbox[1]:
                if bullet.x + bullet.radius > Zombie1.hitbox[0] and bullet.x - bullet.radius < Zombie1.hitbox[0] + Zombie1.hitbox[2]:
                    Zombie1.hit()
                    #hitSound.play()
                    bullets.pop(bullets.index(bullet))
                if Zombie1.visible == False:
                    score += 1

        #if the bullets go off the screen destroy them
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
        # shooting left with left key facing any direction
    if keys [pygame.K_LEFT] and SlowShoot == 0:
        #bulletSound1.play()
        if cowboy.left:
            facing = x  = - 1
        else: 
            facing = x  = -1
        if len (bullets) < 6:
            bullets.append(Projectile(round(cowboy.px + cowboy.width //2), round(cowboy.py + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1    
    #shooting right with right key facing any direction
    if keys [pygame.K_RIGHT] and SlowShoot == 0:
        #bulletSound1.play()
        if cowboy.right:
            facing = x  = 1
        else:
            facing = x  = 1
        if len (bullets) < 6:
            bullets.append(Projectile(round(cowboy.px + cowboy.width //2), round(cowboy.py + cowboy.height//2), 6, (0,0,0), facing))
        SlowShoot = 1 
         
    #Movement
    if keys [pygame.K_a] and cowboy.px > cowboy.vel:
        cowboy.px -= cowboy.vel
        cowboy.left = True
        cowboy.right = False
        cowboy.standing = False
    elif keys [pygame.K_d] and cowboy.px < screenwidth - cowboy.width - cowboy.vel:
        cowboy.px += cowboy.vel
        cowboy.left = False
        cowboy.right = True
        cowboy.standing = False
    else:
        cowboy.standing = True
        cowboy.walkCount = 0

    if not(cowboy.isJump):
        if keys[pygame.K_SPACE]:
            cowboy.isJump = True
            cowboy.right = False
            cowboy.left = False
            cowboy.walkCount = 0
    else:
        if cowboy.jumpCount >= -10:
            neg = 1
            if cowboy.jumpCount < 0:
                neg = -1
            cowboy.py -= (cowboy.jumpCount ** 2) * 0.5 * neg
            cowboy.jumpCount -= 1
        else:
            cowboy.isJump = False
            cowboy.jumpCount = 10

    redrawGameWindow()

pygame.quit()
        