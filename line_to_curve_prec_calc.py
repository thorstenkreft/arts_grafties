import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyparsing import null_debug_action
from sympy import false

"""
Line to Curve graphing
Dynamic Calc: the data point for each line is calculation during runtime (i.e. upon update function call between internvals)
"""

class myAnimation():
    def __init__(self, num_lines=10, interval_speed=50):
        # general behaviour parameters
        self.nl = num_lines
        self.interval_speed = interval_speed
        self.xy_ratio = 1.0
        self.rand_xy_flip = False
        self.rand_lw = 0.6
        # plot parameters
        self.fig = plt.figure(figsize=(8, 8), facecolor='k')
        self.ax = plt.subplot(frameon=False)
        self.ax.axis('off')
        self.ax.set_aspect('equal')
        self.lines = []
        self.x_data = []
        self.y_data = []
                
    def run_animation(self):
        def rand_xy_flip(p=0.5):
            """Random flip of X- and Y-axis"""
            if p < np.random.rand():
                return True
            else:
                return False
        
        def rand_line_width(p=0.5):
            """Random line width used to draw lines in plot"""
            if p < np.random.rand():
                self.rand_lw = np.random.rand()*0.8

        def calc_line_data_points():
            """
            Calculation of coordinates (x,y) data points for each line,
            on the intersection of the x- and y-axis. Called after each frame of the animation
                x_data is a coordinate array where a line intersects with the x-axis
                y_data is a coordinate array where a line intersects with the y-axis
            """
            for i in range(self.nl):
                c = self.nl-i
                m = -c*self.xy_ratio/(i+1)
                x_temp = np.array([0, (i+1)/self.xy_ratio])
                self.x_data.append(x_temp)
                self.y_data.append(m*x_temp+c)

        def init_func():
            # setup random behaviour parameters
            self.xy_ratio = 1 #np.random.rand()
            self.rand_xy_flip = rand_xy_flip(0.8)
            rand_line_width()
            calc_line_data_points()
            # remove previous/existing plot lines
            for line in self.ax.get_lines():
                line.remove()
                del line
            self.lines = []
            self.x_data = []
            self.y_data = []
            # adjust x-y axes limits
            if self.xy_ratio < 1:
                lim = self.nl/self.xy_ratio
            else:
                lim = self.nl*self.xy_ratio
            self.ax.set_xlim(0, lim)
            self.ax.set_ylim(0, lim)
            # add plot lines
            for i in range(self.nl):
                line = self.ax.plot([], [])[0]
                self.lines.append(line)
            return self.lines

        def update(i):
            self.lines[i].set_data(self.x_data, self.y_data)
            self.lines[i].set_c('w')
            self.lines[i].set_lw(self.rand_lw)
            return self.lines

        ani = animation.FuncAnimation(
            fig=self.fig,
            func=update,
            interval=self.interval_speed,
            init_func=init_func,
            frames=self.nl, 
            repeat=False,
            blit= False
        )
        plt.show()


if __name__ == "__main__":
    a = myAnimation(10, 200)
    a.run_animation()