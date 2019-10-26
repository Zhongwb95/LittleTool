import time

from game.sudoku import *
from game.sudoku_puzzles import *


if __name__ == '__main__':
    t = time.time()
    puzzle = parse_puzzle(Normal.n_42944)
    sudo = Sudoku(puzzle)
    print(sudo)
    sudo.routine_solution()
    print(sudo)
    print(time.time()-t)
