import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('city_temperature.csv')

df.head()

df.dtypes

df.shape

df.isnull().sum()

df = df.dropna(how='any', axis=0)
df.shape
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.index

df.describe()

df['Year']= df.index.year
df.head()

df.describe()
latest_df = df.loc['1995' : '2001']
latest_df.head()

latest_df[['country', 'Avg_temp']].groupby(['country']).mean().sort_values('Avg temp')

plt.figure(figsize=(9, 4))
sns.lineplot(x = "Year", y = "Avg_temp", data=latest_df)
plt.show()

resample_df = latest_df[['Avg_temp']].resample('A').mean()
resample_df.head()

resample_df.plot(title= ' temperature changes from 1995-2011'), figsize=(8,5)
plt.ylabel('temperature', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.legend()

