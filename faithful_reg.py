from pydataset import data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from evaluate import regression_errors
from sklearn.linear_model import LinearRegression

faithful = data('faithful')

pearsons_r = faithful.eruptions.corr(faithful.waiting)

sns.scatterplot(x='waiting', y='eruptions', data=faithful) 
plt.show()

reg = LinearRegression()
reg.fit(faithful[['waiting']], faithful[['eruptions']])

y_pred = reg.predict(faithful[['waiting']])
faithful['predicted'] = y_pred

sns.scatterplot(x='waiting', y='predicted', data=faithful, alpha=0.8)
sns.scatterplot(x='waiting', y='eruptions', data=faithful) 
plt.title('Waiting Time Between Geyser Eruptions at Old Faithful')
plt.yticks(np.arange(0,6))
rmse = regression_errors(faithful.eruptions, faithful.predicted)[4]
blue_patch = mpatches.Patch(color='blue', label='Predicted')
orange_patch = mpatches.Patch(color='orange', label='Actual')
plt.legend(handles=[blue_patch, orange_patch])
plt.annotate(s=f'RMSE: {rmse}', xy=(72,1))
plt.show()