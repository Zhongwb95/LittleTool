
import os
import re

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


def remove_note(file, single='//', pre='/*', suf='*/'):
"""
将文件中的注释处理掉,返回没有注释的文件名
"""
    def make_do(s_str):
        r_str = ''
        for ch in s_str:
            dc = ''
            if ch in ['*.\\+%[](){}?^|']:
                dc = '\\'
            r_str += dc + ch
        return r_str
    single = make_do(single)
    pre = make_do(pre)
    suf = make_do(suf)
    re_line = f'({single}.*?\n)|({pre}[\s\S]*?{suf})'
    with open(file, 'rt') as sf:
        new_lines = re.sub(re_line, '', sf.read())
    filename = os.path.splitext(file)
    out_file = '%s_unote%s'%(filename[0], filename[-1])
    with open(out_file, mode='w', encoding='utf-8') as rf:
        rf.writelines(new_lines)
    return out_file

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
