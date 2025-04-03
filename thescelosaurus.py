from constants import *
import pygame
from animal import Animal
from utility import Direction,calculate_velocity
import math
import random 
import pygame

class Thescelosaurus(Animal):
    def __init__(self,pos,orientation=0) -> None:
        super(Thescelosaurus,self).__init__(pos,orientation)
        self.hunter_detected:bool = False
        self._detect_distance = random.uniform(15,50)

    @property
    def radius_of_rotation(self):
        return  T_RADIUS_OF_ROTATION

    @property
    def detect_distance(self):
        return self._detect_distance
    @detect_distance.setter
    def detect_distance(self,detect_distance:float):
        self._detect_distance = detect_distance

    @property
    def isPrey(self):
        return True

    @property
    def max_velocity(self):
        return T_MAX_VELOCITY


    @property
    def acceleration(self):
        return T_ACCELERATION

    def detect(self,animal:Animal):
        return True if  self._find_distance(animal.pos) < self._detect_distance else False

    def __str__(self):
        return f"Thescelosaurus: \n Pos: {self.pos},\n Orientation: {self.orientation},\n Velocity: {self.velocity},\n Angular Velocity: {self.angular_velocity}\n----------------------------"
    def straight_line(self, dt, animal,surface=None):
        if not self.hunter_detected :
            if surface is not None:
                pygame.draw.circle(surface, GREEN, (int(self.pos[0]),int(self.pos[1])), int(self.detect_distance))
            is_detected = self.detect(animal)
            self.hunter_detected = is_detected
        else:
            self.accelerate(dt)
            self.move(dt)
       
    def strat1(self, dt, animal,surface=None):
        if not self.hunter_detected :
            if surface is not None:
                pygame.draw.circle(surface, GREEN, (int(self.pos[0]),int(self.pos[1])), int(self.detect_distance))
            is_detected = self.detect(animal)
            self.hunter_detected = is_detected
        else:
            self.accelerate(dt)
            if(self._find_distance(animal.pos) < 40):
                self.orientation += self._find_max_rotation()* dt
            self.move(dt)

