import pygame
from abc import ABC, abstractmethod
from constants import *
import math
import random 
from utility import *

class Animal(ABC):
    
    def __init__(self,pos) -> None:
        self.__image =pygame.image.load(VELOCIRAPTOR_IMAGE)
        self._pos = pos
        self._orientation = float(0)
        self._velocity = float(0)
        self._angular_velocity =float(0)

    
    @property
    def pos(self):
        return self._pos
    @property
    def orientation(self):
        return self._orientation
  
    @property 
    def velocity(self):
        return self._velocity
    @property 
    def angular_velocity(self):
        return self._angular_velocity
    
    @property
    @abstractmethod
    def radius_of_rotation(self):
        return float(0)

    @property
    @abstractmethod
    def max_velocity(self):
        return float(0)
    @property
    @abstractmethod
    def acceleration(self):
        return float(0)

    @orientation.setter
    def orientation(self,orientation):
        self._orientation = orientation//2*math.pi

    @angular_velocity.setter
    def angular_velocity(self,angular_velocity):
        if (self._find_max_rotation() -angular_velocity >= 0):
            self._angular_velocity = angular_velocity
        else:
            self._angular_velocity = self._find_max_rotation()


    @abstractmethod
    def __str__(self):
        return f" Pos: {self.pos},\n Orientation: {self.orientation},\n Velocity: {self.velocity},\n Angular Velocity: {self.angular_velocity}\n----------------------------"

    @abstractmethod
    def cycle(self,dt,animal):
        pass

    def show(self,screen):
        screen.blit(self.__image,self._pos)

    def rotate(self,dt,direction:Direction):
        self._angular_velocity += math.pi/2 * dt
        if direction == Direction.RIGHT:
            self._angular_velocity += math.pi/2 * dt
        else:
            self._orientation += self._angular_velocity * dt
        self.orientation = self._orientation % 2*math.pi

    def move(self,dt):
        velocity = calculate_velocity(self._velocity,self._orientation)
        self._pos[0] +=  velocity[0]* dt
        self._pos[1] +=  velocity[1]* dt

    def accelerate(self,dt:float):
        if(self._velocity+ self.acceleration*dt < self.max_velocity):
            self._velocity += self.acceleration*dt
        else:
            self._velocity = self.max_velocity

    def _find_wanted_angle(self,pos):
        return math.atan2(pos[1]-self._pos[1],pos[0]-self._pos[0])%(2*math.pi)

    def _find_orientation(self,wanted_angle):
        if wanted_angle > self._orientation:
            if wanted_angle - self._orientation < math.pi:
                return Direction.RIGHT
            else:
                return Direction.LEFT
        else:
            if self._orientation - wanted_angle < math.pi:
                return Direction.LEFT
            else:
                return Direction.RIGHT
    def _find_max_rotation(self):
        return self._velocity/ self.radius_of_rotation 

    def _find_distance(self,pos):
        return math.sqrt((pos[0]-self._pos[0])**2 + (pos[1]-self._pos[1])**2)

    
        
