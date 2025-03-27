import pygame
from constants import *
import math
import random 
from utility import *
class Animal:
    def __init__(self,pos) -> None:
        self.image =pygame.image.load(VELOCIRAPTOR_IMAGE)
        self.pos = pos
        self.orientation = float(0)
        self.acceleration = float(0)
        self.velocity = float(0)
        self.angular_velocity =float(0)
    def __str__(self):
        return f"Pos: {self.pos}, Orientation: {self.orientation}, Velocity: {self.velocity}, Angular Velocity: {self.angular_velocity}"
    def show(self,screen):
        screen.blit(self.image,self.pos)
    def rotate(self,dt,orientation:Orientation):
        self.angular_velocity += math.pi/2 * dt
        if orientation == Orientation.RIGHT:
            self.angular_velocity += math.pi/2 * dt
        else:
            self.orientation += self.angular_velocity * dt
        self.orientation = self.orientation % 2*math.pi
    def move(self,dt):
        velocity = calculate_velocity(self.velocity,self.orientation)
        self.pos[0] +=  velocity[0]* dt
        self.pos[1] +=  velocity[1]* dt

    def accelerate(self,dt:float):
        self.velocity += self.acceleration*dt

    def find_angle(self,pos):
        return math.atan2(pos[1]-self.pos[1],pos[0]-self.pos[0])%(2*math.pi)
    def find_orientation(self,pos):
        wanted_angle = self.find_angle(pos)
        if wanted_angle > self.orientation:
            if wanted_angle - self.orientation < math.pi:
                return Orientation.RIGHT
            else:
                return Orientation.LEFT
        else:
            if self.orientation - wanted_angle < math.pi:
                return Orientation.LEFT
            else:
                return Orientation.RIGHT

    def find_distance(self,pos):
        return math.sqrt((pos[0]-self.pos[0])**2 + (pos[1]-self.pos[1])**2)
        
