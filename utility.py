import math
from enum import Enum
import pygame
from constants import *


class Direction(Enum):
    RIGHT = "RIGHT"
    LEFT= "LEFT"
def inverseDirection(direction:Direction):
    return Direction.RIGHT if direction == Direction.LEFT else Direction.LEFT
def calculate_velocity(velocity, angle):
    return velocity * math.cos(angle), velocity * math.sin(angle)
def display_predator_win(screen):
    pygame.display.set_caption("Game Over")
    font = pygame.font.Font(None, 80)  # Use default font, size 80
    text = font.render("The Predator Wins!", True, RED)  # Render text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

    running = True
    while running:
        screen.fill(BLACK)  
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        screen.blit(text, text_rect)

        pygame.display.flip()  
    pygame.quit()

def display_prey_win(screen):
    pygame.display.set_caption("Game Over")
    font = pygame.font.Font(None, 80)  
    text = font.render("La proie a gagné!", True, GREEN)  
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  

    running = True
    while running:
        screen.fill(BLACK)  
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw the text
        screen.blit(text, text_rect)

        pygame.display.flip()  
    pygame.quit()
def angle_between_points(x,y ):
    return math.atan2(y[1] - y[0], x[1] - x[0])
        


