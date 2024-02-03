import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
grid_size = 250
num_iterations = 1000
initial_infection_rate = 0.01
infection_rate = 0.125
recovery_rate = 0.15

grid = np.zeros((grid_size, grid_size))
infected = np.random.choice(range(grid_size), size=int(
    initial_infection_rate * grid_size), replace=False)
grid[infected, 0] = 1
fig, ax = plt.subplots()


def drawframe(t):
    ax.clear()
    ax.imshow(grid, cmap='viridis')

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 1:
                # Infect neighboring cells
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < grid_size and 0 <= nj < grid_size and grid[ni, nj] == 0:
                            if np.random.rand() < infection_rate:
                                grid[ni, nj] = 1

                # Recover infected cells
                if np.random.rand() < recovery_rate:
                    grid[i, j] = 2


ani = animation.FuncAnimation(
    fig, drawframe, frames=num_iterations, interval=20)

plt.show()
