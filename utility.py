import math
from enum import Enum

class Direction(Enum):
    RIGHT = 1
    LEFT= 2
def calculate_velocity(velocity, angle):
    return velocity * math.cos(angle), velocity * math.sin(angle)

