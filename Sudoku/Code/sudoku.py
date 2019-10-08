import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('sudoku.csv', nrows = 1000000)


for number in range(1,10):


    base = np.zeros((9,9))
    for i, row in df.iterrows():
        quiz = [int(char) for char in row.quizzes]
        #sol = [int(char) for char in row.solutions]
        quiz = np.reshape(quiz, (9,9))
        #sol = np.reshape(sol, (9,9))



        bools = quiz==number    # sol = np.reshape(sol, (9, 9))
        bools = bools.astype(int)
        # print(quiz)
        # print(sol)
        base+= bools#abs(sol - quiz)
        # print(base)

    # base = base/np.float(df.shape[0])

    base = base/np.max(base)
    base = np.flip(base, 0)


    fig = plt.figure(figsize=(9,5))
    ax = fig.add_subplot(111)
    plt.pcolormesh(base, edgecolors='k', linewidth=1, cmap='jet')
    ax.set_aspect('equal')

    plt.axis('off')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    cbar = plt.colorbar(orientation='vertical', ticks = [np.min(base),1])

    cbar.ax.set_yticklabels([f'Pre-Filled Less Often\n ({round(np.min(base),2)} %)', f'Pre-Filled More Often\n ({round(np.max(base),2)} %)'])
    # plt.gca().invert_xaxis()
    plt.suptitle(f"Most Common Pre-Filled Squares\n{number}'s\n {df.shape[0]} Sudoku Games")
    plt.savefig(f"{number}_filled.png")
    plt.close()