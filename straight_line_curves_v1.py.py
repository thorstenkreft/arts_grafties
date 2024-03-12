from matplotlib import lines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class myAnimation():
    def __init__(self, num_lines, xy_ratio=1.0):
        self.data = []
        self.nl = num_lines
        self.xy_ratio = xy_ratio
        self.x_data = np.arange(0, self.nl/self.xy_ratio*1.01, 0.1)
        self.fig, self.ax = plt.subplots(figsize=(9,9))
        self.lines = []
    
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
            line, = self.ax.plot(self.plot_data[i], lw=0.6, c='w')
            self.lines.append(line)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        def setup_plot():
            for i in self.lines:
                i.set_c('w')
            return self.lines

        def update(i):
            print(i)
            self.lines[i].set_c('#03989e')
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
    a = myAnimation(60,0.4)
    a.run_animation()