import time

from game.sudoku import *

normal_30 = [[0, 2, 0, 8, 3, 4, 0, 0, 1],
             [0, 8, 0, 1, 7, 0, 2, 0, 3],
             [9, 0, 1, 5, 2, 0, 7, 0, 8],
             [0, 0, 3, 7, 5, 0, 0, 0, 4],
             [0, 7, 0, 3, 6, 0, 0, 9, 0],
             [5, 6, 0, 0, 4, 0, 3, 0, 0],
             [0, 4, 0, 6, 8, 0, 1, 3, 0],
             [0, 0, 9, 0, 0, 0, 4, 8, 0],
             [0, 1, 0, 4, 9, 3, 0, 0, 7]]

expert_30 = [[0, 8, 7, 5, 0, 0, 0, 6, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 2],
             [0, 5, 4, 0, 0, 0, 0, 3, 0],
             [1, 3, 0, 0, 7, 0, 0, 0, 0],
             [0, 2, 0, 0, 5, 1, 0, 0, 9],
             [0, 0, 0, 0, 8, 0, 0, 4, 0],
             [0, 0, 0, 4, 0, 6, 0, 7, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 3],
             [8, 0, 0, 7, 0, 0, 0, 9, 0]]

if __name__ == '__main__':
    t = time.time()
    sudo = Sudoku(expert_30)
    count = 0
    while True:
        count += 1
        for cell in sudo.cell_list:
            cell.check_self()
        if count == 100:
            break
        if sudo.check_ok():
            break
    print(sudo)
    print(count)
    print(time.time()-t)
