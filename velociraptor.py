from constants import *
import pygame
from animal import Animal

class Velociraptor(Animal):
    def __init__(self,pos) -> None:
        self.image = pygame.image.load(VELOCIRAPTOR_IMAGE)
        self.pos = pos
        self.orientation = 0

