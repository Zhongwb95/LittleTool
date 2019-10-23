import time

from game.sudoku import *

input_num = [[0, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 0, 8, 9, 1, 2, 3],
             [7, 8, 0, 1, 2, 3, 4, 5, 6],
             [2, 3, 4, 5, 0, 7, 8, 9, 1],
             [5, 6, 7, 8, 9, 1, 0, 3, 4],
             [8, 9, 1, 2, 3, 0, 5, 0, 7],
             [3, 4, 0, 6, 7, 8, 9, 1, 2],
             [6, 7, 8, 9, 1, 2, 3, 0, 5],
             [9, 1, 2, 0, 4, 5, 6, 7, 8]]

if __name__ == '__main__':
    t = time.time()
    sudo = Sudoku(input_num)
    for cell in sudo.cell_list:
        cell.check_self()

    print(time.time()-t)
