from constants import *
import pygame
from animal import Animal
from utility import Direction
from thescelosaurus import Thescelosaurus

class Velociraptor(Animal):
    def __init__(self,pos) -> None:
        super(Velociraptor,self).__init__(pos)
        self.image = pygame.image.load(VELOCIRAPTOR_IMAGE)

    @property
    def radius_of_rotation(self):
        return  V_RADIUS_OF_ROTATION
    @property
    def max_velocity(self):
        return V_MAX_VELOCITY
    @property
    def acceleration(self):
        return V_ACCELERATION

    def cycle(self, dt, animal):
        angle = self._find_wanted_angle(animal.pos)
        direction= self._find_orientation(animal.pos)
        self.angular_velocity = abs(self.orientation - angle)
        if direction== Direction.LEFT:
            self.orientation-=self.angular_velocity
        else:
            self.orientation+=self.angular_velocity
        self.accelerate(dt)
        self.move(dt)
        self.can_eat(animal.pos)


    def __str__(self):
        return f"Velociraptor: \n Pos: {self.pos},\n Orientation: {self.orientation},\n Velocity: {self.velocity},\n Angular Velocity: {self.angular_velocity}\n----------------------------"
    def can_eat(self,pos):
        if (pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2 <= EAT_DISTANCE:
            return True
        return False
