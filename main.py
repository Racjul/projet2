from animal import Animal
import math
from utility import *
from constants import *
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus


if __name__ == "__main__":
    running = True
    chasseur = Velociraptor([0,0])
    proie = Thescelosaurus([100,100])
    print(chasseur)
    print(proie)

    while running:
        if chasseur.can_eat(proie.pos):
            print("Velociraptor a mange Thescelosaurus")
            running = False
        


