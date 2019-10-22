

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


class Cell(object):
    able_num = []

    def __init__(self, row, col, layer):
        self.row = row
        self.col = col
        self.layer = layer


class Layer(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)


class Row(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)


class Column(Constraint):
    def __init__(self, value):
        Constraint.__init__(self, value)


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
            cell.value = input_num[cell.row.value][cell.col.value]

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
