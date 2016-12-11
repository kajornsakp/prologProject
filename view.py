import pygame

from Character import *
from Map import Map
from PacmanConstant import *
from eventmanager import *
import tmx.tmx as tmx
from PrologController import PrologController
import math



class GraphicalView(object):

    def __init__(self, evManager, model):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
                
        Attributes:
        isinitialized (bool): pygame is ready to draw.
        screen (pygame.Surface): the screen surface.
        clock (pygame.time.Clock): keeps the fps constant.
        smallfont (pygame.Font): a small font.
        """
        
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
        self.direction = PACMANDIRECTION.LEFT
        self.futureDirection = PACMANDIRECTION.LEFT
        self.movespeed = 1
        self.prolog = PrologController()
        self.life = 3
        self.isBlind = False
        self.count = 0
        self.countGhost = 0
        self.timerSec = 0
        self.isTimerInit = False
        self.fn = None
        self.tick = None
        self.moveable = True
        self.screenPage = 0
        self.score = 0
        self.sec = 0
        self.beast = 99999
        self.biscuitamount = 285
        self.isWin = False


    def initPacman(self):
        self.pacmanSprite = tmx.SpriteLayer()
        pacmantmx = self.tilemap.layers['pacman'].find('pacman')[0]
        self.pacman = Pacman((pacmantmx.px,pacmantmx.py),self.direction,self.pacmanSprite)
        self.pacman.movespeed = self.movespeed
        self.tilemap.layers.append(self.pacmanSprite)
        self.tilemap.set_focus(1,1)

    def initGhost(self):
        self.redghostSprite = tmx.SpriteLayer()
        redghostTmx = self.tilemap.layers['ghost'].find('redghost')[0]
        self.redghost = Ghost((redghostTmx.px, redghostTmx.py),GHOSTSPRITE.RED,self.redghostSprite)
        self.tilemap.layers.append(self.redghostSprite)

        self.pinkghostSprite = tmx.SpriteLayer()
        pinkghostTmx = self.tilemap.layers['ghost'].find('pinkghost')[0]
        self.pinkghost = Ghost((redghostTmx.px, redghostTmx.py), GHOSTSPRITE.PINK,self.pinkghostSprite)
        self.tilemap.layers.append(self.pinkghostSprite)

        self.blueghostSprite = tmx.SpriteLayer()
        blueghostTmx = self.tilemap.layers['ghost'].find('blueghost')[0]
        self.blueghost = Ghost((redghostTmx.px, redghostTmx.py), GHOSTSPRITE.LIGHTBLUE, self.blueghostSprite)
        self.tilemap.layers.append(self.blueghostSprite)

        self.orangeghostSprite = tmx.SpriteLayer()
        orangeghostTmx = self.tilemap.layers['ghost'].find('orangeghost')[0]
        self.orangeghost = Ghost((redghostTmx.px, redghostTmx.py), GHOSTSPRITE.ORANGE, self.orangeghostSprite)
        self.tilemap.layers.append(self.orangeghostSprite)

    def initBiscuit(self):
        self.biscuitSprite = tmx.SpriteLayer()
        for biscuit in self.tilemap.layers['biscuit'].find('biscuit'):
            Biscuit((biscuit.px,biscuit.py),self.biscuitSprite)
        self.tilemap.layers.append(self.biscuitSprite)


    def initPowerball(self):
        self.powerballSprite = tmx.SpriteLayer()
        for powerball in self.tilemap.layers['biscuit'].find('powerball'):
            Powerball((powerball.px,powerball.py),self.powerballSprite)
        self.tilemap.layers.append(self.powerballSprite)

    def notify(self, event):
        """
        Receive events posted to the message queue. 
        """

        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event,InputEvent):
            if(self.screenPage != 3):
                if(event.char == "SPACE"):
                    self.screenPage += 1
            if(self.screenPage == 3):
                self.updateDirection(event.char)
        elif isinstance(event, QuitEvent):
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event,ChangeModeEvent):
            self.changeMode(event)
            self.beast = self.sec + 20
        elif isinstance(event,PacmanDieEvent):
            self.pacmanDie()
        elif isinstance(event, TickEvent):
            if(self.screenPage == 3):
                if (self.isTimerInit):
                    self.countDown(self.fn)
                self.count += 1
                if (self.count == 16):
                    x, y = self.checkValidInput(int(math.floor(self.pacman.posx / 16)) + 1,
                                                int(math.floor(self.pacman.posy / 16)) + 1)
                    moveable = list(self.prolog.p.query('movePacman(' + str(x) + ',' + str(y) + ')'))
                    if len(moveable) != 0:
                        self.direction = self.futureDirection
                    self.pacman.updateDirection(self.direction)
                    self.count = 0
                    self.sec += 1
                if(self.sec == 5):
                    self.updateGhostMode('chase')
                if(self.sec == 25):
                    self.updateGhostMode('scatter')
                if(self.sec >= 30):
                    self.updateGhostMode('chase')
                if(self.sec == 9999):
                    self.changeMode(ChangeModeEvent(GHOSTMODE.CHASE))
                self.pacman.updatePosition(self.prolog)
                self.updateGhostPosition(self.prolog)
            self.renderall()
            self.clock.tick(60)

    def changeMode(self, event):
        if event.mode == GHOSTMODE.CHASE:
            self.pacman.mode = GHOSTMODE.CHASE
            self.redghost.mode = GHOSTMODE.CHASE
            self.blueghost.mode = GHOSTMODE.CHASE
            self.pinkghost.mode = GHOSTMODE.CHASE
            self.orangeghost.mode = GHOSTMODE.CHASE
            list(self.prolog.p.query('changeAllGhostsMode(chase)'))
            list(self.prolog.p.query('changePacmanMode(normal)'))
        elif event.mode == GHOSTMODE.SCARE:
            self.pacman.mode = GHOSTMODE.SCARE
            self.redghost.mode = GHOSTMODE.SCARE
            self.blueghost.mode = GHOSTMODE.SCARE
            self.pinkghost.mode = GHOSTMODE.SCARE
            self.orangeghost.mode = GHOSTMODE.SCARE
    def renderall(self):
        """
        Draw the current game state on screen.
        Does nothing if isinitialized == False (pygame.init failed)
        """
        
        if not self.isinitialized:
            return
        if self.screenPage == 0:
            image = pygame.image.load(SCREENSPRITE[0])
            rect = image.get_rect()
            self.screen.blit(image,rect)
            pygame.display.flip()
            return
        if self.screenPage == 1:
            image = pygame.image.load(SCREENSPRITE[1])
            rect = image.get_rect()
            self.screen.blit(image, rect)
            pygame.display.flip()
            return
        if self.screenPage == 2:
            image = pygame.image.load(SCREENSPRITE[2])
            rect = image.get_rect()
            self.screen.blit(image, rect)
            pygame.display.flip()
            return
        if (self.isWin):
            self.gameWin()
            return
        if self.pacman.isDead:
            self.pacmanDie()
            return
        else:
            self.tilemap.update(self)
            self.tilemap.draw(self.screen)
            self.drawScore()



        pygame.display.flip()

    def drawScore(self):
        # print self.score
        if(self.biscuitamount == 0):
            self.isWin = True
        myfont = pygame.font.Font('font/game_over.ttf', 40)
        textsurface = myfont.render('SCORE : {0}'.format(self.score), False, (255, 255, 255))
        self.screen.blit(textsurface, (SCREENSIZE[0]/2-20,SCREENSIZE[1]-30))

    def gameWin(self):
        image = pygame.image.load(GAMEWINSPRITE)
        rect = image.get_rect()
        self.screen.blit(image, rect)
        pygame.display.flip()


    def clearScreen(self):
        self.screen.fill((0, 0, 0))

    def initialize(self):
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption(GAMENAME)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
        self.smallfont = pygame.font.Font(None, 40)
        self.tilemap = tmx.load("tmx/pacmanmap.tmx", self.screen.get_size())
        self.initPacman()
        self.initBiscuit()
        self.initPowerball()
        self.initGhost()
        self.isinitialized = True

    def updateDirection(self,char):
        if char == 'R':
            self.futureDirection = PACMANDIRECTION.RIGHT
        elif char == 'L':
            self.futureDirection = PACMANDIRECTION.LEFT
        elif char == 'W':
            self.futureDirection = PACMANDIRECTION.UP
        elif char == 'D':
            self.futureDirection = PACMANDIRECTION.DOWN



    def checkValidInput(self, x, y):
        if self.futureDirection == PACMANDIRECTION.RIGHT:
            return x+1, y

        elif self.futureDirection == PACMANDIRECTION.LEFT:
            return x - 1, y

        elif self.futureDirection == PACMANDIRECTION.UP:
            return x, y - 1

        elif self.futureDirection == PACMANDIRECTION.DOWN:
            return x, y + 1

    def redghostDie(self):
        posx = self.redghost.posx
        posy = self.redghost.posy
        self.createTimer(64,lambda : self.fireLaser(posx,posy))



    def blueghostDie(self):
        self.createWater()

    def pinkghostDie(self):
        self.createTrap(self.pinkghost.posx,self.pinkghost.posy)
        self.createTimer(48,lambda : self.releaseTrap())

    def orangeghostDie(self):
        self.blindPacman()


    def fireLaser(self,posx,posy):
        a = Laser((posx, posy), LASERSPRITE.LEFT, self.biscuitSprite)
        b = Laser((posx, posy), LASERSPRITE.RIGHT, self.biscuitSprite)
        c = Laser((posx, posy), LASERSPRITE.UP, self.biscuitSprite)
        d = Laser((posx, posy), LASERSPRITE.DOWN, self.biscuitSprite)

    def createWater(self):
        Water((self.blueghost.posx, self.blueghost.posy), self.biscuitSprite)

    def updateGhostPosition(self, prolog):

        self.redghost.updatePosition(prolog, self)
        self.blueghost.updatePosition(prolog, self)
        self.pinkghost.updatePosition(prolog, self)
        self.orangeghost.updatePosition(prolog, self)

    def updateGhostMode(self, mode):
        self.redghost.changeMode(mode,self.prolog)
        self.blueghost.changeMode(mode, self.prolog)
        self.pinkghost.changeMode(mode, self.prolog)
        self.orangeghost.changeMode(mode, self.prolog)

    def pacmanDie(self):
        image = pygame.image.load(GAMEOVERSPRITE)
        rect = image.get_rect()
        self.screen.blit(image,rect)
        pygame.display.flip()


    def blindPacman(self):
        if(self.isBlind):
            return
        blindLayer = tmx.SpriteLayer()
        Blind((self.pacman.posx,self.pacman.posy),blindLayer)
        self.tilemap.layers.append(blindLayer)
        self.isBlind = True

    def createTrap(self,posx,posy):
        print "create trap"
        Trap((self.pinkghost.posx,self.pinkghost.posy),self.biscuitSprite)
    def releaseTrap(self):
        self.pacman.movespeed = 1
        self.pacman.releaseTrap()
    def createTimer(self,time,fn):
        if(self.isTimerInit == True):
            return
        print "create timer"
        self.timerSec = time
        self.fn = fn
        self.isTimerInit = True

    def countDown(self,fn):
        self.timerSec -= 1
        if(self.timerSec == 1):
            self.isTimerInit = False
            self.callAction(fn)

    def callAction(self,fn):
        fn()
