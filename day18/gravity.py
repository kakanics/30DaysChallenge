import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
SUN_RADIUS = 50
PLANET_RADIUS = 10
GRAVITY = 15
sun_pos = [WIDTH / 2, HEIGHT / 2]
planet_pos = [WIDTH / 2, HEIGHT / 2 - 200]
planet_vel = [4, 4]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx = sun_pos[0] - planet_pos[0]
    dy = sun_pos[1] - planet_pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    force = GRAVITY * (SUN_RADIUS * PLANET_RADIUS) / distance**2
    angle = math.atan2(dy, dx)
    force_x = force * math.cos(angle)
    force_y = force * math.sin(angle)

    planet_vel[0] += force_x
    planet_vel[1] += force_y
    planet_pos[0] += planet_vel[0]
    planet_pos[1] += planet_vel[1]

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (int(
        sun_pos[0]), int(sun_pos[1])), SUN_RADIUS)
    pygame.draw.circle(screen, (0, 0, 255), (int(
        planet_pos[0]), int(planet_pos[1])), PLANET_RADIUS)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
