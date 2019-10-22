import os
import sys
import zipfile


def make_zip(src_dir='', output='', keys=[]):

    src_dir = src_dir.rstrip(os.path.sep)  # 干掉末尾的'/'或'\'
    if not output:
        index = src_dir.rfind(os.path.sep) 
        output = '{}.zip'.format(src_dir[index+1:])  # 以源路径最后的作为压缩文件名
    zipf = zipfile.ZipFile(output, 'w')
    list_file = 'filelist.txt'
    fl = open(list_file, 'w')  # 创建压缩文件的记录文件
    pre_len = len(os.path.dirname(src_dir))
    flag = True
    for root, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            for key in keys:
                if filename.find(key) != -1:
                    flag = False
                    pathfile = os.path.join(root, filename)
                    arcname = pathfile[pre_len:].strip(os.path.sep)   # 相对路径
                    zipf.write(pathfile, arcname)
                    fl.write(arcname)
                    fl.write('\r\n')
    fl.close()
    zipf.write(list_file)
    zipf.close()
    os.remove(list_file)
    if flag:
        os.remove(output)
        print('no same as {} file'.format(keys))


if __name__ == '__main__':
    """ 使用方法 ：
    python package.py path : path为要查找文件夹的路径
    """
    if len(sys.argv)>1: 
        src_dir = sys.argv[1]
        if os.path.isdir(src_dir):
            make_zip(src_dir=src_dir, keys=['SConscript', 'SConstruct'])
        else:
            print('No such directory: %s' % src_dir)
    else:
        print('Not enough arguments')

