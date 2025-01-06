import os
import open3d as o3d
def calculate_average_points(folder_path):
    # get all files in folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.ply')]

    if not files:
        print("文件夹中没有 PLY 文件。")
        return

    total_points = 0
    num_files = len(files)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        # read PLY file
        pcd = o3d.io.read_point_cloud(file_path)
        num_points = len(pcd.points)
        total_points += num_points
        print(f"{file_name} 的点数: {num_points}")

    average_points = total_points / num_files
    print(f"所有 PCD 文件的平均点数: {average_points}")


# edit this path
folder_path = "/home/mmtlab/Desktop/code/RandLA-Net-PyTorch/Paiguang/preprocess_data/input_0.060"
calculate_average_points(folder_path)
