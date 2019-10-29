import time

from game.sudoku import *
from game.sudoku_puzzles import *


if __name__ == '__main__':
    t = time.time()
    puzzle = parse_puzzle(Expert.e_00030)
    sudo = Sudoku(puzzle)
    print(sudo)
    re, count = sudo.routine_solution()
    print('解题成功' if re else '解题失败')
    print(count)
    print(sudo)
    print(time.time()-t)
