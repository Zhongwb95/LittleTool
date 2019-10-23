

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
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def get_cells(self):
        return self.cells


class Cell(object):
    def __init__(self, row, col, layer):
        self.row = row
        self.col = col
        self.layer = layer
        self.limits = [row, col, layer]
        self.able_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = 0

    def check_self(self):
        if self.able_num and len(self.able_num) == 1:
            self.set_value(self.able_num[0])

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        if value:
            self.able_num = []
            self.set_cells_able_num()

    def set_cells_able_num(self):
        for limit in self.limits:
            for cell in limit.get_cells():
                if self.value in cell.able_num:
                    cell.able_num.remove(self.value)

    def set_able_num(self):
        if not self.value:
            for limit in self.limits:
                for cell in limit.get_cells():
                    if cell == self:
                        continue
                    if cell.get_value() in self.able_num:
                        self.able_num.remove(cell.get_value())
        print(self)

    def __str__(self):
        return f'({self.row.value},{self.col.value}) {self.value} {self.able_num}'


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
    rows = []
    cols = []
    layers = []
    cell_list = []

    def __init__(self, input_num):
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

    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])
