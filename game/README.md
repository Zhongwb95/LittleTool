# 游戏

一些游戏的实现或者解法的实现

## 数独解题实现（普通）

运行方式见demo/sudoku_test.py
输入格式见game/sudoku_puzzles.py

### 规则
```text
将数字1至9填入空格中,使得每个数字在每行/每列/每宫中各出现一次。

唯一解（Unique Solution）:
数独谜题（Puzzle）按规定填制数字，必须只能有一个结果否则不能被承认是数独谜题。
```

### 解法

本质方法有两种:

#### 摒除法:
```text
用数字去找单元内唯一可填空格。
数字可填唯一空格称为摒余解（Hidden Single）。

在我的实现中，我用约束（Constraint）作为每行/每列或每宫，即为填数字的约束。
约束自我检查即为摒除法。
class Constraint(object):
    def check_self(self):
```

#### 余数法:
```text
用格位去找唯一可填数字。
格位唯一可填数字称为唯余解（Naked Single）。

在我的实现中，我用格子（Cell）作为每一个可以填数字的格子。
格子自我检查即为余数法。
class Cell(object):
    def check_self(self):
```

### 实现的部分解释
```text
def normal_sudoku(row, col)：
这个方法可以加载异形数独地图

class Sudoku(object):
    def _init_constraint(self):
sudoku的初始化主要分为约束（Constraint）初始化和格子（Cell）初始化。

class Sudoku(object):
    def _init_cells(self, layer_map=normal_sudoku):
初始化格子时将约束有哪些格子和格子有哪些约束配置好。

class Cell(object):
    def set_value(self, value):
只要修改格子的值，就必须同步约束和其他格子的可能值。

```
