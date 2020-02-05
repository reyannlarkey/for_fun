import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

''' Constraints
Three places to check:
    1) No duplicate numbers in same row
    2) No duplicate numbers in same column
    3) No duplicate numbers in same box

    --> 9 of each number (1-9) 
'''


df = pd.read_csv('../Data/sudoku.csv', nrows = 2)


quiz = np.asarray([int(i) for i in df.quizzes.values[1]]) # convert to array of numbers
solution = np.asarray([int(i) for i in df.solutions.values[1]]) # convert to array of numbers
# print(quiz)

puzzle = quiz.reshape((9,9))
solution = solution.reshape((9,9))



class Game:
    def __init__(self, quiz):
        '''
        ###   _________________
        ### A|_|_|_|_|_|_|_|_|_|
        ### B|_|_|_|_|_|_|_|_|_|
        ### C|_|_|_|_|_|_|_|_|_|
        ### D|_|_|_|_|_|_|_|_|_|
        ### E|_|_|_|_|_|_|_|_|_|
        ### F|_|_|_|_|_|_|_|_|_|
        ### G|_|_|_|_|_|_|_|_|_|
        ### H|_|_|_|_|_|_|_|_|_|
        ### I|_|_|_|_|_|_|_|_|_|
        ###   0 1 2 3 4 5 6 7 8
        '''
        self.puzzle = quiz.reshape((9,9))
        self.y_dict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}

        self.found_new = False

    def get_square(self, x = 0,y = "A"):
        ''' returns the number in specified location'''
        return self.puzzle[self.y_dict[y]][x]

    def get_row(self, y = "A"):
        ''' returns the number in specified location'''
        return self.puzzle[self.y_dict[y]]

    def get_column(self, x = 0):
        ''' returns the number in specified location'''
        return self.puzzle[:,x]



    def get_block(self, block_num, arr="None"):
        ''' returns the indicies for the block position'''

        if arr == "None":
            arr = self.puzzle


        # y-indicies
        g = block_num//3 * 3

        rows = arr[g:g+3]

        f = block_num%3 *3
        block = rows[:, f:f+3]

        y_start = g
        x_start = f
        return block , y_start, x_start


    def get_possible_locations(self, number):
        ''' returns mask with possible locations for a given number'''
        unique, counts = np.unique(self.puzzle, return_counts=True)

        finished_nums = np.where(counts[1:] == 9)[0]+1



        if number in finished_nums:
            return dict(zip(unique, counts))

        else:
            # print(finished_nums)
            # print(number)
            # get empty locations first:
            empty_locations = (self.puzzle ==0)# locations of empty numbers

            possible_locations = empty_locations # to start

            # check rows:
            for i, row in enumerate(self.puzzle):
                if number in row:
                    possible_locations[i] = False

            # check columns:
            for i in range(9):
                column = self.get_column(x = i)
                if number in column:
                    possible_locations[:,i] = False

            # check blocks:
            for i in range(9):

                block, y_start, x_start = self.get_block(i)

                if number in block:
                    possible_locations[y_start:y_start+3, x_start:x_start+3] = False

            # print(number)
            # print(possible_locations)
            self.found_new= False
            for i in range(9):
                block, y_start, x_start = self.get_block(i, arr=possible_locations)
                if block.sum()==1:

                    y_pos, x_pos = np.where(block == 1)
                    y_pos+=y_start
                    x_pos+=x_start

                    self.puzzle[y_pos,x_pos] = number
                    # print(f"Found where a {number} goes!: {x_pos, y_pos}")
                    self.found_new = True

            unique, counts = np.unique(self.puzzle, return_counts=True)

        return dict(zip(unique, counts))


df = pd.read_csv('../Data/sudoku.csv', nrows = 2000)

iterations = []
for j in range(df.shape[0]):
    quiz = np.asarray([int(i) for i in df.quizzes.values[j]]) # convert to array of numbers
    solution = np.asarray([int(i) for i in df.solutions.values[j]]) # convert to array of numbers
    # print(quiz)

    puzzle = quiz.reshape((9,9))
    solution = solution.reshape((9,9))


    p = Game(quiz)
    # print(p.puzzle)
    # p.get_block(0)
    # p.get_block(1)
    # p.get_block(2)
    # p.get_block(3)


    # p.get_possible_locations(1)


    dict1 = p.get_possible_locations(1)
    count = 0
    while not np.array_equal(p.puzzle, solution):
        for i in range(1,10):
            count +=1
            dict1 = p.get_possible_locations(i)
            # print(dict1)
    print(count)
    iterations.append(count)
    # print(p.puzzle)
    # print(solution)


p, bins = np.histogram(iterations, bins = np.arange(0,100,5))
plt.step(bins[0:-1], p, where = 'post')
plt.show()