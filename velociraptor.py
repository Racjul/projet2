from constants import *
from animal import Animal
from utility import Direction, calculate_velocity, display_predator_win 

class Velociraptor(Animal):
    def __init__(self,pos,orientation=0) -> None:
        super(Velociraptor,self).__init__(pos,orientation)
        self.eat = False

    @property
    def radius_of_rotation(self):
        return  V_RADIUS_OF_ROTATION
    @property
    def max_velocity(self):
        return V_MAX_VELOCITY
    @property
    def acceleration(self):
        return V_ACCELERATION
    @property
    def isPrey(self):
        return False

    def strat_part1(self, dt, animal,screen=None):
        angle = self._find_wanted_angle(animal.pos)
        direction= self._find_direction(angle)
        self.angular_velocity = abs(self.orientation - angle)
        if direction== Direction.RIGHT:
            self.orientation+=self.angular_velocity *dt
        else:
            self.orientation-=self.angular_velocity * dt
        self.accelerate(dt)
        self.move(dt)
        if (self.can_eat(animal.pos)):
            if(screen is not None):
                display_predator_win(screen)
            self.eat = True




    def __str__(self):
        return f"Velociraptor: \n Pos: {self.pos},\n Orientation: {self.orientation},\n Velocity: {self.velocity},\n Angular Velocity: {self.angular_velocity}thescelosaurus.\n----------------------------"
    def can_eat(self,pos):
        if (pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2 <= EAT_DISTANCE:
            return True
        return False
