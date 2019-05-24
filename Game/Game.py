import pygame
import os, sys
pygame.init()

#The code below sets up the window size also providing the win with a variable
win = pygame.display.set_mode((500,500))
#Gives a title for my game.
pygame.display.set_caption("Dungeon Crawler")

#These are the images that i am using to make the sprite move and stand still etc.
walkRight = [pygame.image.load('imgs/Rightstand.png'),pygame.image.load('imgs/R1.png'), pygame.image.load('imgs/R2.png'), pygame.image.load('imgs/R3.png'), pygame.image.load('imgs/R4.png'), pygame.image.load('imgs/R5.png'), pygame.image.load('imgs/R6.png'), pygame.image.load('imgs/R7.png'), pygame.image.load('imgs/R8.png')]
walkLeft = [pygame.image.load('imgs/LeftStand.png'),pygame.image.load('imgs/L1.png'), pygame.image.load('imgs/L2.png'), pygame.image.load('imgs/L3.png'), pygame.image.load('imgs/L4.png'), pygame.image.load('imgs/L5.png'), pygame.image.load('imgs/L6.png'), pygame.image.load('imgs/L7.png'), pygame.image.load('imgs/L8.png')]
walkUp = [pygame.image.load('imgs/US1.png'), pygame.image.load('imgs/UL.png'),pygame.image.load('imgs/UR.png'), pygame.image.load('imgs/UR.png'),pygame.image.load('imgs/UL.png'), pygame.image.load('imgs/UL.png'),pygame.image.load('imgs/UR.png'), pygame.image.load('imgs/UR.png'),pygame.image.load('imgs/UL.png')]
walkDown = [pygame.image.load('imgs/Front.png'), pygame.image.load('imgs/FL1.png'),pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FR1.png'),pygame.image.load('imgs/FL1.png'), pygame.image.load('imgs/FL1.png'),pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FL1.png')]
bg = pygame.image.load('imgs/BasicBG.png')
char = pygame.image.load('imgs/Front.png')

#The code below is for the clock. This allows me to set the FPS for the game etc.
clock = pygame.time.Clock()

#Used as variables for boundrys etc
screenwidth = 500
screenheight = 500

#class defining all stuff to do with player
class Player(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 0, self.y + 0, 28, 56)
        # The elements in the hitbox are (top left x, top left y, width, height)

    def draw(self, win):    
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],  (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp[self.walkCount//3],  (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown[self.walkCount//3],  (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x ,self.y))
            elif self.right:
                win.blit(walkRight[0], (self.x ,self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x ,self.y))
            else:
                win.blit(walkDown[0], (self.x ,self.y))
            self.hitbox = (self.x + 0, self.y + 0, 28, 56) 
            pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player

#this deifnes the enemy by drawing it and creating a path for it etc.
class Enemy(object):
    
    walkLeft = [pygame.image.load("imgs/EWL3.png"), pygame.image.load("imgs/EWL1.png"), pygame.image.load("imgs/EWL1.png"), pygame.image.load("imgs/EWL3.png"), pygame.image.load("imgs/EWL3.png"),pygame.image.load("imgs/EWL1.png"),pygame.image.load("imgs/EWL1.png"),pygame.image.load("imgs/EWL3.png"),pygame.image.load("imgs/EWL3.png")]
    walkRight = [pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR2.png"),]
    walkUp = [pygame.image.load("imgs/ESU2.png"), pygame.image.load("imgs/ESU1.png"), pygame.image.load("imgs/ESU1.png"), pygame.image.load("imgs/ESU2.png"), pygame.image.load("imgs/ESU2.png"),pygame.image.load("imgs/ESU1.png"),pygame.image.load("imgs/ESU1.png"),pygame.image.load("imgs/ESU2.png"),pygame.image.load("imgs/ESU2.png")]
    walkDown = [pygame.image.load("imgs/ESR.png"), pygame.image.load("imgs/EFL.png"), pygame.image.load("imgs/EFL.png"), pygame.image.load("imgs/EFR.png"), pygame.image.load("imgs/EFR.png"),pygame.image.load("imgs/EFL.png"),pygame.image.load("imgs/EFL.png"),pygame.image.load("imgs/EFR.png"),pygame.image.load("imgs/EFR.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 0, self.y + 0, 40, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 0, self.y + 0, 40, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
     # This will display when the enemy is hit
    def hit(self): 
        print('hit')

#Projectiles class
class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = 4
        self.color = color 
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, (255,255,0), (self.x, self.y), self.radius)

#enemy class

#drawing the game window and sprites etc on the window
def redrawGameWindow():
    win.blit(bg, (0,0))
    Zombie.draw(win)
    for bullet in LRbullets:
        bullet.draw(win)
    
    for bullet in UDbullets:
            bullet.draw(win)
    cowboy.draw(win)
    pygame.display.update()
    

#mainloop
Zombie = Enemy(100, 410, 32, 55, 450)
LRbullets = []
UDbullets = []
cowboy = Player(300, 410 , 28, 56)
run = True
while run:
    clock.tick(27)
    #when you press the close button game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #defining weather the bullets on on the screen
    for bullet in LRbullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            LRbullets.pop(LRbullets.index(bullet))

    for bullet in UDbullets:
        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            UDbullets.pop(UDbullets.index(bullet))

    keys = pygame.key.get_pressed()
    #shooting left with left key facing any direction
    if keys [pygame.K_LEFT]:
        if cowboy.left:
            facing = x  = - 1
        else: 
            facing = x  = -1
        if len (LRbullets) < 6:
            LRbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
    #shooting right with right key facing any direction
    if keys [pygame.K_RIGHT]:
        if cowboy.right:
            facing = x  = 1
        else:
            facing = x  = 1
        if len (LRbullets) < 6:
            LRbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
     #shooting up with up key facing any direction
    if keys [pygame.K_UP]:
        if cowboy.up:
            facing = x  = 1
        else:
            facing = x  = 1

        if len (UDbullets) < 6:
            UDbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))
     #shooting down with down key facing any direction
    if keys [pygame.K_DOWN]:
        if cowboy.down:
            facing = x  = -1
        else:
            facing = x = -1
        if len (UDbullets) < 6:
            UDbullets.append(Projectile(round(cowboy.x + cowboy.width //2), round(cowboy.y + cowboy.height//2), 6, (0,0,0), facing))

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
        