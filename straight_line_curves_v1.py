import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyparsing import null_debug_action

class myAnimation():
    def __init__(self, num_lines=10):
        # random behaviour parameters
        self.nl = num_lines
        self.xy_ratio = 1.0
        self.rand_xy_flip = False
        self.rand_lw = 0.6
        # plot parameters
        self.fig = plt.figure(figsize=(8, 8), facecolor='k')
        self.ax = plt.subplot(frameon=False)
        self.ax.axis('off')
        self.ax.set_aspect('equal')
        self.lines = []
                
    def run_animation(self):
        def rand_xy_flip(p=0.5):
            if p < np.random.rand():
                return True
            else:
                return False
        
        def rand_line_width(p=0.5):
            if p < np.random.rand():
                self.rand_lw = np.random.rand()*0.8

        def calc_line_data_points(curr_line):
            c = self.nl-curr_line
            m = -c*self.xy_ratio/(curr_line+1)
            x_data = np.array([0, (curr_line+1)/self.xy_ratio])
            y_data = m*x_data+c
            # random change of x- and y-data
            if self.rand_xy_flip:
                return y_data, x_data
            else:
                return x_data, y_data

        def init_func():
            # setup random behaviour parameters
            self.xy_ratio = np.random.rand()
            self.rand_xy_flip = rand_xy_flip(0.8)
            rand_line_width()
            # remove previous/existing plot lines
            for line in self.ax.get_lines():
                line.remove()
                del line
            self.lines = []
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
            self.lines[i].set_data(calc_line_data_points(i))
            self.lines[i].set_c('w')
            self.lines[i].set_lw(self.rand_lw)
            return self.lines

        ani = animation.FuncAnimation(
            fig=self.fig,
            func=update,
            interval=50,
            init_func=init_func,
            frames=self.nl, 
            repeat=True,
            blit= False
        )
        plt.show()


if __name__ == "__main__":
    a = myAnimation(100)  #np.random.randint(8,100)
    a.run_animation()