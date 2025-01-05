# PointUtils
This repository has some utils I made in the process of processing point clouds.
The following is brief introduction of different utility.

## old_utils
The code in [old_utils](old_utils) is old, most of them have alternatives in the new utils.

This is just an archive.

### [ave_point.py](old_utils%2Fave_point.py)
This code is used to calculate the number of points in each file and the average number of points in the entire folder in the PLY file.

### [get_all_ply.py](old_utils%2Fget_all_ply.py)
This code is used to find all PLY files in a folder. I personally think this code is stupid and should have been written when I was dizzy or when I was practicing "how to write a loop in Python".

### [get_box_to_3.py](old_utils%2Fget_box_to_3.py)
This code is used to filter points with a particular label number and save it as a TXT file. I refactored this code in the filter.py file and made it more convenient to use.

### [rail_point.py](old_utils%2Frail_point.py)
This code is used to filter points with a particular label number and save it as a PCD file. 

### [get_ori_pcd.py](old_utils%2Fget_ori_pcd.py)
This code is used to filter out the original point cloud files (PCD files with ori in the name) from the radar data stream and add the name of the parent folder (corresponding IP address) to the file name.

### [radsec_vis.py](old_utils%2Fradsec_vis.py)
This code is used to load a point cloud file, fit a plane via the RANSAC algorithm, and visualize the point cloud and the fitted plane.

### [caculateE_Distance.py](old_utils%2FcaculateE_Distance.py)
This code is an improvement of [radsec_vis.py](old_utils%2Fradsec_vis.py). This code is used to load a point cloud file, fit a plane via the RANSAC algorithm, and visualize the point cloud and the fitted plane.

### [new_cac.py](old_utils%2Fnew_cac.py)
This code is an improvement of [caculateE_Distance.py](old_utils%2FcaculateE_Distance.py). It first fits a plane and then calculates the maximum, minimum, and average Euclidean distances of all points to the plane.

