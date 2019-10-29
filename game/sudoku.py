#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# @File    : eq_demo.py
# @Time    : 2019/10/29 19:19
# @Author  : 年少少年
# @Email   : 799571200@qq.com


import copy


def normal_sudoku(row, col):
    normal = [[1, 1, 1, 2, 2, 2, 3, 3, 3],
              [1, 1, 1, 2, 2, 2, 3, 3, 3],
              [1, 1, 1, 2, 2, 2, 3, 3, 3],
              [4, 4, 4, 5, 5, 5, 6, 6, 6],
              [4, 4, 4, 5, 5, 5, 6, 6, 6],
              [4, 4, 4, 5, 5, 5, 6, 6, 6],
              [7, 7, 7, 8, 8, 8, 9, 9, 9],
              [7, 7, 7, 8, 8, 8, 9, 9, 9],
              [7, 7, 7, 8, 8, 8, 9, 9, 9]]
    return normal[row][col]


class Constraint(object):

    def __init__(self, value):
        self.value = value
        self.unused_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def get_cells(self):
        return self.cells

    def finish_check(self):
        finish = 1
        for cell in self.cells:
            finish *= cell.get_value()
        return 1 if finish == 362880 else 0

    def check_self(self):
        for num in self.unused_numbers:
            tmp = []
            for cell in self.cells:
                if num in cell.able_num:
                    tmp.append(cell)
            if len(tmp) == 1:
                tmp[0].set_value(num)


class Cell(object):
    def __init__(self, row, col, layer):
        self.row = row
        self.col = col
        self.layer = layer
        self.constraints = [row, col, layer]
        self.able_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = 0

    def check_self(self):
        if self.able_num and len(self.able_num) == 1:
            self.set_value(self.able_num[0])

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value:
            self.value = value
            self.able_num = []
            self.set_cells_able_num()

    def set_cells_able_num(self):
        for constraint in self.constraints:
            if self.value in constraint.unused_numbers:
                constraint.unused_numbers.remove(self.value)
            for cell in constraint.get_cells():
                if self.value in cell.able_num:
                    cell.able_num.remove(self.value)

    def __str__(self):
        return f'({self.row.value},{self.col.value}) {self.value} {self.able_num}'

    def __eq__(self, other):
        if type(other) == type(self):
            return self.value == other.value and self.able_num == other.able_num


class Layer(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)

    def __str__(self):
        out_str = ''
        for i in range(len(self.cells)):
            if (i + 1) % 3:
                out_str += f'{self.cells[i].get_value()}  '
            else:
                out_str += f'{self.cells[i].get_value()}\n'
        return out_str.strip()


class Row(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)

    def __str__(self):
        return '  '.join([str(cell.get_value()) for cell in self.cells])


class Column(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)

    def __str__(self):
        return '\n'.join([str(cell.get_value()) for cell in self.cells])


class Sudoku(object):

    def __init__(self, input_num):
        self.rows = []
        self.cols = []
        self.layers = []
        self.constraints_list = [self.rows, self.cols, self.layers]
        self.cell_list = []
        self._init_constraint()
        self._init_cells()
        self._init_number(input_num)

    def _init_number(self, input_num):
        for cell in self.cell_list:
            value = input_num[cell.row.value][cell.col.value]
            cell.set_value(value)

    def _init_constraint(self):
        for i in range(9):
            self.rows.append(Row(i))
            self.cols.append(Column(i))
            self.layers.append(Layer(i))

    def _init_cells(self, layer_map=normal_sudoku):
        for row in self.rows:
            for col in self.cols:
                layer = self._get_layer(row.value, col.value, layer_map)
                cell = Cell(row, col, layer)
                self.cell_list.append(cell)
                row.add_cell(cell)
                col.add_cell(cell)
                layer.add_cell(cell)

    def _get_layer(self, row, col, layer_map):
        value = -1
        if callable(layer_map):
            value += layer_map(row, col)
        elif isinstance(layer_map, list):
            if isinstance(layer_map[0], list):
                value += layer_map[row][col]
        return self.layers[value]

    def finish_check(self):
        finish = 1
        for constraints in self.constraints_list:
            for constraint in constraints:
                finish *= constraint.finish_check()
        return True if finish else False

    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])

    def __eq__(self, other):
        if type(other) == type(self):
            t = 1
            for i in range(81):
                t *= self.cell_list[i] == other.cell_list[i]
            return True if t else False

    def constraints_check(self):
        for constraints in self.constraints_list:
            for constraint in constraints:
                constraint.check_self()

    def cells_check(self):
        for cell in self.cell_list:
            cell.check_self()

    def recursion_solution(self):
        # TODO 递归解题，又名暴力解题。等想实现再说吧
        pass

    def routine_solution(self):
        count = 0  # 统计进行了多少次解题（一次就是进行一次检查）
        flag = 1  # 一种方法解不了换另一种
        sc = 2  # 用于,解不了就早点退出
        while not self.finish_check():
            count += 1
            sc -= 1
            last_cells = copy.deepcopy(self.cell_list)
            # 解题方法控制
            if flag + 1:
                self.constraints_check()
            else:
                self.cells_check()
            # 解题退出控制
            if last_cells == self.cell_list:
                flag *= -1
            else:
                sc = 2
            if not sc:
                return False, count
        else:
            return True, count


def parse_puzzle(theme_str):
    count = 0
    out = [[], [], [], [], [], [], [], [], []]
    if isinstance(theme_str, str) and len(theme_str) == 81:
        for num in theme_str:
            out[int(count/9)].append(int(num))
            count += 1
    else:
        raise Exception(f'input error {theme_str}')
    return out
