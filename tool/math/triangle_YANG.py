

def make_triangle(x):
    """
    生成一个指定层数的杨辉三角列表
    如：x=5 时列表如下
    [   [1],
       [1,1],
      [1,2,1],
     [1,3,3,1],
    [1,4,6,4,1], ]
    """
    Y_triangle = list()
    for i in range(1, x+1):
        num = list()
        for j in range(1, i+1):
            if j == 1 or j == i:
                num.append(1)
            else:
                num.append(Y_triangle[i-2][j-2]+Y_triangle[i-2][j-1])
        Y_triangle.append(num)
    return Y_triangle

