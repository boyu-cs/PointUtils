import os

# retrieve all file and folder names in the specified directory
dir_path = './'
file_names = os.listdir(dir_path)

# excluding folders
file_names = [f for f in file_names if os.path.isfile(os.path.join(dir_path, f))]

with open('file_names.txt', 'w', encoding='utf-8') as file:
    for f in file_names:
        # add a newline character after each file name
        file.write(f + '\n')

print("文件名已保存到 file_names.txt。")
