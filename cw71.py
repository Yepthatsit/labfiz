import matplotlib.pyplot as plt
import pandas as pd
if __name__ == "__main__":
    f1 = plt.figure()
    f1.suptitle('Obraz dyfrakcyjny na pojedynczej szczelinie')
    one = f1.add_subplot(1,2,1)
    onelog = f1.add_subplot(1,2,2)
    onelog.set_yscale('log')
    onelog.set_title('w skali logarytmicznej')
    one.set_title('w skali liniowej')
    data = pd.read_excel('cw71.xlsx').sort_values('y1[mm]')
    onelog.plot(data.loc[:,'y1[mm]'],data.loc[:,'U1'],marker = 'o')
    one.plot(data.loc[:,'y1[mm]'],data.loc[:,'U1'],marker = 'o')
    maxims = {}
    for i in range(1,len(data.loc[:,'U1'])-1):
        if abs(data.loc[i,'U1']) >= abs(data.loc[i+1,'U1']) and abs(data.loc[i,'U1']) >= abs(data.loc[i-1,'U1']) and data.loc[i,'U1'] not in list(maxims.keys()):
            maxims[data.loc[i,'U1']] = i
    onetick = [data.loc[i,'y1[mm]'] for i in list(maxims.values())]
    onelog.set_xticks(onetick)
    one.set_xticks(onetick)
    data2 = data.sort_values('y2[mm]')
    data2['y2[mm]'] = data2['y2[mm]'] - 10
    maxims2 = {}
    for i in range(1,len(data.loc[:,'U2'])-1):
        if abs(data2.loc[i,'U2']) >= abs(data2.loc[i+1,'U2']) and abs(data2.loc[i,'U2']) >= abs(data2.loc[i-1,'U2']): #and data2.loc[i,'U2'] not in list(maxims.keys()):
            maxims2[data2.loc[i,'U2']] = i
    twotick = [data2.loc[i,'y2[mm]'] for i in list(maxims2.values())] + [-6.6]
    f2 = plt.figure()
    f2.suptitle('Obraz dyfrakcyjny oraz interferencyjny na dwóch szczelinach')
    two = f2.add_subplot(1,2,1)
    twolog = f2.add_subplot(1,2,2)
    twolog.set_yscale('log')
    twolog.set_title('w skali logarytmicznej')
    two.set_title('w skali liniowej')
    twolog.plot(data2.loc[:,'y2[mm]'],data2.loc[:,'U2'],marker = 'o')
    two.plot(data2.loc[:,'y2[mm]'],data2.loc[:,'U2'],marker = 'o')
    twolog.set_xticks(twotick)
    two.set_xticks(twotick)
    plt.show()