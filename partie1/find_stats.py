from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
from utility import *
from pandas import DataFrame
from matplotlib import pyplot as plt

def simulate_and_plot(angle=0, boundary=50, dt=0.016):
    running = True
    print("Angle: ", angle)
    velociraptor = Velociraptor([600, 600], angle)
    thescelosaurus = Thescelosaurus([677, 600], angle)
    thescelosaurus.detect_distance = boundary
    time = 0

    result = {}
    while running:
        print(time)
        time += dt
        velociraptor.strat_part1(dt, thescelosaurus)
        thescelosaurus.strat_part1(dt, velociraptor)
        if thescelosaurus.escaped:
            print(f"Thescelosaurus escaped! with boundary:", boundary)
            result[boundary] = 1
            time = 0
            if boundary == 15:
                running = False
            boundary = round(boundary - 0.1, 2)
            velociraptor = Velociraptor([600, 600], angle)
            thescelosaurus = Thescelosaurus([667, 600], angle)
            thescelosaurus.detect_distance = boundary
            print(thescelosaurus)
            print(velociraptor)
        if velociraptor.eat:
            result[boundary] = 0
            time = 0
            boundary = round(boundary - 0.1, 2)
            if boundary == 15:
                running = False
            velociraptor = Velociraptor([600, 600], angle)
            thescelosaurus = Thescelosaurus([667, 600], angle)
            thescelosaurus.detect_distance = boundary

    # Plot the results
    x = list(result.keys())
    y = list(result.values())

    plt.scatter(x, y)
    plt.xlabel("Boundary")
    plt.ylabel("Escaped")
    plt.title("Fuite en fonction de la distance de détection")
    plt.show()

    # Print statistics
    print("Escaped count:", y.count(1))
    print("Eaten count:", y.count(0))
    print("Escape percentage:", y.count(1) / (y.count(1) + y.count(0)))

    return result
