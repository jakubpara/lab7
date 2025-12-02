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

#pracownicy_5k=df[df['Pensja']>5000]
#print(f'paracownicy z wysoką pensją {pracownicy_5k}')

#sorted_age=df.sort_values(by='Wiek')
#print(sorted_age)

g_b_p=df.groupby('Stanowisko')['Pensja'].mean()
print(g_b_p)
