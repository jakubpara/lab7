import pandas as pd
info={
    'Nr_albumu': [1, 2, 3, 4, 5, 6],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał','Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński','Pazdan'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5, 3.0],
    'WiekS': [22, 21, 24, 23, 25, 28]
}
df=pd.DataFrame(info)
print(df)

#a()
dfa=df[df['Ocena']>4]
print(f'ocena większa od 4\n {dfa}')

#b)
dfb=df.sort_values(by='WiekS')
print(f'posortowani ludzie względem wieku \n{dfb}')

#c)
dfc=df.groupby('Ocena')['WiekS'].mean()
print(f'ocena i średnia wieku\n {dfc}')
#d)

poprawa = {
    "Nr_albumu": [2, 5, 6],
    "Ocena_poprawa": [4.0, 4.5, 5.0]
}
df_poprawa = pd.DataFrame(poprawa)
df_merged = pd.merge(df, df_poprawa, on="Nr_albumu", how='left')
print(f'\n Połączone pierwszy termin i poprawa\n {df_merged}')

#e)
df_merged.to_csv("studenci.csv", index=False)

#f)
dff=pd.read_csv("studenci.csv")
print(dff)

#g)
studenciak={'Nr_albumu': 7,
    'Imie': 'Piotr',
    'Nazwisko': 'Żyła',
    'Ocena': 3.5,
    'WiekS': 20,
    'Ocena_poprawa': 4.0
}
nowy = pd.DataFrame(studenciak)

dfg = dff._append( nowy)
print(dfg)