import hashlib
from string import *

key = 'password'
lib_char = '_' + ascii_letters + '_' + digits + '_'

if __name__ == '__main__':
    password = 'password'
    m = hashlib.md5()
    m.update(key.encode())
    m.update(password.encode())
    byte = m.digest()
    new_string = ''
    for b in byte:
        new_string += lib_char[int(b) % len(lib_char)]
    print(new_string)
