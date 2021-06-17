import os
import sys


def add_prefix_files():
    # 准备添加的前缀内容
    mark = 'val_'

    # 取路径下的文件名，生成列表
    old_names = os.listdir(path)

    # 遍历列表下的文件名    
    for old_name in old_names:
        if old_name != sys.argv[0]:
            if old_name.endswith('.png'):
            # if old_name.endswith('.txt'):
                os.rename(os.path.join(path, old_name), os.path.join(path, mark + old_name))

                print (old_name,"has been renamed successfully! New name is: ", mark + old_name)

            

if __name__ == '__main__': 
        path = r'.\data\mchar_val\val_train'
       
        add_prefix_files()


