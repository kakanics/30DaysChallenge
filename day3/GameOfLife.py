import pygame

pygame.init()
grid_size = 50
cell_size = 10

window = pygame.display.set_mode(
    (grid_size * cell_size, grid_size * cell_size))

grid = [[(0, 0, 0) for _ in range(grid_size)] for _ in range(grid_size)]


def next_state():
    new_grid = [[(0, 0, 0) for _ in range(grid_size)]
                for _ in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            live_neighbors = sum(grid[x][y] == (255, 255, 255)
                                 for x in range(max(0, i - 1), min(grid_size, i + 2))
                                 for y in range(max(0, j - 1), min(grid_size, j + 2))
                                 if (x, y) != (i, j))

            if grid[i][j] == (255, 255, 255):
                if live_neighbors in [2, 3]:
                    new_grid[i][j] = (255, 255, 255)
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = (255, 255, 255)

    return new_grid


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= cell_size
            y //= cell_size
            grid[x][y] = (255, 255, 255)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = next_state()
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(
                window, grid[i][j], (i * cell_size, j * cell_size, cell_size, cell_size))

    pygame.display.update()

pygame.quit()
