import hashlib
import os
import random

WA = 'm'
TA = 's'
TO = 'p'
ZI = 'z'
sampo_ps = '5z4s6m0p4m5m5s8m3s2s6s8s6p7m4m1m9m9m7m2z3m5z9p7s3z4p9s7s3p4p8p1s7m2s' \
           '6p3z3s8s3z3s1s1s6z6p6m1p0s1p2z6m4z7s3z4z8s6z2s5m1m2p3p7z9m2p9s3s2m7m' \
           '3p5s1p6p9p1z1s5p2p3m2m8p4m7z9p7z5z6s4s7s1m5s4s7p9p6s3m4z1z2m6z2m5z1p' \
           '8p0m7p9m7z1z1m4z8s9s5m6s7p2z8m4p9s6m8m7p5p4s8p3p5p1z3m4m2z6z4p8m2s2p'


def split_with_num(s_str, num=2):
    ss = s_str
    while ss:
        yield ss[:num]
        ss = ss[num:]


def get_ps_sha256(ps_str):
    return hashlib.sha256(ps_str.encode()).hexdigest()


def save_ps_str(info_root_path, ps_str, save_path=None) -> str:
    if not save_path:
        save_path = os.sep.join(split_with_num(get_ps_sha256(ps_str)))
    file_abs_path = os.path.join(info_root_path, save_path)
    if os.path.isfile(file_abs_path):
        return save_path
    os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)
    open(file_abs_path, 'w').write(ps_str)
    return save_path


def read_ps_str(info_root_path, save_path) -> str:
    return open(os.path.join(info_root_path, save_path), 'r').read()


def generate_ps_random(num=1) -> str:
    ps = list(split_with_num(sampo_ps))
    while num:
        yield ''.join(random.sample(ps, len(ps)))
        num -= 1


def generate_and_save_ps(root_dir, num=1):
    for ps in generate_ps_random(num):
        save_ps_str(root_dir, ps)


if __name__ == '__main__':
    generate_and_save_ps(r'C:\Users\Administrator\OneDrive\游戏\quema_data', 10 ** 6)
