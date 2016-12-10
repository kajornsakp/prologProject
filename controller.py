import pygame
import model
from eventmanager import *

class Keyboard(object):

    def __init__(self, evManager, model):
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model

    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.evManager.Post(ClockEvent())
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        if event.key == pygame.K_LEFT:
                            self.evManager.Post(InputEvent('L',None))
                        elif event.key == pygame.K_RIGHT:
                            self.evManager.Post(InputEvent('R',None))
                        elif event.key == pygame.K_UP:
                            self.evManager.Post(InputEvent('W',None))
                        elif event.key == pygame.K_DOWN:
                            self.evManager.Post(InputEvent('D',None))
                        # self.evManager.Post(InputEvent(event.unicode, None))

