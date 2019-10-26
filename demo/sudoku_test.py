import time

from game.sudoku import *
from game.sudoku_puzzles import *


if __name__ == '__main__':
    t = time.time()
    sudo = Sudoku(parse_theme(Normal.n_42944))
    print(sudo)
    sudo.routine_solution()
    print(sudo)
    print(time.time()-t)
