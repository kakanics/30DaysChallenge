import pygame
import math
import random

# Initialize Pygame
pygame.init()

window_size = (500, 500)

window = pygame.display.set_mode(window_size)


waves = [
    {"amplitude": 10, "frequency": 0.01, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.01},
    {"amplitude": 4, "frequency": 0.02, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.02},
    {"amplitude": 12, "frequency": 0.03, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.03},
    {"amplitude": 18, "frequency": 0.04, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.04},
    {"amplitude": 3, "frequency": 0.05, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.05},
    {"amplitude": 2, "frequency": 0.06, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.06},
    {"amplitude": 1, "frequency": 0.07, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.07},
    {"amplitude": 5, "frequency": 0.08, "phase": random.uniform(
        0, 2 * math.pi), "speed": 0.08},
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    for x in range(window_size[0]):
        y = window_size[1] // 2
        for wave in waves:
            y -= wave["amplitude"] * \
                math.sin(wave["frequency"] * x + wave["phase"])

        y = max(min(y, window_size[1]), 0)

        pygame.draw.line(window, (0, 0, 255), (x, y), (x, window_size[1]))

    for wave in waves:
        wave["phase"] += wave["speed"]/10
        wave["phase"] += random.uniform(0, 0.05)

    pygame.display.update()

pygame.quit()
