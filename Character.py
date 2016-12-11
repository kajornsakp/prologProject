import pygame
from PacmanConstant import *
import math
from eventmanager import ChangeModeEvent,PacmanDieEvent
import math
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
        self.prevx = 12
        self.prevy = 23
        self.direction = direction
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(18,18))
        self.step = 0
        self.velx = -1
        self.vely = 0
        self.c = 0
        self.isTrap = False
        self.mode = GHOSTMODE.CHASE
        self.imageSet = None
        self.future = direction
        self.walkable = True
        self.isDead = False



    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def updateDirection(self,direction):
        self.future = direction
        self.step = 0
        if (self.walkable):
            self.direction = direction
        self.checkDirection()

    def update(self,game):
        self.rect = pygame.rect.Rect((self.posx,self.posy),(16,16))
        if(self.mode == GHOSTMODE.CHASE):
            self.imageSet = self.direction
        else:
            if self.direction == PACMANDIRECTION.RIGHT:
                self.imageSet = REDPACMANDIRECTION.RIGHT
            elif self.direction == PACMANDIRECTION.LEFT:
                self.imageSet = REDPACMANDIRECTION.LEFT
            elif self.direction == PACMANDIRECTION.UP:
                self.imageSet = REDPACMANDIRECTION.UP
            elif self.direction == PACMANDIRECTION.DOWN:
                self.imageSet = REDPACMANDIRECTION.DOWN

        last = self.rect.copy()
        self.step += 1
        if(self.step == 8):
            self.step = 0
        self.image = pygame.image.load(self.imageSet[self.step])
        new = self.rect

        for cell in game.tilemap.layers['wall'].collide(new, 'wall'):
            blockers = cell['wall']
            if(blockers == ""):
                return
            if(self.direction == PACMANDIRECTION.UP):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) < new.centery):
                    self.vely = 0

            elif(self.direction == PACMANDIRECTION.DOWN):
                if(new.centerx < cell.right and new.centerx > cell.left and self.getCenterY(cell) > new.centery):
                    self.vely = 0

            elif(self.direction == PACMANDIRECTION.LEFT):
                if(new.centery > cell.top and new.centery < cell.bottom and new.centerx > self.getCenterX(cell)):
                    self.velx = 0

            elif(self.direction == PACMANDIRECTION.RIGHT):
                if (new.centery > cell.top and new.centery < cell.bottom and new.centerx < self.getCenterX(cell)):
                    self.velx = 0

        if (new.centerx > 440 and self.direction == PACMANDIRECTION.RIGHT):
            self.posx = 8
            game.count = 8
        elif (new.centerx < 8 and self.direction == PACMANDIRECTION.LEFT):
            self.posx = 440
            game.count = 8

        game.tilemap.set_focus(new.x,new.y)

    def checkDirection(self):
        if self.direction == PACMANDIRECTION.RIGHT:
            self.velx = 1
            self.vely = 0

        elif self.direction == PACMANDIRECTION.LEFT:
            self.velx = -1
            self.vely = 0

        elif self.direction == PACMANDIRECTION.UP:
            self.velx = 0
            self.vely = -1

        elif self.direction == PACMANDIRECTION.DOWN:
            self.velx = 0
            self.vely = 1

    def setSpeed(self, n):
        if self.direction == PACMANDIRECTION.RIGHT:
            self.velx = n
            self.vely = 0

        elif self.direction == PACMANDIRECTION.LEFT:
            self.velx = n*(-1)
            self.vely = 0

        elif self.direction == PACMANDIRECTION.UP:
            self.velx = 0
            self.vely = n*(-1)

        elif self.direction == PACMANDIRECTION.DOWN:
            self.velx = 0
            self.vely = n


    def updatePosition(self, prolog):
        self.posx += self.velx
        self.posy += self.vely

        if self.posx % 16 == 0 or self.posy % 16 == 0:
            x = math.floor(self.posx / 16)
            y = math.floor(self.posy / 16)
            self.c += 1
            if self.c >= 16:
                if self.prevy != y or self.prevx != x:
                    self.prevx = x
                    self.prevy = y
                    prolog.movePacman(int(x)+1, int(y)+1)
                    self.c = 0

    def getCenterX(self,cell):
        return (cell.right-cell.left)/2+cell.left

    def getCenterY(self,cell):
        return (cell.bottom-cell.top)/2+cell.top

    def releaseTrap(self):
        self.isTrap = False

