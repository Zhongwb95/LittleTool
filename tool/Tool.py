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
    dict = {'d': digits, 'l': line, 'u': upper, 's': special, 'o': lower}

    def __init__(self, length, types='oudl'):
        if not length or length == 'random':
            length = random.randint(8, 32)
        if self.check_input(length, types):
            raise Exception
        self.length = length
        self.types = types
        self.characters = ''
        self.password = ''

    def check_input(self, length, types):
        types = list(set(list(types)))
        keys = self.dict.keys()
        if len(types) > length:
            return True
        return sum([0 if _ in keys else 1 for _ in types])

    def get_random_char(self):
        return self.characters[random.randint(0, len(self.characters)-1)]

    def set_password_base(self):
        for tp in self.types:
            self.characters += self.dict.get(tp, '')

    def check_password(self):
        fl = self.dict.copy()
        for i, v in fl.items():
            fl[i] = 0
            for ch in v:
                if ch in self.password:
                    fl[i] = 1
        if sum(fl.values()) == len(self.types):
            return True

    def get_random_password(self):
        self.set_password_base()
        while not self.check_password():
            self.password = ''
            for i in range(self.length):
                self.password += self.get_random_char()

    def __call__(self):
        self.get_random_password()
        return self.password  


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
    out_file = f'{filename[0]}_note{filename[-1]})'
    with open(out_file, mode='w', encoding='utf-8') as rf:
        rf.writelines(new_lines)
    return out_file


def is_utf8(file):
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
                if b == 0:
                    continue
                if abs(b) == 1:
                    return False
                for _ in range(b-1):
                    if ord(f.read(1)) & 0xc0 != 0x80:
                        return False
    return True
