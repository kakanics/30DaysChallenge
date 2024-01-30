import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d

state = np.zeros((400, 400))
state = np.random.rand(100, 100)

kernel = np.ones((3, 3))
kernel[1, 1] = -8


def birth(x):
    return np.where(np.logical_and(0.020 < x, x < 0.300), x / 2, 0)


def survival(x):
    return np.where(np.logical_and(0.120 < x, x < 0.500), x / 2, 0)


def update(frame):
    global state
    convolved = convolve2d(state, kernel, mode='same', boundary='wrap')
    new_state = state + birth(convolved) + survival(convolved)
    new_state = np.where(new_state > 0, new_state - 0.01, new_state)
    state = np.clip(new_state, 0, 1)
    plt.clf()
    plt.imshow(state, cmap='gray')


fig = plt.figure()
ani = FuncAnimation(fig, update, interval=50)

plt.show()
