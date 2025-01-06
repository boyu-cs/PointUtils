import os
import numpy as np
from plyfile import PlyData, PlyElement

def txt_to_ply(txt_folder_path, ply_folder_path):
    # get all TXT files
    txt_files = [f for f in os.listdir(txt_folder_path) if f.endswith('.txt')]

    for txt_file in txt_files:
        txt_file_path = os.path.join(txt_folder_path, txt_file)
        ply_file_path = os.path.join(ply_folder_path, txt_file[:-4] + '.ply')  # 创建 PLY 文件名

        vertex_data = []

        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                values = line.strip().split()

                # make sure the file has x, y, z, class or give it a default value
                x, y, z = float(values[0]), float(values[1]), float(values[2])
                class_val = int(float(values[3])) if len(values) > 3 else 1
                # intensity = 1  # default intensity
                # scan_angle_rank = 1  # default scan angle rank
                # number_of_returns = 1  # default number of returns

                # vertex_data.append((x, y, z, class_val, intensity, scan_angle_rank, number_of_returns))
                vertex_data.append((x, y, z, class_val))

        vertex_data_np = np.array(vertex_data, dtype=[
            ('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
            ('label', 'i4')
        ])

        vertex = PlyElement.describe(vertex_data_np, 'vertex')
        # vertex = PlyElement.describe(vertex_data, 'vertex')

        ply_data = PlyData([vertex])
        ply_data.write(ply_file_path)


# edit this path
txt_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/test/'
ply_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/test/'
txt_to_ply(txt_folder, ply_folder)
