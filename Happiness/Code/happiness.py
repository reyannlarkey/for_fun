import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hdbscan

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 300
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 8)

import os



data_loc  = "../Data/"

files = [data_loc+i for i in sorted(os.listdir(data_loc))]


file = files[0]

df = pd.read_csv(file)

# rename columns to make it easier to work with
df.columns = ['Country',
              'Region',
              'Happiness_Rank',
              'Happiness_Score',
              'Standard_Error',
              'GDP_per_cap',
              'Family',
              'Life_Expectancy',
              'Freedom',
              'Government_Corruption',
              'Generosity',
              'Dystopia_Residual']



# country_groups = df.groupby('Region')
# for name, group in country_groups:
clusterer = hdbscan.HDBSCAN()
clusters = clusterer.fit(df[['Happiness_Rank', 'Life_Expectancy']])
df['Labels'] = clusters.labels_


clusters = df.groupby('Labels')


for label, cluster in clusters:



    plt.scatter(cluster.Happiness_Rank, cluster.Life_Expectancy)

# plt.legend()
#
plt.show()
