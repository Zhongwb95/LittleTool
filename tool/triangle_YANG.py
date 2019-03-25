def make_triangle(x):
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
