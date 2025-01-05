import os
import numpy as np
import open3d as o3d
from plyfile import PlyData


def filter_rail_points_from_ply(ply_file):
    # read PLY file
    ply_data = PlyData.read(ply_file)
    vertex_data = ply_data['vertex'].data

    # get point cloud coordinates and labels
    points = np.vstack([vertex_data['x'], vertex_data['y'], vertex_data['z']]).T
    labels = vertex_data['label']

    # Filter points with the `label` value of `rail`(label==1)
    rail_indices = np.where(labels == 1)[0]  # edit this
    rail_points = points[rail_indices]

    # create new PCD file
    rail_pcd = o3d.geometry.PointCloud()
    rail_pcd.points = o3d.utility.Vector3dVector(rail_points)

    return rail_pcd


def process_ply_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ply"):
            ply_file = os.path.join(directory, filename)
            rail_pcd = filter_rail_points_from_ply(ply_file)

            # save new PCD file
            new_filename = os.path.join(directory, f"rail_{os.path.splitext(filename)[0]}.pcd")
            o3d.io.write_point_cloud(new_filename, rail_pcd)
            print(f"Saved: {new_filename}")


#current_directory = os.getcwd()
process_ply_files('/home/mmtlab/Desktop/Paiguang/RailOnly轨面铁轨二分类结果/test')
