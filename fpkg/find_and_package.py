import os
import sys
import zipfile


def make_zip(source_dir, output_filename, keys):
    zipf = zipfile.ZipFile(output_filename, 'w')
	listfile = 'filelist.txt'
    fl = open(listfile, 'w')
    pre_len = len(os.path.dirname(source_dir))
    flag = True
    for root, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            for key in keys:
                if filename.find(key) != -1:
                    flag = False
                    fl.write(os.path.join(root, filename))
                    fl.write('\r\n')
                    pathfile = os.path.join(root, filename)
                    arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
                    zipf.write(pathfile, arcname)
    fl.close()
    zipf.write(listfile)
    zipf.close()
    os.remove(listfile)
    if flag :
        os.remove(output_filename)
        print('no same as {} file'.format(keys))

if __name__ == '__main__':
    """ 使用方法 ：
    python find_and_package.py path : path为要查找文件夹的路径
    """
    if len(sys.argv)>1 and os.path.isdir(sys.argv[1]):
        make_zip(sys.argv[1], 'SConscript.zip', ['SConscript', 'SConstruct'])
    else:
        print('no dir to zip %s' % os.path.sep)
