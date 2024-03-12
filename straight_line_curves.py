import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_lines = 30
x_data = np.arange(0, num_lines*1.01, 0.5)


data = []
for line in range(num_lines):
    c = num_lines-line
    # line function (y = mx +c)
    data.append(-c/(line+1)*x_data + c)

df = pd.DataFrame(data).T
df[df < 0] = np.nan
df['x'] = x_data
df.set_index('x', inplace=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim([0,num_lines])
ax.axis('off')

# generate line plots
lines = []
for i in range(num_lines):
    line, = ax.plot(df[i], lw=0.6, c='w')
    lines.append(line)

def init():
    print('init')
    for i in range(len(lines)):
        lines[i].set_c('w')
    return lines

def animate(i):
    print(i)
    lines[i].set_c('#03989e')
    return lines

ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    init_func=init,
    frames=num_lines,
    blit=True,
    interval=100,
    repeat=True
    )

plt.show()