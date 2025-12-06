import pandas as pd
df=pd.read_csv('demografia.csv')


df=pd.read_csv('demografia.csv' ,decimal=',', na_values=['NA','n/a', 'NaN'])

#usuniecie kolumny kraje
df_without=df.drop(columns=['KRAJE'])

max_przyrost =df_without.max().max()
print(max_przyrost)
rok_max_przyrost=df_without.max().idxmax()
print(rok_max_przyrost)
indeksMax= df_without[rok_max_przyrost].idxmax()


kraj_max_przyr=df.loc[indeksMax,'KRAJE']
print(f'najwiekszy przyrost ludności wyniósł {max_przyrost} w {kraj_max_przyr}')
