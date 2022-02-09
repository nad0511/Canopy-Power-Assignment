import numpy
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('data.csv')


null_data = df[df.isnull().any(axis=1)]



total_time = df['irradiance'].count()


df = df.interpolate(method ='linear', limit_direction ='forward')

df['PV'] = df['irradiance'] * 0.09


for index in df.index:
    if df.iloc[index]['PV'] > df.iloc[index]['total_load_kw']:
        df.loc[index,'PV'] = df.iloc[index].at['total_load_kw']

df['genset'] = df['total_load_kw'] - df['PV']


null_data = df[df.isnull().any(axis=1)]


total_littre = sum(df['genset']) /60 * 0.3

print("total litres of diesel: ", total_littre)

df.plot(x="timestamp", y=["PV", "total_load_kw", "genset"])

plt.show()


