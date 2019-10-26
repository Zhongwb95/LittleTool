import os
import sys
import zipfile


def make_zip(src_dir='', output='', keys=[]):
    src_dir = src_dir.rstrip(os.path.sep)  # 干掉末尾的'/'或'\'
    if not output:
        index = src_dir.rfind(os.path.sep) 
        output = '{}.zip'.format(src_dir[index+1:])  # 以源路径最后的作为压缩文件名
    zip_file = zipfile.ZipFile(output, 'w')
    list_file = 'file_list.txt'
    fl = open(list_file, 'w')  # 创建压缩文件的记录文件
    pre_len = len(os.path.dirname(src_dir))
    flag = True
    for root, dir_names, file_names in os.walk(src_dir):
        for filename in file_names:
            for key in keys:
                if filename.find(key) != -1:
                    flag = False
                    file_path = os.path.join(root, filename)
                    arc_name = file_path[pre_len:].strip(os.path.sep)   # 相对路径
                    zip_file.write(file_path, arc_name)
                    fl.write(arc_name)
                    fl.write('\r\n')
    fl.close()
    zip_file.write(list_file)
    zip_file.close()
    os.remove(list_file)
    if flag:
        os.remove(output)
        print('no same as {} file'.format(keys))


if __name__ == '__main__':
    """ 使用方法 ：
    python package.py path : path为要查找文件夹的路径
    """
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
        if os.path.isdir(input_dir):
            make_zip(src_dir=input_dir, keys=['SConscript', 'SConstruct'])
        else:
            print('No such directory: %s' % input_dir)
    else:
        print('Not enough arguments')
