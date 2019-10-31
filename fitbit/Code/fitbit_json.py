import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import os
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


files = [i for i in sorted(os.listdir('../Data/ReyannLarkey/user-site-export/')) if i.startswith('heart_rate')]

for i, file in enumerate(files):
    with  open(f'../Data/ReyannLarkey/user-site-export/{file}') as openfile:
        jsondata = json.load(openfile)
        df = pd.DataFrame(jsondata)

        df = pd.concat([df['dateTime'], df['value'].apply(pd.Series)], axis=1)
        # df.value = df.value['bpm']
        # df.value = df.value.astype(int)
    print(df)
    df.dateTime = pd.to_datetime(df.dateTime, infer_datetime_format=True)
    df = df.set_index('dateTime')
    rolling = df.rolling(window = '600s').mean()
    print(rolling)



    plt.plot(rolling.index, rolling.bpm, 'b.-')

    if i> 3:
        break

plt.show()
# plt.show()