import pygame

from Character import *
from Map import Map
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
        self.screenMode = SCREENMODE.MENU
        self.movespeed = 1
        self.prolog = PrologController()
        self.life = 3


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

        pinkghostSprite = tmx.SpriteLayer()
        pinkghostTmx = self.tilemap.layers['ghost'].find('pinkghost')[0]
        self.pinkghost = Ghost((pinkghostTmx.px,pinkghostTmx.py), GHOSTSPRITE.PINK,pinkghostSprite)
        self.tilemap.layers.append(pinkghostSprite)

        blueghostSprite = tmx.SpriteLayer()
        blueghostTmx = self.tilemap.layers['ghost'].find('blueghost')[0]
        self.blueghost = Ghost((blueghostTmx.px, blueghostTmx.py), GHOSTSPRITE.LIGHTBLUE, blueghostSprite)
        self.tilemap.layers.append(blueghostSprite)

        orangeghostSprite = tmx.SpriteLayer()
        orangeghostTmx = self.tilemap.layers['ghost'].find('orangeghost')[0]
        self.orangeghost = Ghost((orangeghostTmx.px, orangeghostTmx.py), GHOSTSPRITE.ORANGE, orangeghostSprite)
        self.tilemap.layers.append(orangeghostSprite)

    def initBiscuit(self):
        biscuitSprite = tmx.SpriteLayer()
        for biscuit in self.tilemap.layers['biscuit'].find('biscuit'):
            Biscuit((biscuit.px,biscuit.py),biscuitSprite)
        self.tilemap.layers.append(biscuitSprite)


    def initPowerball(self):
        powerballSprite = tmx.SpriteLayer()
        for powerball in self.tilemap.layers['biscuit'].find('powerball'):
            Powerball((powerball.px,powerball.py),powerballSprite)
        self.tilemap.layers.append(powerballSprite)

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
            self.renderall()
            self.pacman.updatePosition(self.prolog)
            self.updateGhostPosition(self.prolog, self.pacman)
            # self.checkLimit()
            # limit the redraw speed to 30 frames per second
            # print self.redghost.mode
            self.clock.tick(60)

    def changeMode(self,event):
        if event.mode == GHOSTMODE.CHASE:
            self.redghost.mode = GHOSTMODE.CHASE
            self.blueghost.mode = GHOSTMODE.CHASE
            self.pinkghost.mode = GHOSTMODE.CHASE
            self.orangeghost.mode = GHOSTMODE.CHASE
        elif event.mode == GHOSTMODE.SCARE:
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
        self.pacman.updateDirection(self.direction)


    def redghostDie(self):
        a = Laser((self.redghost.posx,self.redghost.posy),LASERSPRITE.LEFT,self.redghostSprite)
        b = Laser((self.redghost.posx,self.redghost.posy),LASERSPRITE.RIGHT, self.redghostSprite)
        c = Laser((self.redghost.posx,self.redghost.posy), LASERSPRITE.UP, self.redghostSprite)
        d = Laser((self.redghost.posx,self.redghost.posy), LASERSPRITE.DOWN, self.redghostSprite)


    def updateGhostPosition(self, prolog,pacman):
        # self.redghost.updatePosition(prolog, pacman)
        # self.blueghost.updatePosition()
        # self.pinkghost.updatePosition()
        # self.orangeghost.updatePosition()
        a = 0

    def checkLimit(self):
        print self.pacman.rect

    def pacmanDie(self):
        self.life -= 1
        self.pacman.rect.x = 0
        self.pacman.rect.y = 0


