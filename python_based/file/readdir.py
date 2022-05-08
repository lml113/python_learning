import os
path = r'F:\vscode\python\python_learning\python_based\file\images'

files = os.listdir(path)
for file in files:
    if file[-5:] == '.xlsx':
        # 注释部分为单纯添加后缀
        old_name = os.path.join(path, file)
        print(old_name)
        fname, bac = os.path.splitext(old_name)
        print(fname,bac)
        #new_name = os.path.join(path, file + '.xlsx')
        os.rename(old_name, fname)
        #print(file)
#print(files)