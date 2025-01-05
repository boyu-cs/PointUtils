import os
import shutil

# edit this path
input_dir = '/home/mmtlab/Desktop/Paiguang/RainTest/oriOnly/'
output_dir = '/home/mmtlab/Desktop/Paiguang/RainTest/allOriOnly/'

os.makedirs(output_dir, exist_ok=True)

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if 'ori' in file and file.endswith('.pcd'):
            source_file = os.path.join(root, file)
            parent_folder_name = os.path.basename(root)
            new_file_name = parent_folder_name + '_' + file
            destination_file = os.path.join(output_dir, new_file_name)
            shutil.copy2(source_file, destination_file)
            print(f'已复制并重命名文件: {source_file} 到 {destination_file}')