import open3d as o3d
import numpy as np

# set the background PCD file
background_pcd_path = "/home/mmtlab/Desktop/Paiguang/RailOnly轨面铁轨二分类结果/test/rail_192.168.2.215.pcd"

# use open3d to load the background
background_pcd = o3d.io.read_point_cloud(background_pcd_path)

# fit a plane using the RANSAC algorithm
plane_model, inliers = background_pcd.segment_plane(distance_threshold=0.05,
                                                    ransac_n=3,
                                                    num_iterations=1000)

# get the plane
a, b, c, d = plane_model
print(f"平面方程: {a}x + {b}y + {c}z + {d} = 0")

# visualize the point cloud and the fitted plane
pcd = o3d.geometry.PointCloud()
pcd.points = background_pcd.points
pcd.colors = background_pcd.colors

# create a mesh grid for the plane
def create_plane_mesh(a, b, c, d):
    # create a plane
    plane_size = 10.0  # size of the plane
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.array([[-plane_size, -plane_size, (-a * (-plane_size) - b * (-plane_size) + d) / c],
                         [plane_size, -plane_size, (-a * plane_size - b * (-plane_size) + d) / c],
                         [plane_size, plane_size, (-a * plane_size - b * plane_size + d) / c],
                         [-plane_size, plane_size, (-a * (-plane_size) - b * plane_size + d) / c]])
    triangles = np.array([[0, 1, 2],
                          [0, 2, 3]])
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    mesh.compute_vertex_normals()
    return mesh

plane_mesh = create_plane_mesh(a, b, c, d)
plane_mesh.paint_uniform_color([0.7, 0.7, 0.7])  # set the color

# visualize the point cloud and the fitted plane
o3d.visualization.draw_geometries([pcd, plane_mesh],
                                  window_name="PCD File with Fitted Plane",
                                  width=800,
                                  height=600,
                                  left=50,
                                  top=50,
                                  point_show_normal=False)
