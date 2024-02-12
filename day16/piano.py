import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np


class InteractivePlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.points = []
        self.cid = self.fig.canvas.mpl_connect(
            'button_press_event', self.onclick)

    def onclick(self, event):
        if event.xdata is None or event.ydata is None:  # Ignore clicks outside the plot area
            return

        self.points.append((event.xdata, event.ydata))
        self.points.sort()  # Sort points by x-value
        self.ax.clear()

        x, y = zip(*self.points)  # Unzip the list of points
        self.ax.plot(x, y, 'ro')

        if len(self.points) > 1:
            xnew = np.linspace(min(x), max(x), 300)
            # Adjust k based on the number of points
            k = min(3, len(self.points) - 1)
            spl = make_interp_spline(x, y, k=k)
            ynew = spl(xnew)
            self.ax.plot(xnew, ynew, 'b-')

        plt.draw()

    def show(self):
        plt.show()


plot = InteractivePlot()
plot.show()
