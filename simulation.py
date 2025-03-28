import pygame
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Simulation projet 2')
velociraptor_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

velociraptor = Velociraptor(velociraptor_pos)
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    velociraptor.show(screen)
    #pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        velociraptor.pos.y -= 300 * dt
    if keys[pygame.K_s]:
        velociraptor.pos.y += 300 * dt
    if keys[pygame.K_a]:
        velociraptor.pos.x -= 300 * dt
    if keys[pygame.K_d]:
        velociraptor.pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