class Ghost(pygame.sprite.Sprite):
    def __init__(self,location,direction,*group):
        super(Ghost,self).__init__(*group)
        self.mode = GHOSTMODE.CHASE
        self.direction = direction
        self.posx = location[0]
        self.posy = location[1]
        self.prevx = 12
        self.prevy = 12
        self.ghostdirection = GHOSTDIRECTION.UP
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(16,16))
        self.step = 0
        self.movespeed = 1
        self.c = 0
        self.count = 0


    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def updatePosition(self, prolog, game):
        if self.ghostdirection == GHOSTDIRECTION.RIGHT:
            self.posx += self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.LEFT:
            self.posx -= self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.UP:
            self.posy -= self.movespeed
        elif self.ghostdirection == GHOSTDIRECTION.DOWN:
            self.posy += self.movespeed


        if self.posx % 16 == 0 or self.posy % 16 == 0:
            if self.posx % 16 == 0 or self.posy % 16 == 0:
                x1 = math.floor(self.posx / 16)
                y1 = math.floor(self.posy / 16)
                y = int(math.floor(game.pacman.rect.centery / 16)) + 1
                x = int(math.floor(game.pacman.rect.centerx / 16)) + 1
                self.c += 1
                if self.c >= 16:
                    self.c = 0
                    self.prevx = x1
                    self.prevy = 1
                    direction = 0
                    if self.direction == GHOSTSPRITE.LIGHTBLUE:
                        direction = self.getBlueDirection(x, y, game.pacman, prolog)
                    elif self.direction == GHOSTSPRITE.PINK:
                        direction = self.getPinkDirection(x, y, game.redghost, prolog)
                    else:
                        direction = prolog.moveGhost(x, y, self.direction)
                    # print direction
                    if direction == 100:
                        self.updateDirection(self.ghostdirection)
                    else:
                        self.updateDirection(direction)

    def getBlueDirection(self, x, y, pacman, prolog):
        if y - 4 > 1 and y + 4 < 31 and x - 4 > 1 and x + 4 < 28:
            # print "------------------------------------"
            # print "pacmanx,y: " + str(x) + ',' + str(y)
            if pacman.direction == PACMANDIRECTION.UP:
                return prolog.moveGhost(x, y - 4, self.direction)
            elif pacman.direction == PACMANDIRECTION.DOWN:
                return prolog.moveGhost(x, y + 4, self.direction)
            elif pacman.direction == PACMANDIRECTION.RIGHT:
                return prolog.moveGhost(x + 4, y, self.direction)
            elif pacman.direction == PACMANDIRECTION.LEFT:
                return prolog.moveGhost(x - 4, y, self.direction)
        else:
            # print "===================================="
            if pacman.direction == PACMANDIRECTION.UP:
                return prolog.moveGhost(x, 2, self.direction)
            elif pacman.direction == PACMANDIRECTION.DOWN:
                return prolog.moveGhost(x, 30, self.direction)
            elif pacman.direction == PACMANDIRECTION.RIGHT:
                return prolog.moveGhost(2, y, self.direction)
            elif pacman.direction == PACMANDIRECTION.LEFT:
                return prolog.moveGhost(27, y, self.direction)

    def getPinkDirection(self, px, py, redghost, prolog):
        ry = int(math.floor(redghost.rect.centery / 16)) + 1
        rx = int(math.floor(redghost.rect.centerx / 16)) + 1
        newx = px + (rx - px)
        newy = py + (ry - py)
        # print "p:" +str(px) + "," + str(py)
        # print "r:" + str(rx) + "," + str(ry)
        # print "n:" + str(newx) + "," + str(newy)
        return prolog.movePinkGhost(px, py, rx, ry)


    def changeMode(self, mode, prolog):
        if self.direction == GHOSTSPRITE.RED:
            prolog.changeGhostMode('red', mode)
        elif self.direction == GHOSTSPRITE.LIGHTBLUE:
            prolog.changeGhostMode('blue', mode)
        elif self.direction == GHOSTSPRITE.PINK:
            prolog.changeGhostMode('pink', mode)
        elif self.direction == GHOSTSPRITE.ORANGE:
            prolog.changeGhostMode('orange', mode)

    def changePath(self, x1, y1,game):
        x = int(math.floor(self.posx / 16)) + 1
        y = int(math.floor(self.posy / 16)) + 1
        qu = 'findAdj((' + str(x) + ',' + str(y) + '),[(' + str(x+x1) + ',' + str(y + y1) + ')],X)'
        q = str(list(game.prolog.p.query(qu))[0]['X'][0]).split(',')
        newX = int(q[1][1] + q[1][2])
        newY = int(q[2][1] + q[2][2])
        self.prevx = x
        self.prevy = y
        self.updateDirection(self.checkDirection(newX, newY, x, y))


    def checkDirection(self, x1, y1, x2, y2):
        if x1 == x2 and y1 - y2 < 0:
            return GHOSTDIRECTION.UP
        elif x1 == x2 and y1 - y2 > 0:
            return GHOSTDIRECTION.DOWN
        elif y1 == y2 and x1 - x2 < 0:
            return GHOSTDIRECTION.LEFT
        elif y1 == y2 and x1 - x2 > 0:
            return GHOSTDIRECTION.RIGHT

    def updateDirection(self,direction):
        p = self.ghostdirection
        self.ghostdirection = direction
        if direction != p:
            self.movespeed = 1


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
                game.pacman.isDead = True
                game.evManager.Post(PacmanDieEvent())
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
                if(self.direction == GHOSTSPRITE.RED):
                    game.redghostDie()
                elif(self.direction == GHOSTSPRITE.LIGHTBLUE):
                    game.blueghostDie()
                elif(self.direction == GHOSTSPRITE.PINK):
                    game.pinkghostDie()
                elif(self.direction == GHOSTSPRITE.ORANGE):
                    game.orangeghostDie()
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
            self.c = 8
            # print "+++++++++++++++++++++++++++++++++"
        elif (new.centerx < 8 and self.ghostdirection == GHOSTDIRECTION.LEFT):
            self.posx = 440
            self.c = 8
            # print "===================================="

    def getCenterX(self,cell):
        return (cell.right-cell.left)/2+cell.left
    def getCenterY(self,cell):
        return (cell.bottom-cell.top)/2+cell.top

