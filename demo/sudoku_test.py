import time

from game.sudoku import *
from game.sudoku_themes import *


if __name__ == '__main__':
    t = time.time()
    sudo = Sudoku(parse_theme(Normal.n_42943))
    count = 0
    while True:
        count += 1
        for cell in sudo.cell_list:
            cell.check_self()
        if count == 80:
            break
        if sudo.check_ok():
            break
    print(sudo)
    print(count)
    print(time.time()-t)
