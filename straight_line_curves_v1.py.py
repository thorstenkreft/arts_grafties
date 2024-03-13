from matplotlib import lines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyparsing import null_debug_action

class myAnimation():
    def __init__(self, num_lines=10, xy_ratio=1.0):
        # plot data parameters
        self.nl = num_lines
        self.xy_ratio = xy_ratio
        self.data = []
        self.x_data = np.arange(0, self.nl/self.xy_ratio*1.01, 0.1)
        self.plt_change = False
        # plot parameters
        self.fig, self.ax = plt.subplots(figsize=(9,9), facecolor='k')
        self.lim = self.nl/self.xy_ratio
        self.ax.set_ylim(-self.lim,self.lim)
        self.ax.set_xlim(-self.lim,self.lim)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.lines = []
    


    def run_animation(self):
        def calc_line_data_points(curr_line):
            c = self.nl-curr_line
            m = -c*self.xy_ratio/(curr_line+1)
            y_data = m*self.x_data+c
            y_data[y_data<0] = np.nan
            #print(y_data)
            return y_data

        def setup_plot(p=0.5):
            for i in self.lines:
                i.set_lw(0)
            v = np.random.rand()
            if v > p:
                self.plt_change = True
            else:
                self.plt_change = False
            return self.lines

        def update(i):
            if self.plt_change:
                self.lines[i].set_data(self.x_data, calc_line_data_points(i))
                self.lines[i].set_c('#03989e')
                self.lines[i].set_lw(0.8)
            else:
                self.lines[i].set_data(-calc_line_data_points(i), self.x_data)
                self.lines[i].set_c('w')
                self.lines[i].set_lw(0.4)
            return self.lines
        
        #for curr_line in range(self.nl):
            # line function (y = mx +c)
            #c = self.nl-curr_line
            #m = -c*self.xy_ratio/(curr_line+1)
        #    self.data.append(calc_line_data_points(m, c))
        #self.plot_data = pd.DataFrame(self.data).T

        for i in range(self.nl):
            line = self.ax.plot([], [])[0]
            self.lines.append(line)

        ani = animation.FuncAnimation(
            fig= self.fig,
            func= update,
            interval= 50,
            init_func= setup_plot,
            frames= self.nl, 
            repeat= False,
            blit= True
        )
        plt.show()
        


if __name__ == "__main__":
    #np.random.seed(19680801)
    a = myAnimation(30,0.6)
    a.run_animation()