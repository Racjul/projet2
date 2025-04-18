import pygame
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
import math
import sys
from utility import *

def run_simulation(detect_distance=None):
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    running = True
    pygame.display.set_caption('Simulation projet 2  - partie 2')

    # Initialize positions and objects
    pos_predator_A = [600, 650]
    pos_predator_B = [600, 550]
    pos_prey = [677, 600]
    dt=0.016
    angle = angle_between_points(pos_predator_A, pos_prey)
    predator_A = Velociraptor(pos_predator_A, angle)
    predator_B = Velociraptor(pos_predator_B, 2*math.pi - angle)
    prey = Thescelosaurus(pos_prey, 0)
    if detect_distance is not None:
        prey.detect_distance = detect_distance

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to wipe away anything from the last frame
        screen.fill("white")
        prey.draw_oriented_dot(screen)
        predator_A.draw_oriented_dot(screen)
        predator_B.draw_oriented_dot(screen)

        # Update simulation
        predator_A.strat_part1(dt, prey, screen)
        predator_B.strat_part1(dt, prey, screen)
        prey.strat_part2(dt, predator1=predator_A, predator2=predator_B, surface=screen)

        # Display countdown timer
        remaining_time = max(0, 15 - int(prey.totaldt))
        countdown = font.render(str(remaining_time), True, (0, 0, 0))
        text_rect = countdown.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
        screen.blit(countdown, text_rect)

        # Update the display
        pygame.display.flip()

        # Limit FPS to 60
        clock.tick(60)

    pygame.quit()
