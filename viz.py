from pydataset import data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = data('mpg')


sns.scatterplot(y='hwy', x='displ', data=mpg, hue='cyl')
plt.ylabel('Highway Mileage (mpg)')
plt.xlabel('Engine Displacement (L)')
plt.title('How Engine Displacement Affects Fuel Efficiency')
plt.hlines(y=mpg.hwy.mean(), linestyles='dotted', xmin=0, xmax=8)
plt.vlines(x=mpg.displ.mean(), linestyles='dotted', ymin=0, ymax=45)
plt.show()
# Visualize highway mileage (hwy) on the y-axis against engine displacement (displ) on the x-axis.
# Add meaningful labels and a title.
# Add a horizontal dotted line that indicates the average highway mileage.
# Add a vertical dotted line that indicates the average engine displacement.
# Use color to indicate the number of cylinders (cyl) each car's engine has.
# Instead of color, use seperate subplots to indicate the number of cylinders.