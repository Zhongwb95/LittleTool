
import os
import re
import random

class Password(object):
"""
根据需求生成随机字符串(可用来产生随机密码)
使用方法:
    # 第一个参数为随机字符串长度,0为8到32随机长度; 
    # 第二个参数为字符串组成成分,如:{'d':digits, 'l':line, 'u':upper, 's':special, 'o':lower}
    password = Password(8, 'udlo') 
    print(password())
    # 未进行输入校验,若第二个参数长度(类型总数)大于随机字符串长度或输入不存在类型会抛出异常
"""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    line = '_'
    special = '!@#$%^&*()+~.-=|\\?/;:><,[]{}"\'`'
    dict = {'d':digits, 'l':line, 'u':upper, 's':special, 'o':lower}

    def __init__(self, length, types='unl'):
        if self.checkInput(length, types): raise Exception
        self.length = length
        self.types = types
        self.characters = ''
        self.password = ''

    def checkInput(self, length, types):
        types = list(set(list(types)))
        keys = self.dict.keys()
        if len(types) > length:
            return True
        return sum([0 if _ in keys else 1 for _ in types])

    def getRandomChar(self):
        return self.characters[random.randint(0, len(self.characters)-1)]

    def setPasswordBase(self):
        if not self.length or self.length == 'random':
            self.length = random.randint(8,32)
        for tp in self.types:
            self.characters += self.dict.get(tp, '')

    def checkPassword(self):
        fl = self.dict.copy()
        for i,v in fl.items():
            fl[i] = 0
            for ch in v:
                if ch in self.password: fl[i] = 1
        if sum(fl.values()) == len(self.types):
            return True

    def getRandomPassword(self):
        self.setPasswordBase()
        while not self.checkPassword():
            self.password = ''
            for i in range(self.length):
                self.password += self.getRandomChar()

    def __call__(self):
        self.getRandomPassword()
        return self.password  


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
