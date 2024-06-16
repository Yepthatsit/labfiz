import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import tkinter.filedialog as fdial

import pandas as pd

filename = ""
def animation(i):
    data = pd.read_csv(filename)
    line1.set_data(data.loc[:,'TEMP'],data.loc[:,'B'])
    line2.set_data(data.loc[:,'TIME'],data.loc[:,'TEMP'])
    ax1.set_xlabel('Temp [K]')
    ax1.set_ylabel('Voltage [V]')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('TEMP [K]')
    ax1.relim()
    ax2.relim()
    ax1.autoscale_view(True, True, True)
    ax2.autoscale_view(True, True, True)
    fig.tight_layout()
if __name__ == "__main__":
    if len(sys.argv) != 1:
        filename = sys.argv[1]
    else:
        filename = fdial.askopenfilename()
    fig = plt.figure(figsize=(10, 6))
    
    ax1 = fig.add_subplot(2,1,1)
    line1, = ax1.plot([], [], marker='o', linestyle='-', color='b')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Pressure [bar]')

    ax2 = fig.add_subplot(2,1,2)
    line2, = ax2.plot([], [], marker='o', linestyle='-', color='r')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Voltage [V]')

    fig.tight_layout()
    ani = animate.FuncAnimation(fig,animation,cache_frame_data=False,interval=1000,blit= False)
    plt.show()