def enum(**enums):
    return type('Enum', (), enums)

DIRECTION = enum(UP='W',LEFT='L',DOWN='D',RIGHT='R')
GAMENAME = "Pac Man"
SCREENWIDTH = 28
SCREENHEIGHT = 33
SCREENSIZE = (448,528)
#SCREENSIZE = (48,48)
Color = enum(WHITE=(255,255,255),
             BLACK=(0,0,0),
             RED=(255,0,0),
             GREEN=(0,255,0),
             BLUE=(0,0,255),
             YELLOW=(255,255,0),
             ORANGE=(255,102,51),
             LIGHTBLUE=(0,255,255),
             PINK=(255,102,204))

SCREENMODE = enum(MENU=0,GAME=1,GAMEOVER=2)

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y


PACMANDIRECTION = enum(UP=["sprite/pacman-u-1.png","sprite/pacman-u-2.png",
                           "sprite/pacman-u-3.png","sprite/pacman-u-4.png",
                           "sprite/pacman-u-5.png","sprite/pacman-u-6.png",
                           "sprite/pacman-u-7.png","sprite/pacman-u-8.png"],
                       LEFT=["sprite/pacman-l-1.png","sprite/pacman-l-2.png",
                           "sprite/pacman-l-3.png","sprite/pacman-l-4.png",
                           "sprite/pacman-l-5.png","sprite/pacman-l-6.png",
                           "sprite/pacman-l-7.png","sprite/pacman-l-8.png"],
                       DOWN=["sprite/pacman-d-1.png","sprite/pacman-d-2.png",
                           "sprite/pacman-d-3.png","sprite/pacman-d-4.png",
                           "sprite/pacman-d-5.png","sprite/pacman-d-6.png",
                           "sprite/pacman-d-7.png","sprite/pacman-d-8.png"],
                       RIGHT=["sprite/pacman-r-1.png","sprite/pacman-r-2.png",
                           "sprite/pacman-r-3.png","sprite/pacman-r-4.png",
                           "sprite/pacman-r-5.png","sprite/pacman-r-6.png",
                           "sprite/pacman-r-7.png","sprite/pacman-r-8.png"])

REDPACMANDIRECTION = enum(UP=["sprite/pacman-u-1-red.png","sprite/pacman-u-2-red.png",
                           "sprite/pacman-u-3-red.png","sprite/pacman-u-4-red.png",
                           "sprite/pacman-u-5-red.png","sprite/pacman-u-6-red.png",
                           "sprite/pacman-u-7-red.png","sprite/pacman-u-8-red.png"],
                       LEFT=["sprite/pacman-l-1-red.png","sprite/pacman-l-2-red.png",
                           "sprite/pacman-l-3-red.png","sprite/pacman-l-4-red.png",
                           "sprite/pacman-l-5-red.png","sprite/pacman-l-6-red.png",
                           "sprite/pacman-l-7-red.png","sprite/pacman-l-8-red.png"],
                       DOWN=["sprite/pacman-d-1-red.png","sprite/pacman-d-2-red.png",
                           "sprite/pacman-d-3-red.png","sprite/pacman-d-4-red.png",
                           "sprite/pacman-d-5-red.png","sprite/pacman-d-6-red.png",
                           "sprite/pacman-d-7-red.png","sprite/pacman-d-8-red.png"],
                       RIGHT=["sprite/pacman-r-1-red.png","sprite/pacman-r-2-red.png",
                           "sprite/pacman-r-3-red.png","sprite/pacman-r-4-red.png",
                           "sprite/pacman-r-5-red.png","sprite/pacman-r-6-red.png",
                           "sprite/pacman-r-7-red.png","sprite/pacman-r-8-red.png"])
GHOSTSPRITE = enum(RED=["sprite/ghost-red-1.png","sprite/ghost-red-2.png",
                        "sprite/ghost-red-3.png","sprite/ghost-red-4.png",
                        "sprite/ghost-red-5.png","sprite/ghost-red-6.png"],
                   LIGHTBLUE=["sprite/ghost-lightblue-1.png", "sprite/ghost-lightblue-2.png",
                        "sprite/ghost-lightblue-3.png", "sprite/ghost-lightblue-4.png",
                        "sprite/ghost-lightblue-5.png", "sprite/ghost-lightblue-6.png"],
                   PINK=["sprite/ghost-pink-1.png", "sprite/ghost-pink-2.png",
                        "sprite/ghost-pink-3.png", "sprite/ghost-pink-4.png",
                        "sprite/ghost-pink-5.png", "sprite/ghost-pink-6.png"],
                   ORANGE=["sprite/ghost-orange-1.png", "sprite/ghost-orange-2.png",
                        "sprite/ghost-orange-3.png", "sprite/ghost-orange-4.png",
                        "sprite/ghost-orange-5.png", "sprite/ghost-orange-6.png"])

LASERSPRITE = enum(LEFT=["sprite/laser-l-1.png","sprite/laser-l-2.png",
                         "sprite/laser-l-3.png"],
                   RIGHT=["sprite/laser-r-1.png","sprite/laser-r-2.png",
                         "sprite/laser-r-3.png"],
                   UP=["sprite/laser-u-1.png", "sprite/laser-u-2.png",
                          "sprite/laser-u-3.png"],
                   DOWN=["sprite/laser-d-1.png", "sprite/laser-d-2.png",
                          "sprite/laser-d-3.png"])

WATERSPRITE = enum(WATER=["sprite/water-splash-1.png", "sprite/water-splash-2.png",
                        "sprite/water-splash-3.png", "sprite/water-splash-4.png",
                        "sprite/water-splash-5.png", "sprite/water-splash-6.png",
                          "sprite/water-splash-7.png"])

BLINDSPRITE = "sprite/blind-mask.png"
TRAPSPRITE = "sprite/trap.png"
SCREENSPRITE = ["sprite/screen-1.gif","sprite/screen-2.gif","sprite/screen-3.gif"]
GAMEOVERSPRITE = "sprite/screen-gameover.gif"
GAMEWINSPRITE = "sprite/screen-gamewin.gif"
FN = enum(LASER=0,TRAP=1)
GHOSTMODE = enum(SCARE=0,CHASE=1)
GHOSTDIRECTION = enum(UP=0,DOWN=1,LEFT=2,RIGHT=3)

