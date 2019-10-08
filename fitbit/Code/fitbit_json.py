import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import os

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)



files = [i for i in os.listdir('../Data/ReyannLarkey/user-site-export/') if i.startswith('altitude')]

for file in files:
#
    with open(f'../Data/ReyannLarkey/user-site-export/{file}', "r") as read_file:
        data = json.load(read_file)

    for i in data:
        plt.plot(pd.to_datetime(i['dateTime'], infer_datetime_format=True), i['value'], 'b.')
plt.show()