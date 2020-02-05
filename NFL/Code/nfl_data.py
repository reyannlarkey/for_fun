import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.tab20b.colors)


file = '../Data/detailed/NFL_Play_by_Play_2009-2018.csv'

columns_to_keep = ['play_id', 'game_id', 'home_team', 'away_team', 'posteam', 'posteam_type', 'defteam', 'side_of_field', 'yardline_100', 'game_date', 'quarter_seconds_remaining', 'half_seconds_remaining', 'game_seconds_remaining', 'game_half', 'quarter_end', 'drive', 'sp', 'qtr', 'down', 'goal_to_go', 'time', 'yrdln', 'ydstogo', 'ydsnet', 'play_type', 'yards_gained', 'shotgun', 'no_huddle', 'qb_dropback', 'qb_kneel', 'qb_spike', 'qb_scramble', 'pass_length', 'pass_location', 'air_yards', 'yards_after_catch', 'run_location', 'run_gap', 'field_goal_result', 'kick_distance', 'extra_point_result', 'two_point_conv_result', 'home_timeouts_remaining', 'away_timeouts_remaining', 'timeout', 'timeout_team', 'td_team', 'posteam_timeouts_remaining', 'defteam_timeouts_remaining', 'total_home_score', 'total_away_score', 'posteam_score', 'defteam_score', 'score_differential', 'posteam_score_post', 'defteam_score_post', 'score_differential_post', 'no_score_prob', 'opp_fg_prob', 'opp_safety_prob', 'opp_td_prob', 'fg_prob', 'safety_prob', 'td_prob', 'extra_point_prob', 'two_point_conversion_prob',]

df = pd.read_csv(file, low_memory = False, usecols =columns_to_keep).tail(10000)
subdf = df[(df.posteam =='ATL') & (df.play_type == "pass")]

plt.plot(subdf.ydstogo.values, subdf.pass_length.values, 'b.')
plt.show()

#p, bins = np.histogram(subdf.air_yards.values, bins = np.arange(0,101, 1))
#plt.step(bins[0:-1], p)
#plt.show()


