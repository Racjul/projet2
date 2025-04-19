from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
from utility import *
from pandas import DataFrame
from matplotlib import pyplot as plt


def simulate_and_plot(distance_between_predators=100,plot=True):
    running = True
    
# Initialize positions and objects
    pos_predator_A = [600, 600 + distance_between_predators/2]
    pos_predator_B = [600, 600 - distance_between_predators/2]
    pos_prey = [677, 600]
    time = 0
    dt=0.016
    boundary = 50
    angle = angle_between_points(pos_predator_A, pos_prey)

    predator_A = Velociraptor(pos_predator_A, angle)
    predator_B = Velociraptor(pos_predator_B, 2*math.pi - angle)
    prey = Thescelosaurus([677, 600], 0)

    prey.detect_distance = boundary

    result = {}
    while running:
        print(time)
        time += dt
        predator_A.strat_part1(dt, prey)
        predator_B.strat_part1(dt, prey)
        prey.strat_part2(dt, predator1=predator_A, predator2=predator_B)
        if prey.escaped:
            result[boundary] = 1
            time = 0
            boundary = round(boundary - 0.1, 2)
            if boundary == 15:
                running = False

            prey = Thescelosaurus([677, 600], 0)
            predator_A = Velociraptor([600, 600 + distance_between_predators/2], angle)
            predator_B = Velociraptor([600, 600 - distance_between_predators/2], 2*math.pi - angle)
            prey.detect_distance = boundary

        if predator_A.eat or predator_B.eat:
            result[boundary] = 0
            time = 0
            boundary = round(boundary - 0.1, 2)
            if boundary == 15:
                running = False

            prey = Thescelosaurus([677, 600], 0)
            predator_A = Velociraptor([600, 600 + distance_between_predators/2], angle)
            predator_B = Velociraptor([600, 600 - distance_between_predators/2], 2*math.pi - angle)
            prey.detect_distance = boundary

    # Plot the results
    x = list(result.keys())
    y = list(result.values())
    if plot:
        plt.scatter(x, y)
        plt.xlabel("Boundary")
        plt.ylabel("Escaped")
        plt.title("Fuite en fonction de la distance de détection")
        plt.show()
    # Print statistics
    print("Escaped count:", y.count(1))
    print("Eaten count:", y.count(0))
    print("Escape percentage:", y.count(1) / (y.count(1) + y.count(0)))

    return y.count(1) / (y.count(1) + y.count(0))


def find_optimal_distance():
    min_percentage = 1  
    optimal_distance = 0

    for distance in range(2, 201, 2):
        print(f"Testing distance: {distance}")
        escape_percentage = simulate_and_plot(distance_between_predators=distance, plot=False)
        
        if escape_percentage < min_percentage:
            min_percentage = escape_percentage
            optimal_distance = distance

    print(f"Least optimal distance: {optimal_distance} with escape percentage: {min_percentage * 100:.2f}%")
    return optimal_distance