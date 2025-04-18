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
    pygame.display.set_caption('Simulation projet 2')

    # Initialize positions and objects
    pos1 = [600, 600]
    pos2 = [677, 600]
    dt=0.016
    angle = 0
    velociraptor = Velociraptor(pos1, angle)
    thescelosaurus = Thescelosaurus(pos2, angle)
    if detect_distance is not None:
        thescelosaurus.detect_distance = detect_distance

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to wipe away anything from the last frame
        screen.fill("white")
        thescelosaurus.draw_oriented_dot(screen)
        velociraptor.draw_oriented_dot(screen)

        # Update simulation
        velociraptor.strat_part1(dt, thescelosaurus, screen)
        thescelosaurus.strat_part1(dt, velociraptor, screen)

        # Display countdown timer
        remaining_time = max(0, 15 - int(thescelosaurus.totaldt))
        countdown = font.render(str(remaining_time), True, (0, 0, 0))
        text_rect = countdown.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
        screen.blit(countdown, text_rect)

        # Update the display
        pygame.display.flip()

        # Limit FPS to 60
        clock.tick(60)

    pygame.quit()
