import pygame
import random
import time
import colorsys

pygame.init()
window_size = (300, 300)
grid_size = 3
window = pygame.display.set_mode(window_size)

# Create a 2D list to represent the state of each box in the grid
grid = [[(0, 0, 0) for _ in range(window_size[1] // grid_size)]
        for _ in range(window_size[0] // grid_size)]


def draw_grid():
    for i, row in enumerate(grid):
        for j, color in enumerate(row):
            pygame.draw.rect(window, color, (i * grid_size,
                             j * grid_size, grid_size, grid_size))


def move_down():
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1, 0, -1):
            if grid[i][j] == (0, 0, 0) and grid[i][j - 1] != (0, 0, 0):
                grid[i][j], grid[i][j - 1] = grid[i][j - 1], grid[i][j]
            elif grid[i][j] != (0, 0, 0) and grid[i][j - 1] != (0, 0, 0):
                # Randomly decide whether to check left or right first
                if random.choice([True, False]):
                    if i > 0 and grid[i - 1][j] == (0, 0, 0):
                        grid[i - 1][j], grid[i][j -
                                                1] = grid[i][j - 1], grid[i - 1][j]
                    elif i < len(grid) - 1 and grid[i + 1][j] == (0, 0, 0):
                        grid[i + 1][j], grid[i][j -
                                                1] = grid[i][j - 1], grid[i + 1][j]
                else:
                    if i < len(grid) - 1 and grid[i + 1][j] == (0, 0, 0):
                        grid[i + 1][j], grid[i][j -
                                                1] = grid[i][j - 1], grid[i + 1][j]
                    elif i > 0 and grid[i - 1][j] == (0, 0, 0):
                        grid[i - 1][j], grid[i][j -
                                                1] = grid[i][j - 1], grid[i - 1][j]


mouse_button_pressed = False

running = True
while running:
    window.fill((0, 0, 0))

    draw_grid()
    move_down()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_pressed = True
            x, y = pygame.mouse.get_pos()
            x //= grid_size
            y //= grid_size

            current_time = time.time()

            # Spawn particles in a 5x5 circle around the mouse
            for i in range(max(0, x - 2), min(len(grid), x + 3)):
                for j in range(max(0, y - 2), min(len(grid[0]), y + 3)):
                    if ((i - x) ** 2 + (j - y) ** 2) ** 0.5 <= 2.5:
                        if random.random() < 0.5:
                            hue = (current_time % 10) / 10
                            r, g, b = [int(c * 255)
                                       for c in colorsys.hsv_to_rgb(hue, 1, 1)]

                            grid[i][j] = (r, g, b)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button_pressed = False
        elif event.type == pygame.MOUSEMOTION and mouse_button_pressed:
            x, y = pygame.mouse.get_pos()
            x //= grid_size
            y //= grid_size
            current_time = time.time()
            for i in range(max(0, x - 2), min(len(grid), x + 3)):
                for j in range(max(0, y - 2), min(len(grid[0]), y + 3)):
                    if ((i - x) ** 2 + (j - y) ** 2) ** 0.5 <= 2.5:
                        if random.random() < 0.5:
                            hue = (current_time % 10) / 10
                            r, g, b = [int(c * 255)
                                       for c in colorsys.hsv_to_rgb(hue, 1, 1)]
                            grid[i][j] = (r, g, b)
pygame.quit()
