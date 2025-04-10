from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
from utility import *

running = True
angle = 0
boundary = 50
dt = 0.016
print("Angle: ",angle)
velociraptor = Velociraptor([600,600],angle)
thescelosaurus = Thescelosaurus([667,600],angle)
thescelosaurus.detect_distance = boundary
time = 0
while running:
    print(time)
    time +=dt
    thescelosaurus.strat1(dt,velociraptor)
    velociraptor.cycle(dt,thescelosaurus)
    if(thescelosaurus.escaped):
        print(f"Thescelosaurus escaped! with boundary:",boundary)
        time = 0
        boundary-= 0.1
        velociraptor = Velociraptor([600,600],angle)
        thescelosaurus = Thescelosaurus([667,600],angle)
        thescelosaurus.detect_distance = boundary
        print(thescelosaurus)
        print(velociraptor)
    if(velociraptor.eat):
        running = False
        print("Maximum boundary:",boundary)


