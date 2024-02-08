import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
G = 6.67430e-11  # Gravitational constant
RADIUS = 10
MASS = 10
PIXELS_PER_METER = 1e4  # Scale for converting between pixels and meters

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

spheres = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            spheres.append({'pos': np.array([x, y], dtype=float), 'vel': np.zeros(
                2), 'mass': MASS, 'radius': RADIUS})

    # Update sphere velocities based on gravitational forces
    for i, sphere1 in enumerate(spheres):
        for j, sphere2 in enumerate(spheres):
            if i != j:
                r = sphere2['pos'] - sphere1['pos']
                r_meters = r / PIXELS_PER_METER
                force = G * sphere1['mass'] * \
                    sphere2['mass'] / np.linalg.norm(r_meters)**2
                acceleration = force / \
                    sphere1['mass'] * r_meters / np.linalg.norm(r_meters)
                sphere1['vel'] += acceleration

    # Handle collisions
    i = 0
    while i < len(spheres):
        sphere1 = spheres[i]
        j = i + 1
        while j < len(spheres):
            sphere2 = spheres[j]
            r = sphere2['pos'] - sphere1['pos']
            if np.linalg.norm(r) < sphere1['radius'] + sphere2['radius']:
                new_mass = 0.75*(sphere1['mass'] + sphere2['mass'])
                new_radius = 0.75 * (sphere1['radius'] + sphere2['radius'])
                new_vel = (sphere1['vel'])
                new_pos = (sphere1['pos'])
                spheres.append({'pos': new_pos, 'vel': new_vel,
                               'mass': new_mass, 'radius': new_radius})
                del spheres[j]
                del spheres[i]
                break
            else:
                j += 1
        else:
            i += 1

    for sphere in spheres:
        sphere['pos'] += sphere['vel']

    screen.fill((0, 0, 0))
    for sphere in spheres:
        pygame.draw.circle(screen, (255, 255, 255), (int(
            sphere['pos'][0]), int(sphere['pos'][1])), int(sphere['radius']))
    pygame.display.flip()
