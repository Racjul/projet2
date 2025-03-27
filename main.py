from animal import Animal
import math
from utility import *
from constants import *
DT = 1
print(calculate_velocity(5,math.pi/2))

if __name__ == "__main__":
    running = True
    animal = Animal([0,0])
    animal2 = Animal([1,1])
    animal.acceleration = 5
    animal.angular_velocity = math.pi/2
    print(animal.find_angle(animal2.pos) * 4)
    for i in range(10):
        animal.accelerate(DT)
        animal.move(DT)
        animal.rotate(DT,Orientation.RIGHT)
        print(animal)



