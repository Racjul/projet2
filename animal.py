import pygame
from constants import *
class Animal:
    def __init__(self,pos) -> None:
        self.image =pygame.image.load(VELOCIRAPTOR_IMAGE)
        self.pos = pos
        self.orientation = 90
        pass

    def show(self,screen):
        screen.blit(self.image,self.pos)
    def move(self,x,y,dt):
        self.pos.x += x * dt
        self.pos.y += y * dt
