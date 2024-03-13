from matplotlib import lines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class myAnimation():
    def __init__(self, plot_data):
        self.plot_data = plot_data
        self.fig, self.ax = plt.subplots(figsize=(9,9))
        self.lines = []
        for i in self.plot_data.columns:
            line, = self.ax.plot(self.plot_data[i], lw=0.6, c='w')
            self.lines.append(line)
        self.ax.set_aspect('equal')
        self.ax.axis('off')


    def setup_plot(self):
        for i in self.lines:
            i.set_c('w')
        return self.lines

    def update(self, i):
        self.lines[i].set_c('#03989e')
        return self.lines

def random_flip(p=0.6):
    """Return a random flip"""
    while True:
        v = np.random.rand()
        if v > p:
            return -1
        else:
            return 1

if __name__ == "__main__":

    num_lines = 60
    xy_ratio = 0.4
    x_data = np.arange(0, num_lines/xy_ratio*1.01, 0.1)

    data = []
    for curr_line in range(num_lines):
        # line function (y = mx +c)
        c = num_lines-curr_line
        m = -c*xy_ratio/(curr_line+1)
        data.append(m*x_data+c)
    df = pd.DataFrame(data).T
    df[df < 0] = np.nan
    df['x'] = x_data
    df.set_index('x', inplace=True)

    df = df*random_flip()

    a = myAnimation(df)
    ani = animation.FuncAnimation(
            fig= a.fig,
            func= a.update,
            interval= 100,
            init_func= a.setup_plot,
            frames= num_lines, 
            repeat= False,
            blit= True
            )
    plt.show()