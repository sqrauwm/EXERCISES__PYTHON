import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
# print(ts)
ts.plot()
# plt.savefig('wykres1.png')
# plt.show()

# data={'Kraj':['Belgia','Indie','Brazylia', 'Polska'],
#       'Stolica':['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#       'Populacja': [11190846, 1303171035, 207847528, 38775467],
#       'Kontynent':['Europa', 'Azja', 'Ameryka Południowa','Europa']}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})

# grupa.plot(kind='bar', xlabel='Kontynent',ylabel='Populacja w mld',
#            rot=0, title='Populacja dla kontynentów')

# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja dla kontynentow')
# plt.savefig('wykres-kontynenty.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep =';', decimal='.')
# print(df)
# grupa= df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot.pie(subplots=True, autopct='%.2f %%',
#                fontsize=18, figsize=(5,5), legend=(1,1))
# plt.show()

df = pd.DataFrame(ts)

df['Średnia krocząca'] = df.rolling(window=30).mean()
print(df)
df.plot()
plt.legend(['Wartości','Średnia krocząca'])
plt.show()