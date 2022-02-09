import numpy
import pandas
import matplotlib.pyplot as plt

#read data
df = pandas.read_csv('data.csv')

#check null data
null_data = df[df.isnull().any(axis=1)]

#calculate total time interval
total_time = df['irradiance'].count()

#fill null data
df = df.interpolate(method ='linear', limit_direction ='forward')

#calculate PV
df['PV'] = df['irradiance'] * 0.09

#compare and modify PV value
for index in df.index:
    if df.iloc[index]['PV'] > df.iloc[index]['total_load_kw']:
        df.loc[index,'PV'] = df.iloc[index].at['total_load_kw']

#calculate genset
df['genset'] = df['total_load_kw'] - df['PV']

#calculate diesel 
total_littre = sum(df['genset']) /60 * 0.3

print("total litres of diesel: ", total_littre)

df.plot(x="timestamp", y=["PV", "total_load_kw", "genset"])

plt.show()


