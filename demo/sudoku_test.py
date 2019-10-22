import time

from game.sudoku import *

input_num = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 3, 4, 5, 6, 7, 8, 9, 1],
             [5, 6, 7, 8, 9, 1, 2, 3, 4],
             [8, 9, 1, 2, 3, 4, 5, 6, 7],
             [3, 4, 5, 6, 7, 8, 9, 1, 2],
             [6, 7, 8, 9, 1, 2, 3, 4, 5],
             [9, 1, 2, 3, 4, 5, 6, 7, 8]]

if __name__ == '__main__':
    t = time.time()
    sudo = Sudoku(input_num)
    print(time.time()-t)
