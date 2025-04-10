
import pygame
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
import math
import sys
from utility import *

# pygame setup

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)
running = True
pygame.display.set_caption('Simulation projet 2')
velociraptor_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pos1 = [600,600]
pos2 = [667,600]
angle = 0
print("Angle: ",angle)
velociraptor = Velociraptor(pos1,angle)
thescelosaurus = Thescelosaurus(pos2,angle)
thescelosaurus.detect_distance = 30.29999999999972
print(f"Thescelosaurus: ",thescelosaurus)
print(f"Velociraptor: ",velociraptor)
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    thescelosaurus.draw_oriented_dot(screen)
    velociraptor.draw_oriented_dot(screen)


    # limits FPS to 60
    dt = clock.tick(60) / 1000

    print(f"Delta Time: {dt:.4f} seconds")

    velociraptor.cycle(dt,thescelosaurus,screen)
    thescelosaurus.strat1(dt,velociraptor,screen)
    remaining_time = max(0, 15 - int(thescelosaurus.totaldt))
    countdown = font.render(str(remaining_time), True, (0,0,0))
    text_rect = countdown.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
    screen.blit(countdown, text_rect)

    pygame.display.flip()

pygame.quit()
