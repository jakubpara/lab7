import pandas as pd

data = {
    'Numer': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 700],

}
df = pd.DataFrame(data)

#A)
pracownicy_5k=df[df['Pensja']>5000]
print(f'paracownicy z wysoką pensją {pracownicy_5k}')

#b)
sorted_age=df.sort_values(by='Wiek')
print(sorted_age)

#c)
g_b_p=df.groupby('Stanowisko')['Pensja'].mean()
print('\n śrenia pensja według stanowiska\n')
print(g_b_p)

#d)
dane_awans={
    'Numer': [2,4],
    'nowe_stanowiska' : ['Senior Programista', 'Senior Programista']
}
df_awans= pd.DataFrame(dane_awans)

df_combined=pd.merge(df,df_awans,on='Numer', how= 'left')
print(f'Nowe stanowiska \n  {df_combined}')

#e)
#df_combined.to_csv('dane_z_pracy.csv', index=False)
#nie ma po co żeby sie wywolywalo nie wiadomo ile
#f)

df1=pd.read_csv('dane_z_pracy.csv')

print(df1)
