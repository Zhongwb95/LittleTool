#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# @File    : eq_demo.py
# @Time    : 2019/10/29 19:19
# @Author  : 年少少年
# @Email   : 799571200@qq.com


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(self) == type(other):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == '__main__':
    p_list = [Point(x, x) for x in range(9)]
    pp_list = [Point(x, x) for x in range(1, 10)]
    ps_list = [Point(x, x) for x in range(1, 10)]

    l1 = [1,2,3,4,5,6,7,8,9]
    l2 = [1,2,3,4,5,6,7,8,9]

    print(l1 == l2)

    print(p_list == pp_list)

    print(pp_list == ps_list)
