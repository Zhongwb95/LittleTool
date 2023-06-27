import random

from common import *
from db import DataBase

sampo_ps = '5z4s6m0p4m5m5s8m3s2s6s8s6p7m4m1m9m9m7m2z3m5z9p7s3z4p9s7s3p4p8p1s7m2s' \
           '6p3z3s8s3z3s1s1s6z6p6m1p0s1p2z6m4z7s3z4z8s6z2s5m1m2p3p7z9m2p9s3s2m7m' \
           '3p5s1p6p9p1z1s5p2p3m2m8p4m7z9p7z5z6s4s7s1m5s4s7p9p6s3m4z1z2m6z2m5z1p' \
           '8p0m7p9m7z1z1m4z8s9s5m6s7p2z8m4p9s6m8m7p5p4s8p3p5p1z3m4m2z6z4p8m2s2p'


def generate_ps_random(num=1) -> str:
    ps = list(split_with_num(sampo_ps))
    while num:
        yield ''.join(random.sample(ps, len(ps)))
        num -= 1


def generate_and_save_ps(db_file, num=1):
    db = DataBase(db_file)
    pack = []
    for ps in generate_ps_random(num):
        if len(pack) == 2 ** 18:
            db.save_data(pack)
            pack = []
        pack.append((get_sha256_dig(ps), str_to_zip_byte(ps)))
        # pack.append((get_sha256_hex(ps), ps))
    db.save_data(pack)
    db.close()


if __name__ == '__main__':
    root_dirs = r'C:\Users\Administrator\OneDrive\游戏\quema_data'
    # DataBase(os.path.join(root_dirs, 'qm.db'), True).close()
    # DataBase(os.path.join(root_dirs, 'qm2.db'), True).close()
    # generate_and_save_ps(os.path.join(root_dirs, 'qm.db'), 10 ** 6)
    pass
    zip_bt = str_to_zip_byte(sampo_ps)
    print(sampo_ps)
    print(zip_bt.hex())

    sha256 = 'aa01d13be6494ecba1bb6f7c0cf74510712ae73a817c7885d3c65b259e51c886'
    db = DataBase(os.path.join(root_dirs, 'qm.db'))
    db.get_data(bytes.fromhex(sha256))
