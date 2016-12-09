import pygame
from PacmanConstant import *
from eventmanager import ChangeModeEvent
class Character(pygame.sprite.Sprite):
    def __init__(self,location,*group):
        super(Character,self).__init__(*group)
        # self.width = width
        # self.height = height
        self.posx = 0
        self.posy = 0

    def checkScreenLimit(self):
        if(self.posx > SCREENWIDTH*16):
            self.posx = SCREENWIDTH*16
        if(self.posy > SCREENHEIGHT*16):
            self.posy = SCREENHEIGHT*16
        if(self.posx < 0):
            self.posx = 0
        if(self.posy < 0):
            self.posy = 0

class Pacman(pygame.sprite.Sprite):
    def __init__(self,location,direction,*groups):
        super(Pacman,self).__init__(*groups)
        self.posx = location[0]
        self.posy = location[1]
        self.direction = direction
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(16,16))
        self.step = 0
        self.movespeed = 0


    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def updateDirection(self,direction):
        self.direction = direction
        self.step = 0
        self.movespeed = 1
    def update(self,game):
        self.rect.x = self.posx
        self.rect.y = self.posy
        last = self.rect.copy()
        self.step += 1
        if(self.step == 8):
            self.step = 0
        self.image = pygame.image.load(self.direction[self.step])
        new = self.rect

        for cell in game.tilemap.layers['wall'].collide(new, 'wall'):
            blockers = cell['wall']
            if(blockers == ""):
                return
            if(self.direction == PACMANDIRECTION.UP):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) < new.centery):
                    self.movespeed = 0

            elif(self.direction == PACMANDIRECTION.DOWN):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) > new.centery):
                    self.movespeed = 0


            elif(self.direction == PACMANDIRECTION.LEFT):
                if(new.centery > cell.top and new.centery < cell.bottom and new.centerx > self.getCenterX(cell)):
                    self.movespeed = 0

            elif(self.direction == PACMANDIRECTION.RIGHT):
                if (new.centery > cell.top and new.centery < cell.bottom and new.centerx < self.getCenterX(cell)):
                    self.movespeed = 0
        if (new.centerx > 440 and self.direction == PACMANDIRECTION.RIGHT):
            self.posx = 8
        elif (new.centerx < 8 and self.direction == PACMANDIRECTION.LEFT):
            self.posx = 440

        game.tilemap.set_focus(new.x,new.y)

    def updatePosition(self):
        if self.direction == PACMANDIRECTION.RIGHT:
            self.posx += self.movespeed
        elif self.direction == PACMANDIRECTION.LEFT:
            self.posx -= self.movespeed
        elif self.direction == PACMANDIRECTION.UP:
            self.posy -= self.movespeed
        elif self.direction == PACMANDIRECTION.DOWN:
            self.posy += self.movespeed

    def getCenterX(self,cell):
        return (cell.right-cell.left)/2+cell.left
    def getCenterY(self,cell):
        return (cell.bottom-cell.top)/2+cell.top
class Ghost(pygame.sprite.Sprite):
    def __init__(self,location,direction,*group):
        super(Ghost,self).__init__(*group)
        self.mode = GHOSTMODE.CHASE
        self.direction = direction
        self.posx = location[0]
        self.posy = location[1]
        self.ghostdirection = GHOSTDIRECTION.UP
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(16,16))
        self.step = 0
        self.movespeed = 1


    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def updatePosition(self):
        if self.ghostdirection == GHOSTDIRECTION.RIGHT:
             self.posx += self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.LEFT:
             self.posx -= self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.UP:
             self.posy -= self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.DOWN:
             self.posy += self.movespeed

    def updateDirection(self,direction):
        self.ghostdirection = direction

    def update(self,game):
        if self.mode == GHOSTMODE.CHASE:
            self.rect.x = self.posx
            self.rect.y = self.posy
            self.step += 1
            if (self.step == 6):
                self.step = 0
            self.image = pygame.image.load(self.direction[self.step])
            if(self.rect.colliderect(game.pacman.rect)):
                game.pacman.kill()
                print "die"

        elif self.mode == GHOSTMODE.SCARE:
            self.rect.x = self.posx
            self.rect.y = self.posy
            self.step += 1
            if (self.step == 6):
                self.step = 0
            self.image = pygame.image.load(self.direction[self.step])
            if (self.rect.colliderect(game.pacman.rect)):
                self.kill()
                print "eat ghost"
        new = self.rect
        for cell in game.tilemap.layers['wall'].collide(new, 'wall'):
            blockers = cell['wall']
            if(blockers == ""):
                return
            if(self.ghostdirection == GHOSTDIRECTION.UP):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) < new.centery):
                    self.movespeed = 0

            elif(self.ghostdirection == GHOSTDIRECTION.DOWN):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) > new.centery):
                    self.movespeed = 0


            elif(self.ghostdirection == GHOSTDIRECTION.LEFT):
                if(new.centery > cell.top and new.centery < cell.bottom and new.centerx > self.getCenterX(cell)):
                    self.movespeed = 0

            elif(self.ghostdirection == GHOSTDIRECTION.RIGHT):
                if (new.centery > cell.top and new.centery < cell.bottom and new.centerx < self.getCenterX(cell)):
                    self.movespeed = 0
        if (new.centerx > 440 and self.ghostdirection == GHOSTDIRECTION.RIGHT):
            self.posx = 8
        elif (new.centerx < 8 and self.ghostdirection == GHOSTDIRECTION.LEFT):
            self.posx = 440

    def getCenterX(self,cell):
        return (cell.right-cell.left)/2+cell.left
    def getCenterY(self,cell):
        return (cell.bottom-cell.top)/2+cell.top

class Biscuit(pygame.sprite.Sprite):

    def __init__(self,location,*groups):
        super(Biscuit,self).__init__(*groups)
        self.image = pygame.image.load('sprite/biscuit.gif')
        self.rect = pygame.rect.Rect(location,(15,15))

    def update(self,game):
        if self.rect.colliderect(game.pacman.rect):
            # print "eat biscuit"
            self.kill()

class Powerball(pygame.sprite.Sprite):

    def __init__(self,location,*groups):
        super(Powerball,self).__init__(*groups)
        self.image = pygame.image.load('sprite/powerball.gif')
        self.rect = pygame.rect.Rect(location,(15,15))

    def update(self,game):
        if self.rect.colliderect(game.pacman.rect):
            print "eat powerball"
            game.evManager.Post(ChangeModeEvent(GHOSTMODE.SCARE))
            self.kill()