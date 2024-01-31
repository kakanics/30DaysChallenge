import pygame
import numpy as np

WIDTH, HEIGHT = 410, 400
CELL_SIZE = 8
GRID_SIZE = 100
BORDER_SIZE = 10
COLOR_BOX_SIZE = 10
COLOR_BOX_COUNT = 40

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = np.random.choice([0, 1], GRID_SIZE*GRID_SIZE *
                        3).reshape(GRID_SIZE, GRID_SIZE, 3)
selected_color = pygame.Color(255, 255, 255)


running = True
pressed = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = False
        if pressed:
            x, y = pygame.mouse.get_pos()
            if x < COLOR_BOX_COUNT * COLOR_BOX_SIZE and y < COLOR_BOX_SIZE:
                index = x // COLOR_BOX_SIZE
                hue = index * (360 / COLOR_BOX_COUNT)
                selected_color.hsva = (hue, 100, 100, 100)
            elif x >= BORDER_SIZE and y >= BORDER_SIZE and x < WIDTH - BORDER_SIZE and y < HEIGHT - BORDER_SIZE:
                cell_x = (x - BORDER_SIZE) // CELL_SIZE
                cell_y = (y - BORDER_SIZE) // CELL_SIZE
                # Only use the RGB values, not the A value
                grid[cell_y, cell_x] = selected_color[:3]

    screen.fill((0, 0, 0))

    # Draw the color palette
    for i in range(COLOR_BOX_COUNT):
        hue = i * (360 / COLOR_BOX_COUNT)
        color = pygame.Color(0)
        color.hsva = (hue, 100, 100, 100)
        pygame.draw.rect(screen, color, pygame.Rect(
            i * COLOR_BOX_SIZE, 0, COLOR_BOX_SIZE, COLOR_BOX_SIZE))

    pygame.draw.rect(screen, selected_color, pygame.Rect(
        0, HEIGHT - COLOR_BOX_SIZE, COLOR_BOX_SIZE, COLOR_BOX_SIZE))

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = grid[i, j] if any(grid[i, j]) else (0, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(
                BORDER_SIZE + j*CELL_SIZE, BORDER_SIZE + i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

pygame.quit()
