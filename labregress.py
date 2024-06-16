from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
if __name__ == "__main__":
    x0 = np.array([457,522,593,630])
    x = (3*10**17)/x0
    y = np.array([0.686,0.497,0.330,0.237])
    result = linregress(x,y)
    print(result.slope*(1.6*10**-19),result.stderr*(1.6*10**-19),-result.intercept*(1.6*10**-19),result.intercept_stderr*(1.6*10**-19))
    plt.plot(np.linspace(min(x)-0.5, max(x)),result.slope*np.linspace(min(x)-0.5, max(x))+ result.intercept,label = "Prosta najlepszego dopasowania")
    plt.scatter(x,y,c="r",label = "Zmierzone wartości")
    plt.xlabel("Częstotliwość[Hz]")
    plt.ylabel("Napięcie[V]")
    plt.legend()
    print(result)
    plt.show()