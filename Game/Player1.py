import pygame
pygame.init
#These are the images that i am using to make the sprite move and stand still etc.
walkRight = [pygame.image.load('imgs/Rightstand.png'),pygame.image.load('imgs/R1.png'), pygame.image.load('imgs/R2.png'), pygame.image.load('imgs/R3.png'), pygame.image.load('imgs/R4.png'), pygame.image.load('imgs/R5.png'), pygame.image.load('imgs/R6.png'), pygame.image.load('imgs/R7.png'), pygame.image.load('imgs/R8.png')]
walkLeft = [pygame.image.load('imgs/LeftStand.png'),pygame.image.load('imgs/L1.png'), pygame.image.load('imgs/L2.png'), pygame.image.load('imgs/L3.png'), pygame.image.load('imgs/L4.png'), pygame.image.load('imgs/L5.png'), pygame.image.load('imgs/L6.png'), pygame.image.load('imgs/L7.png'), pygame.image.load('imgs/L8.png')]


red = (200,0,0)
yellow = (200,200,0)
green = (34,177,76)


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
        self.standing =True
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.hitbox = (self.x + 0, self.y + 0, 28, 56)
        self.health = 6
        self.visible = True
        # The elements in the hitbox are (top left x, top left y, width, height)
    def draw(self, win):    
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right: 
                    win.blit(walkRight[self.walkCount//3],  (self.x,self.y))
                    self.walkCount += 1
            else:
                if self.left:
                    win.blit(walkLeft[0], (self.x ,self.y))
                else: 
                    win.blit(walkRight[0], (self.x ,self.y))
            
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (50/6 * (6 - self.health)), 10))
            self.hitbox = (self.x + 0, self.y + 0, 40, 57)
            self.hitbox = (self.x + 0, self.y + 0, 28, 56) 
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player

    def health_bar(self,win):
        
        pass
        

    def hit(self): 
        self.isJump = False
        self.jumpCount = 10
        self.walkcount = 0

        if self.health > 0:
            self.health -= 1 
        else:
            self.visible = False

       
        