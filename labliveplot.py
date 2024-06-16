import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
def animation(frame):
    data = pd.read_excel(sys.argv[1])
    data = data.sort_values(sys.argv[2])
    dataline.set_data(data.loc[:,sys.argv[2]],data.loc[:,sys.argv[3]])
    subfigure.set_xlabel(sys.argv[2])
    subfigure.set_ylabel(sys.argv[3])
    #subfigure.set_yscale("log")
    subfigure.relim()
    subfigure.autoscale_view()
    return dataline
if __name__ == "__main__":
    figure = plt.figure()
    subfigure = figure.add_subplot(1,1,1)
    file = pd.read_excel(sys.argv[1])
    dataline, = subfigure.plot(file.loc[:,sys.argv[2]],file.loc[:,sys.argv[3]],marker = "o")
    print(file)
    an = anim.FuncAnimation(fig = figure,func = animation,interval = 2000,cache_frame_data=False)
    plt.show()
