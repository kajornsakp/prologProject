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


PACMANDIRECTION = enum(UP=["sprite/pacman-u-1.gif","sprite/pacman-u-2.gif",
                           "sprite/pacman-u-3.gif","sprite/pacman-u-4.gif",
                           "sprite/pacman-u-5.gif","sprite/pacman-u-6.gif",
                           "sprite/pacman-u-7.gif","sprite/pacman-u-8.gif"],
                       LEFT=["sprite/pacman-l-1.gif","sprite/pacman-l-2.gif",
                           "sprite/pacman-l-3.gif","sprite/pacman-l-4.gif",
                           "sprite/pacman-l-5.gif","sprite/pacman-l-6.gif",
                           "sprite/pacman-l-7.gif","sprite/pacman-l-8.gif"],
                       DOWN=["sprite/pacman-d-1.gif","sprite/pacman-d-2.gif",
                           "sprite/pacman-d-3.gif","sprite/pacman-d-4.gif",
                           "sprite/pacman-d-5.gif","sprite/pacman-d-6.gif",
                           "sprite/pacman-d-7.gif","sprite/pacman-d-8.gif"],
                       RIGHT=["sprite/pacman-r-1.gif","sprite/pacman-r-2.gif",
                           "sprite/pacman-r-3.gif","sprite/pacman-r-4.gif",
                           "sprite/pacman-r-5.gif","sprite/pacman-r-6.gif",
                           "sprite/pacman-r-7.gif","sprite/pacman-r-8.gif"])

GHOSTSPRITE = enum(RED=["sprite/ghost-red-1.gif","sprite/ghost-red-2.gif",
                        "sprite/ghost-red-3.gif","sprite/ghost-red-4.gif",
                        "sprite/ghost-red-5.gif","sprite/ghost-red-6.gif"],
                   LIGHTBLUE=["sprite/ghost-lightblue-1.gif", "sprite/ghost-lightblue-2.gif",
                        "sprite/ghost-lightblue-3.gif", "sprite/ghost-lightblue-4.gif",
                        "sprite/ghost-lightblue-5.gif", "sprite/ghost-lightblue-6.gif"],
                   PINK=["sprite/ghost-pink-1.gif", "sprite/ghost-pink-2.gif",
                        "sprite/ghost-pink-3.gif", "sprite/ghost-pink-4.gif",
                        "sprite/ghost-pink-5.gif", "sprite/ghost-pink-6.gif"],
                   ORANGE=["sprite/ghost-orange-1.gif", "sprite/ghost-orange-2.gif",
                        "sprite/ghost-orange-3.gif", "sprite/ghost-orange-4.gif",
                        "sprite/ghost-orange-5.gif", "sprite/ghost-orange-6.gif"])

GHOSTMODE = enum(SCARE=0,CHASE=1)
GHOSTDIRECTION = enum(UP=0,DOWN=1,LEFT=2,RIGHT=3)