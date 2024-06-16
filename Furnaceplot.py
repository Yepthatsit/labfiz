import sys

import matplotlib.lines
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import tkinter.filedialog as fdial
import math
import pandas as pd
filename:str = ''
plots_to_make:list = []
axes:list = []
lines:list = []

def HAndle_Plots(i)->None:
    global filename, plots_to_make, axes, lines, figure
    data = pd.read_excel(filename)
    for i in range(len(plots_to_make)):
        plot_parameters = plots_to_make[i].split(',')
        lines[i].set_data(data.loc[:,plot_parameters[0]],data.loc[:,plot_parameters[1]])
        axes[i].relim()
        axes[i].autoscale_view()
        axes[i].set_xlabel(plot_parameters[0])
        axes[i].set_ylabel(plot_parameters[1])
    figure.tight_layout()
def main()->None:
    try:
        global filename, plots_to_make, axes, lines, figure
        filename = sys.argv[1]
        plots_to_make = sys.argv[2:]
        figure = plt.figure()
        columns = 2
        rows = math.ceil(len(plots_to_make)/2)
        for i in range(len(plots_to_make)):
            subplot = figure.add_subplot(rows,columns,i+1)
            line, = subplot.plot([],[],marker = 'o')
            axes.append(subplot)
            lines.append(line)
        live_plot = animate.FuncAnimation(figure,HAndle_Plots,cache_frame_data=False,interval=1000)
        plt.show()
    except KeyboardInterrupt:
        print('Plotting stopped by user.')
if __name__ == '__main__':
    main()