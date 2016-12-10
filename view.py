import pygame

from Character import *
from Map import Map
from PrologController import PrologController
from PacmanConstant import *
from eventmanager import *
import tmx.tmx as tmx
from PrologController import PrologController



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
            self.updateDirection(event.char)
        elif isinstance(event, QuitEvent):
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event,ChangeModeEvent):
            self.changeMode(event)
        elif isinstance(event,PacmanDieEvent):
            self.pacmanDie()
        elif isinstance(event, TickEvent):
            if(self.isTimerInit):
                self.countDown(self.fn)
            self.count += 1
            if(self.count == 16):
                self.pacman.updateDirection(self.direction)
                self.count = 0
            self.renderall()
            self.pacman.updatePosition(self.prolog)
            self.updateGhostPosition(self.prolog, self.pacman)
            self.clock.tick(60)

    def changeMode(self,event):
        if event.mode == GHOSTMODE.CHASE:
            self.pacman.mode = GHOSTMODE.CHASE
            self.redghost.mode = GHOSTMODE.CHASE
            self.blueghost.mode = GHOSTMODE.CHASE
            self.pinkghost.mode = GHOSTMODE.CHASE
            self.orangeghost.mode = GHOSTMODE.CHASE
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


        self.tilemap.update(self)
        self.tilemap.draw(self.screen)

        pygame.display.flip()

    def renderMenu(self):
        menuText = self.smallfont.render('Main menu',True,Color.WHITE)
        self.screen.blit(menuText,(SCREENSIZE[0]/3,20))

    def renderGame(self):
        self.screen.fill(Color.WHITE)

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
            self.direction = PACMANDIRECTION.RIGHT
        elif char == 'L':
            self.direction = PACMANDIRECTION.LEFT
        elif char == 'W':
            self.direction = PACMANDIRECTION.UP
        elif char == 'D':
            self.direction = PACMANDIRECTION.DOWN
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

    def updateGhostPosition(self, prolog,pacman):

        self.redghost.updatePosition(prolog, pacman)
        self.blueghost.updatePosition(prolog, pacman)
        self.pinkghost.updatePosition(prolog, pacman)
        self.orangeghost.updatePosition(prolog, pacman)


    def pacmanDie(self):
        self.life -= 1
        self.pacman.rect.x = 0
        self.pacman.rect.y = 0


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
