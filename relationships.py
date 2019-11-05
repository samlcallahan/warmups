import pandas as pd
from pydataset import data
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from sklearn.cluster import KMeans

relationships = pd.read_csv('50k-posts-from-relationship-advice.csv', header=None, names=['f_age', 'm_age', 'id', 'text'])

sns.scatterplot(x='f_age', y='m_age', data=relationships)
plt.show()
# Let's go ahead and remove the super outliers with age over 100. 
# Drop under 18 bc that's creepy and there are some about 6yo cats

to_drop = relationships[(relationships.m_age > 80) | (relationships.f_age > 80) | (relationships.m_age < 18) | (relationships.f_age < 18)]
relationships.drop(to_drop.index, inplace=True)
sns.scatterplot(x='f_age', y='m_age', data=relationships)
plt.show()

drop_words = ['mother', 'mom', 'father', 'dad', 'brother', 'sister']

def contains_list_word(text, bad_words):
    for word in bad_words:
        if word in text:
            return True
    return False

mask = relationships.text.apply(lambda x: contains_list_word(x, drop_words))

relationships.drop(relationships[mask].index, inplace=True)

X = relationships[['f_age', 'm_age']]
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
relationships['cluster'] = kmeans.labels_
plt.figure(figsize=(12, 9))
sns.scatterplot(x='f_age', y='m_age', data=relationships, hue='cluster', alpha=0.2, palette='terrain')
plt.scatter(x=kmeans.cluster_centers_[:, 0], y=kmeans.cluster_centers_[:, 1], marker='x', s=2000, c='black')
plt.show()