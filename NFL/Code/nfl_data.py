import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.tab20b.colors)




colors = ['blue', 'red']
for i, year in enumerate([2019]):
    df = pd.read_csv(f"../Data/pbp/pbp-{year}.csv")
    off_teams = df.groupby("OffenseTeam")
    print(df.columns.values)
    atl = off_teams.get_group("ATL")
    kc = off_teams.get_group("KC")

    fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)
    for j, team in enumerate([kc, atl]):


        down2_plays = team[team.Down == 2]
        plays = down2_plays.groupby("PlayType")

        for name, play in plays:
            if name == 'PASS':
                quarters = play.groupby("Quarter")
                for quarter, data in quarters:

                    axes[j].scatter(data.ToGo, data.Yards, label = f"{name}, ({data.shape[0]}), ({quarter})")

        axes[j].plot([0,30], [0, 30], 'k-')

        axes[j].set_title(team.OffenseTeam.values[0])
        axes[j].set_ylabel("Yards Gained")
        axes[j].set_xlabel("Yards To Go")

        axes[j].legend()
    plt.suptitle(f"Down {down2_plays.Down.values[0]}")
    plt.show()



#     for team, data in off_teams:
#
#         if team == "ATL":
#
#             #
#             # atl_offense = off_teams.get_group("KC")
#             #
#             # print(atl_offense.columns)
#
#             passes = data[(data.IsPass == 1) | (data.PlayType == "SACK")]
#             passes = passes[(passes.IsIncomplete == 0)]
#
#             prob = passes.PassType.value_counts()
#             # threshold = 0.02
#             # mask = prob > threshold
#             # tail_prob = prob.loc[~mask].sum()
#             # prob = prob.loc[mask]
#             # prob['other'] = tail_prob
#
#
#             prob.plot(kind='bar', color = 'None', edgecolor = colors[i], linewidth = 4, label = year)
#             plt.xticks(rotation=25)
# plt.legend()
# plt.show()