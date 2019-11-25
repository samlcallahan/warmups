import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('the_data.csv')
data.timestamp = pd.to_datetime(data.timestamp)

data = data.set_index('timestamp')

data[data.y == 'B'].x.max() # 1.91
data[data.y == 'A'].x.max() # 1.84
data[data.y == 'C'].x.min() # -1.83
data.groupby('y').sum() # group C

data.resample('D').sum() # -4.02
data.resample('D').mean() # .22, -.1675
data.resample('D').median() # .175, .22
data.resample('D').x.max() # april 30
data[data.y == 'C'].resample('D').x.min() # may 1

data.groupby('y').x.min().plot.bar()
plt.ylabel('minimum x value')
plt.show()

data.x.plot()
plt.ylabel('x')
plt.show()

data.groupby('y').x.plot(legend=True)
plt.ylabel('x')
plt.show()

data['2018-04-30'].y.value_counts() # b and c are tied
data.resample('D').y.value_counts() # a, c, respectively