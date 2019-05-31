import pygame

win = pygame.display.set_mode((500,500))

#this deifnes the enemy by drawing it and creating a path for it etc.
class Mob(object):
    
    #attackLeft = [pygame.image.load("imgs/ELA1.png"), pygame.image.load("imgs/ELA2.png"), pygame.image.load("imgs/ELA3.png"), pygame.image.load("imgs/ELA4.png"), pygame.image.load("imgs/ELA1.png"),pygame.image.load("imgs/ELA2.png"),pygame.image.load("imgs/ELA3.png"),pygame.image.load("imgs/ELA4.png"),pygame.image.load("imgs/ELA1.png")]
    walkLeft = [pygame.image.load("imgs/EWL3.png"), pygame.image.load("imgs/EWL1.png"), pygame.image.load("imgs/EWL1.png"), pygame.image.load("imgs/EWL3.png"), pygame.image.load("imgs/EWL3.png"),pygame.image.load("imgs/EWL1.png"),pygame.image.load("imgs/EWL1.png"),pygame.image.load("imgs/EWL3.png"),pygame.image.load("imgs/EWL3.png")]
    walkRight = [pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR1.png"), pygame.image.load("imgs/ESR2.png"), pygame.image.load("imgs/ESR2.png"),]
    

    def __init__(self, ex, ey, width, height, end):
        self.ex = ex
        self.ey = ey
        self.width = width
        self.height = height
        self.path = [ex, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.ex + 0, self.ey + 0, 40, 57)
        self.health = 2
        self.visible = True
        

    def draw(self,  win):
       
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
        
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.ex,self.ey))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.ex,self.ey))
                self.walkCount += 1

            
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (50/3 * (2 - self.health)), 10))
            self.hitbox = (self.ex + 0, self.ey + 0, 40, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
    def move(self):
        if self.vel > 0:
            if self.ex < self.path[1] + self.vel:
                self.ex += self.vel
            else:
                self.vel = self.vel * -1
                self.ex += self.vel
                self.walkCount = 0
        else:
            if self.ex > self.path[0] - self.vel:
                self.ex += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
      
    def hit(self): 
        if self.health > 0:
            self.health -= 1 
        else: 
            self.visible = False
        
