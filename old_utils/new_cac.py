import open3d as o3d
import os
import numpy as np
import pandas as pd

# set the background PCD file
background_pcd_path = "/home/mmtlab/Desktop/Paiguang/计算abnormal距离/OriginRailway/192.168.4.181.ply"

pcd_directory = "/home/mmtlab/Desktop/Paiguang/计算abnormal距离/test/192.168.4.181"

# fit a plane of background PCD file using the RANSAC algorithm
background_pcd = o3d.io.read_point_cloud(background_pcd_path)
plane_model, inliers = background_pcd.segment_plane(distance_threshold=0.01,
                                                    ransac_n=3,
                                                    num_iterations=1000)

# get the plane
[a, b, c, d] = plane_model
print(f"平面方程: {a}x + {b}y + {c}z + {d} = 0")

# init a result list
results = []


# Define a function to calculate the Euclidean distance from a point to a plane
def calculate_distance_to_plane(point, plane_params):
    a, b, c, d = plane_params
    x, y, z = point
    distance = (a * x + b * y + c * z + d) / np.sqrt(a ** 2 + b ** 2 + c ** 2)
    return distance


# iterate through all PCD files in the folder, calculate the Euclidean distance from each point to the plane,
# and record statistical data
for filename in os.listdir(pcd_directory):
    if filename.endswith(".pcd"):
        pcd = o3d.io.read_point_cloud(os.path.join(pcd_directory, filename))
        points = np.asarray(pcd.points)

        distances = np.array([calculate_distance_to_plane(point, plane_model) for point in points])

        max_distance = np.max(distances)
        min_distance = np.min(distances)
        avg_distance = np.mean(distances)
        point_count = len(points)

        results.append([filename, point_count, max_distance, min_distance, avg_distance])

# turn the result to DataFrame
df = pd.DataFrame(results, columns=["文件名", "点数", "最大距离", "最小距离", "平均距离"])

# export the results to a CSV file
output_csv = "192.168.4.181.csv"
df.to_csv(output_csv, index=False)
print(f"结果已保存到 {output_csv}")
