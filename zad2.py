import pandas as pd
df = pd.read_csv(   'demografia.csv',decimal=',' ,na_values=['NA''n/a', 'NaN'])


df_without=df.drop(columns=['KRAJE'])
print(df_without)

max_p =df_without.max().max()

indeksMax=max_p.max().idxmax()

print(indeksMax)




