import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.tab20b.colors)



for year in [2014, 2015, 2016, 2017, 2018, 2019]:
    df = pd.read_csv(f"../Data/pbp-{year}.csv")
    off_teams = df.groupby("OffenseTeam")

    
    for team, data in off_teams:

        if team == "KC" or team == 'ATL':
            #
            # atl_offense = off_teams.get_group("KC")
            #
            # print(atl_offense.columns)

            rushes = data[(data.IsPass == 1) | (data.PlayType == "SACK")]
            rushes = rushes[(rushes.IsIncomplete == 0)]

            print(rushes.Yards.mean())
            print(rushes.Yards.sum())
            plt.scatter(year, rushes.Yards.mean())

    plt.show()
    #         p, bins = np.histogram(rushes.Yards, bins = np.arange(-10,100, 1))
    #         plt.step(bins[0:-1], p, where = 'post', label = f'{team}: AVG = {round(rushes.Yards.mean(),2)} TOT = {round(rushes.Yards.sum(),2)}')
    # plt.legend()
    # plt.title(year)
    # plt.show()

# print(rush.ToGo - rush.Down)


# plt.title(f'{name}: {rush.shape[0]} Times')
plt.show()

# rush_types = rushes.groupby('RushDirection')
#
# for name, rush in rush_types:
#     print(name)
#
#     p, bins = np.histogram(rush.Yards, bins = np.arange(0,50, 1))
#
#     print(rush.ToGo - rush.Down)
#
#
#     plt.step(bins[0:-1], p, where = 'post')
#     plt.title(f'{name}: {rush.shape[0]} Times')
#     plt.show()