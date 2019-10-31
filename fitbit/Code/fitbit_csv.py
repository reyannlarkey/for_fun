import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

file = '../Data/Rey_fitbit.csv'
df = pd.read_csv(file)

## NEED TO CLEAN THE HECK OUT OF THIS DATASET!

### TIME FIXING
df['start_time'] = df.Date.astype(str)+","+df.Year.astype(str)
df.start_time = pd.to_datetime(df.start_time, format = "%b %d, %I:%M%p,%Y")
df = df.drop(['Date', 'Year'], axis = 1)


# Clean Calories
df.Calories = df.Calories.astype(str).str.strip('cals')
df.Calories = df.Calories.astype(str).str.replace(',', '').astype(float)

# Clean Activity
df.Activity = df.Activity.astype(str).str.strip('Edit')
df.Activity = df.Activity.astype(str).str.replace(u'\xa0',"")

# Clean Distance
df.Distance = df.Distance.astype(str).str.strip(' miles').astype(float)

# Clean Duration
duration = df.Duration.astype(str).str.split(':').values
seconds = []
for i in duration:
    if len(i)==2:
        num_seconds = int(i[0])*60 + int(i[1])
        seconds.append(float(num_seconds))
    else:
        num_seconds = int(i[0])*3600 + int(i[1])*60 + int(i[2])
        seconds.append(float(num_seconds))

df.Duration = seconds

#############################
#    Cleaned Dataframe!     #
#############################
#
# df['Color'] = "black"
#
# df.Color[df.Activity  == 'Walk']='red'
# df.Color[df.Activity  == 'Treadmill']='green'
# df.Color[df.Activity  == 'Workout']='orange'
# df.Color[df.Activity  == 'Sport']='magenta'
# df.Color[df.Activity  == 'Hike']='yellow'
# # print(df)
fill_between = ['2018-05-04T00:00:00',
                '2018-08-27T00:00:00',
                '2019-05-03T00:00:00',
                '2019-08-26T00:00:00',
                '2019-01-01T00:00:00',
                '2019-01-31T00:00:00']
fill_between_values = pd.to_datetime(fill_between, infer_datetime_format=True)



fig, axes = plt.subplots(nrows = 4, ncols = 1, figsize = (10, 12), sharex=True, sharey = False)

groups = df.groupby('Activity')
print(df)
for group_name in ['Hike', 'Run', 'Sport', 'Treadmill', 'Walk', 'Workout']:
    group = groups.get_group(group_name)

    axes[0].plot(group.start_time, group.Duration/60.0, linestyle = 'none', marker = '.')
    axes[0].set_ylabel("Duration (Min.)")

    axes[1].plot(group.start_time, group.Distance, linestyle = 'none', marker = '.')
    axes[1].set_ylabel("Distance (Mi.)")

    axes[2].plot(group.start_time, group.Steps, linestyle = 'none', marker = '.')
    axes[2].set_ylabel("Steps")

    axes[3].plot(group.start_time, group.Calories, linestyle = 'none', marker = '.', label = group_name)
    axes[3].set_ylabel("Calories")




for ax in axes:
    ax.axvspan(fill_between_values[0], fill_between_values[1], alpha=0.25, color='green', label='Summer')
    ax.axvspan(fill_between_values[2], fill_between_values[3], alpha=0.25, color='green')
    ax.axvspan(fill_between_values[4], fill_between_values[5], alpha=0.25, color='black', label= 'new years')

plt.suptitle("All 'Activities' For Reyann")
plt.legend(loc="upper left", bbox_to_anchor=(1,3))
plt.show()


#
#
#         # axes[index].axvspan(fill_between_values[4], fill_between_values[5], alpha=0.5, color='green')
#

# plt.show()