class Biscuit(pygame.sprite.Sprite):

    def __init__(self,location,*groups):
        super(Biscuit,self).__init__(*groups)
        self.image = pygame.image.load('sprite/biscuit.png')
        self.rect = pygame.rect.Rect(location,(15,15))

    def update(self,game):
        if self.rect.colliderect(game.pacman.rect):
            game.score += 1
            self.kill()

class Powerball(pygame.sprite.Sprite):

    def __init__(self,location,*groups):
        super(Powerball,self).__init__(*groups)
        self.image = pygame.image.load('sprite/powerball.png')
        self.rect = pygame.rect.Rect(location,(15,15))

    def update(self,game):
        if self.rect.colliderect(game.pacman.rect):
            print "eat powerball"
            game.evManager.Post(ChangeModeEvent(GHOSTMODE.SCARE))
            self.kill()

class Laser(pygame.sprite.Sprite):

    def __init__(self,location,direction,*group):
        super(Laser,self).__init__(*group)
        self.direction = direction
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(16,16))
        self.posx = location[0]
        self.posy = location[1]
        self.step = 0

    def update(self,game):
        self.rect.x = self.posx
        self.rect.y = self.posy
        #TODO: add speed
        if(self.direction == LASERSPRITE.UP):
            self.posy -= 1.075
        elif(self.direction == LASERSPRITE.DOWN):
            self.posy += 1.075
        elif(self.direction == LASERSPRITE.LEFT):
            self.posx -= 1.075
        elif(self.direction == LASERSPRITE.RIGHT):
            self.posx += 1.075
        self.image = pygame.image.load(self.direction[self.step])
        self.step+=1
        if(self.step == 3):
            self.step = 2
        if self.rect.colliderect(game.pacman.rect):
            print "headshot"
            game.pacman.kill()
            self.kill()


class Water(pygame.sprite.Sprite):

    def __init__(self,location,*group):
        super(Water,self).__init__(*group)
        self.direction = WATERSPRITE.WATER
        self.image = pygame.image.load(self.direction[0])
        self.rect = pygame.rect.Rect(location,(15,15))
        self.step = 0

    def update(self,game):
        self.image = pygame.image.load(self.direction[self.step])
        self.step += 1
        if (self.step == 7):
            self.step = 6

        if self.rect.colliderect(game.pacman.rect):
            game.pacman.setSpeed(0.5)

class Blind(pygame.sprite.Sprite):

    def __init__(self,location,*group):
        super(Blind,self).__init__(*group)
        self.image = pygame.image.load(BLINDSPRITE)
        self.rect = pygame.rect.Rect(location,(1500,1500))

    def update(self,game):
        self.rect.x = game.pacman.posx-self.rect.width/2
        self.rect.y = game.pacman.posy-self.rect.height/2
        print self.rect.x,self.rect.y
        game.tilemap.set_focus(self.rect.x, self.rect.y)


class Trap(pygame.sprite.Sprite):
    def __init__(self,location,*group):
        super(Trap,self).__init__(*group)
        self.image = pygame.image.load(TRAPSPRITE)
        self.rect = pygame.rect.Rect(location,(16,16))

    def update(self,game):
        if(self.rect.colliderect(game.pacman.rect)):
            if(game.pacman.isTrap == True):
                game.pacman.vely = 0
                game.pacman.velx = 0
            else:
                game.pacman.checkDirection()
