# import plyfile
# import numpy as np
# import open3d as o3d
# import os
# import glob
#
# '''
# input = PCD
# '''
# input_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/withTrain_5cate_all_torch_17/allPcd/'
# output_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/withTrain_5cate_all_torch_17/allPly/'
#
# os.makedirs(output_folder, exist_ok=True)
#
# pcd_files = glob.glob(os.path.join(input_folder, '*.pcd'))
#
# # iterate all PCD files
# for pcd_file in pcd_files:
#
#     pcd = o3d.io.read_point_cloud(pcd_file)
#     filename = os.path.splitext(os.path.basename(pcd_file))[0]
#
#     # write the point cloud data to a new PLY file
#     ply_file = os.path.join(output_folder, filename + '.ply')
#     o3d.io.write_point_cloud(ply_file, pcd)
#
#     # use plyfile read PLY file
#     plydata = plyfile.PlyData.read(ply_file)
#
#     # get vertex data from PLY file
#     vertex = plydata['vertex']
#
#     # create new vertex data
#     new_vertex_data = np.zeros(vertex.count, dtype=[
#         ('x', 'double'),
#         ('y', 'double'),
#         ('z', 'double'),
#         ('class', 'u1'),
#         ('intensity', 'i2'),
#         ('scan_angle_rank', 'i1'),
#         ('number_of_returns', 'u1'),
#     ])
#
#     # copy the original attributes
#     for prop in vertex.properties:
#         new_vertex_data[prop.name] = vertex[prop.name]
#
#     # add four new attributes (adjustable)
#     new_vertex_data['class'] = 1
#     new_vertex_data['intensity'] = 1
#     new_vertex_data['scan_angle_rank'] = 1
#     new_vertex_data['number_of_returns'] = 1
#
#     # create new PLY data
#     new_plydata = plyfile.PlyData(
#         [plyfile.PlyElement.describe(new_vertex_data, 'vertex')],
#         text=False
#     )
#
#     # save a new PLY file
#     new_ply_file = os.path.join(output_folder, filename + '.ply')
#     new_plydata.write(new_ply_file)
#
# print("所有PCD文件已处理完毕。")


import os
import numpy as np
from plyfile import PlyData, PlyElement
import math
from termcolor import cprint  # Import termcolor for colored console output

'''
input = TXT
'''

def txt_to_ply(txt_folder_path, ply_folder_path):
    # Ensure the output folder exists
    os.makedirs(ply_folder_path, exist_ok=True)

    # get all TXT files
    txt_files = [f for f in os.listdir(txt_folder_path) if f.endswith('.txt')]

    # iterate all TXT file
    for txt_file in txt_files:
        txt_file_path = os.path.join(txt_folder_path, txt_file)
        ply_file_path = os.path.join(ply_folder_path, txt_file[:-4] + '.ply')  # Create the PLY filename

        # initialize vertex data list
        vertex_data = []

        # read each line from the TXT file
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                values = line.strip().split()

                try:
                    # ensure at least x, y, z, class properties exist; otherwise set default values
                    x, y, z = float(values[0]), float(values[1]), float(values[2])
                    class_val = float(values[3]) if len(values) > 3 else 1.0

                    # check for NaN values
                    if math.isnan(x) or math.isnan(y) or math.isnan(z) or math.isnan(class_val):
                        raise ValueError("NaN encountered")

                    # convert class_val to integer
                    # add three new attributes (adjustable)
                    class_val = int(class_val)
                    intensity = 1.0
                    scan_angle_rank = 1
                    number_of_returns = 1

                    # add vertex data as a tuple to the list
                    vertex_data.append((x, y, z, class_val, intensity, scan_angle_rank, number_of_returns))

                except ValueError:
                    # print error message in red text and skip the file
                    cprint(f"[File Error] \"{txt_file}\" 存在 NaN 项", 'red')
                    break  # Exit the loop to skip processing this file

        # skip writing if vertex_data is empty due to NaN values
        if not vertex_data:
            continue

        # create a NumPy array for vertex data
        vertex_data_np = np.array(vertex_data, dtype=[
            ('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
            ('class', 'i4'), ('intensity', 'f4'),
            ('scan_angle_rank', 'i4'), ('number_of_returns', 'i4')
        ])

        # create a PlyElement using the NumPy array
        vertex = PlyElement.describe(vertex_data_np, 'vertex')

        # create a PlyData object and write to file
        ply_data = PlyData([vertex])
        ply_data.write(ply_file_path)

# edit this path
txt_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/withTrain_5cate_all_torch_17/bg/allTxt/'  # 你的txt文件所在的文件夹路径
ply_folder = '/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/withTrain_5cate_all_torch_17/bg/allPly/'
txt_to_ply(txt_folder, ply_folder)
print("所有TXT文件已处理完毕。")