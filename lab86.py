import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal
if __name__ == "__main__":
    labcw86 = pd.read_excel('labcw86.xlsx')
    Ipolaryzacja = labcw86.loc[:,'Ipol']
    kat = labcw86.loc[:,'stopni']*math.pi/180
    Imax = max(Ipolaryzacja)
    Imin = min(Ipolaryzacja)
    kat_teoria = np.linspace(0,2*math.pi)
    Ipolaryzacja_teoria = Imin + (Imax - Imin)*np.cos(kat_teoria - 80*math.pi/180)**2
    Polaryzacjafig = plt.figure()
    Polaryzacjaplot = Polaryzacjafig.add_subplot(1,1,1)
    Polaryzacjaplot.plot(kat_teoria,Ipolaryzacja_teoria,label = 'Krzywa teoretyczna', c='g')
    Polaryzacjaplot.scatter(kat,Ipolaryzacja,label = 'Punkty pomiarowe',c='b')
    Polaryzacjaplot.set_xlabel('Kąt(Rad)')
    Polaryzacjaplot.set_ylabel('Natężenie(A)')
    Polaryzacjafig.legend()
    Prof_wiaz_nat = labcw86.loc[:,'natIobr']
    Prof_wiaz_obr = labcw86.loc[:,'lpolobr']*0.75/2
    Prof_wiazki = plt.figure()
    Prof_wiazki_plot = Prof_wiazki.add_subplot(111)
    Prof_wiazki_plot.plot(Prof_wiaz_obr,Prof_wiaz_nat,marker = 'o')
    Prof_wiazki_plot.set_xlabel('Położenie')
    Prof_wiazki_plot.set_ylabel('Natężenie')
    peaks, _ = scipy.signal.find_peaks(Prof_wiaz_nat)
    results = scipy.signal.peak_widths(Prof_wiaz_nat,peaks,rel_height=0.5,)
    Prof_wiazki_plot.hlines(y = results[1][0], xmin=results[2][0]*0.75/2,xmax=results[3][0]*0.75/2,colors= 'g')
    print(results[0][0]*0.75/2, round(100*(2.69e-3/0.16)/(2.65*0.17),2))
    labcw87 = pd.read_excel('labcw87.xlsx')
    x = labcw87.loc[:,'x[mm]']
    Ilaser = labcw87.loc[:,'Ilaser']
    cz3 = plt.figure()
    cz3plot = cz3.add_subplot(111)
    cz3plot.plot(x,Ilaser,marker = 'o',c='b')
    peaks2,_ = scipy.signal.find_peaks(Ilaser,height=0.03)
    results2 = scipy.signal.peak_widths(Ilaser,peaks2,rel_height=0.5)
    print(results2)
    cz3plot.hlines(y = [results2[1][0],results2[1][1]],xmin=[results2[2][0]*25,results2[2][1]*25],xmax=[results2[3][0]*25,results2[3][1]*25],colors = 'g')
    print(f'fwdh 1 {results2[0][0]*25}, 2 {results2[0][1]*25} h1 {Ilaser[peaks2[0]]} h2 {Ilaser[peaks2[1]]}')
    cz3plot.set_xlabel('Położenie')
    cz3plot.set_ylabel('Natężenie')
    plt.show()