from os import X_OK
from matplotlib import lines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyparsing import null_debug_action

class myAnimation():
    def __init__(self, num_lines=10):
        # random behaviour parameters
        self.nl = num_lines
        self.xy_ratio = 1.0
        self.rand_xy_flip = False
        # plot parameters
        self.fig, self.ax = plt.subplots(figsize=(9,9), facecolor='k')
        self.lim = self.nl/self.xy_ratio
        self.ax.set_ylim(0,self.lim)
        self.ax.set_xlim(0,self.lim)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.lines = []
                
    def run_animation(self):

        def rand_xy_flip(p=0.5):
            if p > np.random.rand():
                return True
            else:
                return False
            
        def calc_line_data_points(curr_line):
            c = self.nl-curr_line
            m = -c*self.xy_ratio/(curr_line+1)
            x_data = np.array([0, (curr_line+1)/self.xy_ratio])
            y_data = m*x_data+c

            if self.rand_xy_flip:
                return y_data, x_data
            else:
                return x_data, y_data

        def init_func():
            # setup random behaviour parameters
            self.xy_ratio = np.random.rand()*2
            self.rand_xy_flip = rand_xy_flip()

            # setup plot
            self.lines = []
            for i in range(self.nl):
                line = self.ax.plot([], [])[0]
                self.lines.append(line)


            return self.lines

        def update(i):
            #if self.plt_change:
            #    self.lines[i].set_data(calc_line_data_points(i))
            #    self.lines[i].set_c('#03989e')
            #    self.lines[i].set_lw(0.8)
            #else:
            self.lines[i].set_data(calc_line_data_points(i))
            self.lines[i].set_c('w')
            self.lines[i].set_lw(0.4)
            return self.lines

        ani = animation.FuncAnimation(
            fig= self.fig,
            func= update,
            interval= 50,
            init_func= init_func,
            frames= self.nl, 
            repeat= True,
            blit= True
        )
        plt.show()
        


if __name__ == "__main__":
    #np.random.seed(19680801)
    a = myAnimation(np.random.randint(8,100))
    a.run_animation()