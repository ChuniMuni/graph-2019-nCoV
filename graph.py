import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# считаем данные из csv файла
data = pd.read_csv("covid_19_data.csv")

# определим размер набора данных
data.shape

# Sample data output
# print(data.head())

data.describe()

# Проверка на дубликаты
# print(sum(data.duplicated(['Country/Region', 'Province/State', 'ObservationDate'])))

data.loc[data['Country/Region'] == 'Mainland China', 'Country/Region'] = 'China'

# Выводим общий список
country_list = data['Country/Region'].unique()
print('Коронавирус COVID19 обнаружен в {} странах:'.format(country_list.size))

for country in sorted(country_list):
    print('- {}'.format(country))

# Анализ по отдельной стране
# var = data[data['Country/Region'] == 'Russia']
# print(var)

# Приводим даты к единому виду
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])
data['Date_date'] = data['ObservationDate'].apply(lambda x:x.date())
df_by_date=data.groupby(['Date_date']).sum().reset_index(drop=None)

# Временная зависимость количества подтвержденных случаев
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = [12.0, 5.0]
mpl.rcParams['figure.dpi'] = 100

sns.set()
plt.plot(df_by_date["Date_date"],
         df_by_date["Confirmed"]/1000,
         'o:')

plt.xlabel('Дата')
plt.ylabel('Число подтвержденных случаев, тыс. чел.')
plt.show()

# Число умерших и выздоровевших
d = {"Deaths":"Умерли", "Recovered":"Выздоровели"}

for label in d:
    plt.plot(df_by_date["Date_date"],
             df_by_date[label]/1000,
             label=d[label])

plt.ylabel('Число случаев, тыс. человек')
plt.xlabel('Дата')
plt.legend()
plt.show()

# данные в полулогарифмическом масштабе
plt.yscale('log')
for label in d:
    plt.plot(df_by_date["Date_date"],
             df_by_date[label]/1000,
             label = d[label])

plt.ylabel('Число случаев, тыс. человек')
plt.xlabel('Дата')
plt.legend()
plt.show()
