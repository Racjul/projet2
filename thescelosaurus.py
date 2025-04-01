from constants import *
import pygame
from animal import Animal
from utility import *

class Thescelosaurus(Animal):
    def __init__(self,pos) -> None:
        super(Thescelosaurus,self).__init__(pos)
        self.image = pygame.image.load(THESCELOSAURUS_IMAGE)
        self.hunter_detected:bool = False

    @property
    def radius_of_rotation(self):
        return  T_RADIUS_OF_ROTATION
    
    @property
    def max_velocity(self):
        return T_MAX_VELOCITY

    @property
    def acceleration(self):
        return T_ACCELERATION

    def detect(self,animal:Animal):
        #TODO
        pass

    def __str__(self):
        return f"Thescelosaurus: \n Pos: {self.pos},\n Orientation: {self.orientation},\n Velocity: {self.velocity},\n Angular Velocity: {self.angular_velocity}\n----------------------------"

    def cycle(self, dt, animal):
        if not self.hunter_detected :
            self.detect(animal)
        else:
            #TODO
            self.accelerate(dt)
            self.move(dt)
