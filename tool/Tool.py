
import os

def Deduplication(obj_list):
"""
对列表中的元素去重 （python3 有效）
"""
    return list(set(obj_list))


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
    for i in range(1,x+1):
        num = list()
        for j in range(1,i+1):
            if j==1 or j==i:
                num.append(1)
            else:
                num.append(Y_triangle[i-2][j-2]+Y_triangle[i-2][j-1])
        Y_triangle.append(num)
    return Y_triangle


def remove_note(file, single='//', pre='/*', fix='*/'):
"""
将文件中的注释处理掉,返回没有注释的文件名
"""
    new_lines = []
    flag = False
    with open(file, ) as sf:
        for line in sf:
            index_ll = line.find(single)
            index_le = line.find(pre)
            index_el = line.find(fix)
            if index_ll == index_le and not flag:
                new_lines.append(line.strip())
                continue
            new_line = ''
            if index_le != -1 and index_ll != -1:
                min_index = min([index_le, index_ll])
                new_line = line[:min_index]
                if min_index == index_le:
                    flag = True
                else:
                    new_lines.append(new_line.strip())
                    continue
            if index_ll != -1 and not flag:
                new_line = line[:index_ll]
            if index_le != -1 and not flag:
                new_line = line[:index_le]
                flag = True
            if flag and index_el != -1:
                flag = False
                new_line += line[index_el+2:]
            new_lines.append(new_line.strip())
    filename = os.path.splitext(file)
    re_file = '%s_unote%s'%(filename[0], filename[-1])
    with open(re_file, mode='w', encoding='utf-8') as rf:
        rf.writelines('\n'.join(new_lines))
    return re_file

def isUtf8(file):
"""
判断文件是不是以utf-8编码
"""
    with open(file, "rb") as f:
        byte = 1
        while byte:
            byte = f.read(1)
            if byte:
                data = '{:08b}'.format(ord(byte))
                b = data.find('0')	    
                if b==0:
                    continue
                if abs(b)==1:
                    return False
                for _ in range(b-1):
                    if ord(f.read(1))&0xc0!=0x80:
                        return False
    return True
