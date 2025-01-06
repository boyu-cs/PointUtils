import os
from plyfile import PlyData
import numpy as np


def process_ply_files(input_folder, output_folder, mapping_dict):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # iterate through all PLY files
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.ply'):
            # read PLY file
            ply_path = os.path.join(input_folder, file_name)
            ply_data = PlyData.read(ply_path)

            # get the list of attribute names
            property_names = [prop.name for prop in ply_data['vertex'].properties]

            # whether the file contains `class` or `scalar_label`
            if 'class' in property_names:
                label_type = 'class'
            elif 'scalar_label' in property_names:
                label_type = 'scalar_label'
            else:
                print(f"{file_name} 文件没有class或scalar_label属性，跳过处理")
                continue  # skip this file

            # get x, y, z and class/scalar_label
            points = np.vstack([ply_data['vertex']['x'],
                                ply_data['vertex']['y'],
                                ply_data['vertex']['z'],
                                ply_data['vertex'][label_type]]).T

            # filter and remap
            selected_points = []
            for point in points:
                original_label = int(point[3])
                if original_label in mapping_dict:
                    # remap the labels
                    new_label = mapping_dict[original_label]
                    selected_points.append([point[0], point[1], point[2], new_label])

            # output the filtered points to a TXT file
            output_file = os.path.join(output_folder, file_name.replace('.ply', '.txt'))
            np.savetxt(output_file, selected_points, fmt="%.6f %.6f %.6f %d", comments='')

            print(f"{file_name} 文件处理完成")


if __name__ == "__main__":
    # edit this path
    input_folder = "/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/2cate_train_test/originData/train_ori/"
    output_folder = "/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/2cate_train_test/originData/allTxt/"

    # label mapping table
    # e.g., map original label 0 to 1, and label 1 to 2
    mapping_dict = {
        0: 0,
        4: 1,
    }

    process_ply_files(input_folder, output_folder, mapping_dict)
