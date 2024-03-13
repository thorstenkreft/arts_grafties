from matplotlib import lines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyparsing import null_debug_action

class myAnimation():
    def __init__(self, num_lines, xy_ratio=1.0):
        self.data = []
        self.nl = num_lines
        self.xy_ratio = xy_ratio
        self.x_data = np.arange(0, self.nl/self.xy_ratio*1.01, 0.1)
        self.fig, self.ax = plt.subplots(figsize=(9,9), facecolor='k')
        self.ax.set_ylim(-num_lines,num_lines)
        self.ax.set_xlim(-num_lines/xy_ratio,num_lines/xy_ratio)
        self.lines = []
        self.plt_change = False
    
    def run_animation(self):
        for curr_line in range(self.nl):
            # line function (y = mx +c)
            c = self.nl-curr_line
            m = -c*self.xy_ratio/(curr_line+1)
            self.data.append(m*self.x_data+c)
        self.plot_data = pd.DataFrame(self.data).T
        self.plot_data[self.plot_data < 0] = np.nan
        self.plot_data['x'] = self.x_data
        self.plot_data.set_index('x', inplace=True)

        for i in range(self.nl):
            #line, = self.ax.plot(self.plot_data[i], lw=0.6, c='k')
            line, = self.ax.plot(self.x_data, self.plot_data[i], lw=0.6, c='k')
            self.lines.append(line)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        def setup_plot(p=0.5):
            for i in self.lines:
                i.set_lw(0)
            v = np.random.rand()
            if v > p:
                self.plt_change = True
            else:
                self.plt_change = False
            print(self.plt_change)
            return self.lines

        def update(i):
            if self.plt_change:
                self.lines[i].set_data(self.x_data, self.plot_data[i])
                self.lines[i].set_c('#03989e')
                self.lines[i].set_lw(0.8)
            else:
                self.lines[i].set_data(-self.plot_data[i], self.x_data)
                self.lines[i].set_c('w')
                self.lines[i].set_lw(0.4)
            return self.lines

        ani = animation.FuncAnimation(
            fig= self.fig,
            func= update,
            interval= 100,
            init_func= setup_plot,
            frames= self.nl, 
            repeat= True,
            blit= True
        )
        plt.show()
        


if __name__ == "__main__":
    #np.random.seed(19680801)
    a = myAnimation(20,0.7)
    a.run_animation()