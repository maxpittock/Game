import pygame
pygame.init
#These are the images that i am using to make the sprite move and stand still etc.
walkRight = [pygame.image.load('imgs/Rightstand.png'),pygame.image.load('imgs/R1.png'), pygame.image.load('imgs/R2.png'), pygame.image.load('imgs/R3.png'), pygame.image.load('imgs/R4.png'), pygame.image.load('imgs/R5.png'), pygame.image.load('imgs/R6.png'), pygame.image.load('imgs/R7.png'), pygame.image.load('imgs/R8.png')]
walkLeft = [pygame.image.load('imgs/LeftStand.png'),pygame.image.load('imgs/L1.png'), pygame.image.load('imgs/L2.png'), pygame.image.load('imgs/L3.png'), pygame.image.load('imgs/L4.png'), pygame.image.load('imgs/L5.png'), pygame.image.load('imgs/L6.png'), pygame.image.load('imgs/L7.png'), pygame.image.load('imgs/L8.png')]
walkUp = [pygame.image.load('imgs/US1.png'), pygame.image.load('imgs/UL.png'),pygame.image.load('imgs/UR.png'), pygame.image.load('imgs/UR.png'),pygame.image.load('imgs/UL.png'), pygame.image.load('imgs/UL.png'),pygame.image.load('imgs/UR.png'), pygame.image.load('imgs/UR.png'),pygame.image.load('imgs/UL.png')]
walkDown = [pygame.image.load('imgs/Front.png'), pygame.image.load('imgs/FL1.png'),pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FR1.png'),pygame.image.load('imgs/FL1.png'), pygame.image.load('imgs/FL1.png'),pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FR1.png'), pygame.image.load('imgs/FL1.png')]

win = pygame.display.set_mode((500,500))

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
        self.standing =True
        self.down = False
        self.walkCount = 0
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

    def hit(self): 
        self.x = 60
        self.y = 410
        self.walkcount = 0
        font1 = pygame.font.SysFont('cominsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i <100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player