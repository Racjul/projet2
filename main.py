from animal import Animal
import math
from utility import *
from constants import *
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus


if __name__ == "__main__":
    running = True
    time = 0
    hunter = Velociraptor([0,0])
    prey = Thescelosaurus([100,100])
    print(hunter)
    print(prey)
    while running:
        hunter.cycle(1,prey)
        prey.cycle(1,hunter)
        time+=DT
        if time == 100:
            running = False



