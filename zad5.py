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

#a)
df.groupby('Ocena')['Ocena'>4]
print(df.groupby('Ocena')['Ocena'].nunique())