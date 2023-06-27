import hashlib
import os

from config import *


def split_with_num(s_str, num=2):
    ss = s_str
    while ss:
        yield ss[:num]
        ss = ss[num:]


def get_sha256_hex(ps_str):
    return hashlib.sha256(ps_str.encode()).hexdigest()


def get_sha256_dig(ps_str):
    return hashlib.sha256(ps_str.encode()).digest()


def str_to_zip_byte(ps_str) -> bytes:
    zip_byte = bytes()
    for tuple_str in split_with_num(ps_str, ZIP_PRE):
        flag = True
        t_num = 0
        for ss in tuple_str:
            if flag:
                t_num = t_num << 4 | MAP_INT.index(ss)
                flag = False
            else:
                t_num = t_num << 2 | MAP_TYPE.index(ss)
                flag = True
        zip_byte += int(t_num).to_bytes(ZIP_SUF, 'little')
    return zip_byte


def zip_byte_to_str(zip_byte) -> str:
    ps_str = ''
    for tuple_byte in split_with_num(zip_byte, ZIP_SUF):
        t_num = int.from_bytes(tuple_byte, 'little')
        ss = []
        flag = False
        for _ in range(ZIP_PRE):
            if flag:
                ss.insert(0, MAP_INT[0xf & t_num])
                t_num = t_num >> 4
                flag = False
            else:
                ss.insert(0, MAP_TYPE[0x3 & t_num])
                t_num = t_num >> 2
                flag = True
        ps_str += ''.join(ss)
    return ps_str


def save_ps_str(info_root_path, ps_str, save_path=None) -> str:
    if not save_path:
        save_path = os.sep.join(split_with_num(get_sha256_hex(ps_str)))
    file_abs_path = os.path.join(info_root_path, save_path)
    if os.path.isfile(file_abs_path):
        return save_path
    os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)
    open(file_abs_path, 'w').write(ps_str)
    return save_path


def read_ps_str(info_root_path, save_path) -> str:
    return open(os.path.join(info_root_path, save_path), 'r').read()
