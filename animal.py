import pygame
from abc import ABC, abstractmethod
from constants import *
import math
import random 
from utility import *

class Animal(ABC):

    def __init__(self,pos,orientation:float) -> None:
        self._pos = pos
        self._orientation = orientation
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
    def radius_of_rotation(self)->float:
        pass

    @property
    @abstractmethod
    def isPrey(self)->bool:
        pass

    @property
    @abstractmethod
    def max_velocity(self)->float:
        pass

    @property
    @abstractmethod
    def acceleration(self)->float:
        pass

    @orientation.setter
    def orientation(self,orientation):
        self._orientation = orientation%(2*math.pi)

    @angular_velocity.setter
    def angular_velocity(self,angular_velocity):
        if (self._find_max_rotation() -angular_velocity >= 0):
            self._angular_velocity = angular_velocity
        else:
            self._angular_velocity = self._find_max_rotation()

    @abstractmethod
    def __str__(self)->str:
        pass

    def rotate(self,dt,direction):
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

    # Function to draw the dot with an arrow
    def draw_oriented_dot( self,surface):
        if self.isPrey:
            color = BLUE
        else:
            color= RED
        x, y = self.pos
        pygame.draw.circle(surface, color, (x, y), RADIUS)

        arrow_x = x + ARROW_LENGHT * math.cos(self.orientation)
        arrow_y = y + ARROW_LENGHT * math.sin(self.orientation)

        pygame.draw.line(surface, BLACK, (x, y), (arrow_x, arrow_y), ARROW_SIZE)

        angle1 = self.orientation+ math.pi * 5 / 6  
        angle2 = self.orientation- math.pi * 5 / 6   
        point1 = (arrow_x + ARROW_HEAD_SIZE * math.cos(angle1), arrow_y + ARROW_HEAD_SIZE * math.sin(angle1))
        point2 = (arrow_x + ARROW_HEAD_SIZE * math.cos(angle2), arrow_y + ARROW_HEAD_SIZE * math.sin(angle2))

        pygame.draw.polygon(surface, BLACK, [(arrow_x, arrow_y), point1, point2])


    
        
