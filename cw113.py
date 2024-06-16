import matplotlib.pyplot as plt
import numpy.polynomial.chebyshev as npcheb
import numpy as np
import pandas as pd
import math
if __name__ == "__main__":
    rawdata = pd.read_excel('lab113.xlsx')
    data:pd.DataFrame = rawdata.loc[:,('T','P')].sort_values('P')
    Perror = [0.05*10**5 for i in range(len(data.loc[:,'P']))]
    data['P'] = 10**5 + data.loc[:,'P']*10**5
    #data['P'] = data.loc[:,'P']*10^
    #plt.scatter(data.loc[:,'P'],data.loc[:,'T'],label = "Zmierzone punkty")
    model = npcheb.chebfit(data.loc[:,'P'],data.loc[:,'T'],4)
    P = np.linspace(min(data.loc[:,'P']),max(data.loc[:,'P']))
    #generowanie wartości chebacheva
    T= npcheb.chebval(P,model)
    #pochodna z chebacheva
    dtdp = npcheb.chebder(model)
    slope = npcheb.chebval(10**5,dtdp)
    plt.errorbar(data.loc[:,'P'],data.loc[:,'T'],xerr=Perror,fmt='o',label = "Zmierzone punkty",elinewidth=1.5,markersize = 4)
    plt.plot(P,slope*(P-10**5) + npcheb.chebval(10**5,model),c='g',label = "Styczna do wyznaczonego wielomianu dla P = 1000 hPa")
    plt.plot(P,T,c='r',label = "Interpolowany wielomian Chebysheva 4 stopnia")
    Rmse = np.sqrt(np.mean((data.loc[:,'T']- npcheb.chebval(data.loc[:,'P'],model))**2))
    print(f'RMSE = {Rmse}\n')
    a = 1/4.42 - 1/808
    Qp = (npcheb.chebval(10**5,model)*(a))/slope * 10**(-3)
    uQp = math.sqrt((Rmse*a*10**-3/slope)**2 )
    print(f"Qp = {Qp} +/- {uQp}J/g\n")
    V0 = math.pi*1.42**2*6
    V2 = V0 - math.pi*0.22**2*12
    m0 = V0*0.8
    m2 = V2*0.8
    Qp1 = (19*0.26*357.78*160.53)/(m2*357.78 - m0*160.53)
    Qp2 = (15*0.2*357.78*226.13)/(m2*357.78 - m0*226.13)
    print(f'Q1 = {Qp1} Q2 = {Qp2}\n')
    plt.xlabel('Ciśnienie [Pa]')
    plt.ylabel("Temperatura [K]")
    plt.legend()
    plt.show()