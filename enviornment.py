import numpy as np
import open3d as o3d
import laspy as lp

def read_las_file(filename):
    las = lp.read(filename)
    points = np.vstack((las.x, las.y, las.z)).transpose()
    return points

def visualize_point_cloud(points):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([point_cloud])

# Read the LAS file
filename = "mandelbulb.las"
points = read_las_file(filename)

# Visualize the point cloud
visualize_point_cloud(points)