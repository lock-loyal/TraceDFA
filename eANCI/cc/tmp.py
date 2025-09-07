import os
print("开始执行...")

# 遍历当前目录下的所有文件
for filename in os.listdir('.'):
    # 判断是否是.java文件
    if filename.endswith('.java'):
        # 构造新文件名
        new_filename = filename[:-5] + '.txt'
        # 重命名文件
        os.rename(filename, new_filename)