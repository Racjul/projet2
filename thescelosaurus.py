from constants import *
import pygame
from animal import Animal
from utility import Direction,calculate_velocity, ending_screen,ending_screen1, inverseDirection
import math
import random 
import pygame

class Thescelosaurus(Animal):
    def __init__(self,pos,orientation=0) -> None:
        super(Thescelosaurus,self).__init__(pos,orientation)
        self.hunter_detected:bool = False
        self._detect_distance = random.uniform(15,50)
        self._rotated_distance = 0
        self._rotating = False
        self._able_to_rotate = True
        self.totaldt =0
        self.escaped = False 
        self._wanted_angle = 0

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
        return True if  self.find_distance(animal.pos) < self._detect_distance else False

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

            distance = self.find_distance(animal.pos)

            if  distance < T_RESET_DISTANCE and self._able_to_rotate and not self._rotating:
                self._rotating = True
                angle =  animal.orientation
                self._direction= self._find_direction(angle)
                self._wanted_angle =(T_ROTATION_ANGLE -abs(animal.orientation-self.orientation) )% (2*math.pi)
                print(self._direction)


            elif  distance >= T_RESET_DISTANCE :
                self._able_to_rotate = True

            if(self._rotating):
                self.angular_velocity = self.find_max_rotation()
                self._rotated_distance += dt * self.angular_velocity
                self.rotate(dt,self._direction)
                if(self._rotated_distance >= self._wanted_angle):
                    self._rotated_distance = 0
                    self._rotating = False
                    self._able_to_rotate = False
                    print("Rotated")

            self.accelerate(dt)
            self.move(dt)
            self.totaldt += dt
            if(self.totaldt >=15):
                if(surface is not None):
                    ending_screen1(surface)
                self.escaped = True

