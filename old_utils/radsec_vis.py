import open3d as o3d
import numpy as np

# set the background PCD file
background_pcd_path = "/home/mmtlab/Desktop/Paiguang/RailOnly轨面铁轨二分类结果/test/rail_192.168.2.215.pcd"

background_pcd = o3d.io.read_point_cloud(background_pcd_path)

# fit a plane using the RANSAC algorithm
plane_model, inliers = background_pcd.segment_plane(distance_threshold=0.05,
                                                    ransac_n=3,
                                                    num_iterations=1000)

# get the plane
[a, b, c, d] = plane_model
print(f"平面方程: {a}x + {b}y + {c}z + {d} = 0")

# visualize the point cloud and the fitted plane
pcd = o3d.geometry.PointCloud()
pcd.points = background_pcd.points
pcd.colors = background_pcd.colors

plane_mesh = o3d.geometry.TriangleMesh.create_box(width=1, height=1, depth=1)
plane_mesh.paint_uniform_color([0.7, 0.7, 0.7])  # set color
# plane_mesh.translate([0, 0, -d / c])  # move the plane along the z-axis to an appropriate position

# visualize the point cloud and the fitted plane
o3d.visualization.draw_geometries([pcd, plane_mesh],
                                  window_name="PCD File with Fitted Plane",
                                  width=800,
                                  height=600,
                                  left=50,
                                  top=50,
                                  point_show_normal=False)

