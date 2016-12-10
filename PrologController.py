from pyswip import Prolog
from PacmanConstant import *


class PrologController:
    def __init__(self):
        self.p = Prolog()
        self.p.consult('prolog/prolog-ai.pl')


    def movePacman(self, x, y):
        q = 'movePacman(' + str(x) + ',' + str(y) + ')'
        print q
        result = self.p.query(q)
        list(result)
        print list(self.p.query('pacman(X,Y,_)'))

    def moveGhost(self, x, y, ghostType):
        if ghostType == GHOSTSPRITE.RED:
            return self.moveRedGhost(x, y)
        elif ghostType == GHOSTSPRITE.LIGHTBLUE:
            return self.moveBlueGhost(x, y)
        elif ghostType == GHOSTSPRITE.PINK:
            return self.movePinkGhost(x, y)
        elif ghostType == GHOSTSPRITE.ORANGE:
            return self.moveOrangeGhost(x,y)

    def moveRedGhost(self, x, y):
        print list(self.p.query('ghost(X,Y,red,_)'))

        ghost = list(self.p.query('moveRedGhost'))

        prev = list(self.p.query('ghostPrev(X1,Y1,red)'))
        curr = list(self.p.query('ghost(X2,Y2,red,W)'))
        # print(curr)
        print(prev)
        # print list(self.p.query('pacman(X,Y,Z)'))
        # print curr[0]['Y2']
        print curr
        return self.getDirection(curr[0]['X2'], curr[0]['Y2'], prev[0]['X1'], prev[0]['Y1'])
        # return 0

    def moveBlueGhost(self, x, y):
        b = "moveBlueGhost(" + str(x) + "," + str(y) + ")"

        ghost = list(self.p.query(b))
        prev = list(self.p.query('ghostPrev(X,Y,blue)'))
        curr = list(self.p.query('ghost(X,Y,blue,W)'))
        return self.getDirection(curr[0]['X'], curr[0]['Y'], prev[0]['X'], prev[0]['Y'])

    def movePinkGhost(self, x, y):
        p = "movePinkGhost(" + str(x) + "," + str(y) + ")"
        ghost = list(self.p.query(p))
        prev = list(self.p.query('ghostPrev(X,Y,pink)'))
        curr = list(self.p.query('ghost(X,Y,pink,W)'))
        return self.getDirection(curr[0]['X'], curr[0]['Y'], prev[0]['X'], prev[0]['Y'])

    def moveOrangeGhost(self,x,y):
        ghost = list(self.p.query("moveOrangeGhost"))
        prev = list(self.p.query('ghostPrev(X,Y,orange)'))
        curr = list(self.p.query('ghost(X,Y,orange,W)'))
        return self.getDirection(curr[0]['X'], curr[0]['Y'], prev[0]['X'], prev[0]['Y'])

    def getDirection(self, x1, y1, x2, y2):
        if x1 == x2 and y1 - y2 < 0:
            return GHOSTDIRECTION.UP
        elif x1 == x2 and y1 - y2 > 0:
            return GHOSTDIRECTION.DOWN
        elif y1 == y2 and x1 - x2 < 0:
            return GHOSTDIRECTION.LEFT
        elif y1 == y2 and x1 - x2 > 0:
            return GHOSTDIRECTION.RIGHT

    def getPacman(self):
        return list(self.p.query('pacman(X,Y,_)'))

