import os
import numpy as np
from plyfile import PlyData

# edit this path
input_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/at/box_4cate/originPly/'
output_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/at/fake_box/getBox/'

# iterate through all PLY files
for filename in os.listdir(input_folder):
    if filename.endswith('.ply'):
        input_path = os.path.join(input_folder, filename)
        # use plyfile not open3d
        plydata = PlyData.read(input_path)
        vertex = plydata['vertex'].data

        # check if the 'label' or 'scalar_label' field exists
        if 'label' in vertex.dtype.names:
            labels = vertex['label']
        elif 'scalar_label' in vertex.dtype.names:
            labels = vertex['scalar_label']
        else:
            print(f"{filename}没有'label'或'scalar_label'字段。")
            continue

        # get x, y, z coordinates
        x = vertex['x']
        y = vertex['y']
        z = vertex['z']

        # filter points with a label == 11
        mask = labels == 11 # edit this
        if not np.any(mask):
            print(f"{filename}不存在box，已跳过")
            continue

        x = x[mask]
        y = y[mask]
        z = z[mask]
        labels = labels[mask]

        # set the label as 3
        labels = np.full_like(labels, 3) # edit this

        # save the results as TXT
        output_filename = filename.replace('.ply', '.txt')
        output_path = os.path.join(output_folder, output_filename)
        data_to_save = np.column_stack((x, y, z, labels))
        np.savetxt(output_path, data_to_save, fmt='%f %f %f %d')

        print(f"{filename}输出成功")
