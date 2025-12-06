import pandas as pd
df = pd.read_csv(   'demografia.csv',decimal=',' ,na_values=['NA''n/a', 'NaN'])

max_przyrost_index=df['2022'].idxmax(skipna=True)
kraj_z_max_przyrost = df.loc[max_przyrost_index, 'KRAJE']
print(f'Kraj z najwiekszym przyrostem to {kraj_z_max_przyrost}')







