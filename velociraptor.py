from constants import *
import pygame
class Velociraptor:
    def __init__(self,pos,) -> None:
        self.image = pygame.image.load(VELOCIRAPTOR_IMAGE)
        self.pos = pos
    def show(self,screen):
        screen.blit(self.image,self.pos)
