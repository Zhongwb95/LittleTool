class Tool:
"""
一些小工具，用于进行数据处理
"""
    def Deduplication(obj_list):
    """
    对列表中的元素去重 （python3 有效）
    """
        return list(set(obj_list))
    
    def make_triangle(x):
    """
    生成一个指定层数的杨辉三角 
    """
        Y_triangle = list()
        for i in range(1,x+1):
            num = list()
            for j in range(1,i+1):
                if j==1 or j==i:
                    num.append(1)
                else:
                    num.append(Y_triangle[i-2][j-2]+Y_triangle[i-2][j-1])
            Y_triangle.append(num)
        return Y_triangle
