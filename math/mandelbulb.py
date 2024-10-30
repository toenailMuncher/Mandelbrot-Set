import numpy as np
import laspy

def mandelbulb(x, y, z, max_iter=10, power=8):
    zx, zy, zz = x, y, z
    for i in range(max_iter):
        r = (zx**2 + zy**2 + zz**2)**0.5
        if r > 2.0:
            return False
        theta = np.arctan2((zx**2 + zy**2)**0.5, zz) * power
        phi = np.arctan2(zy, zx) * power
        zr = r**power
        zx = zr * np.sin(theta) * np.cos(phi) + x
        zy = zr * np.sin(theta) * np.sin(phi) + y
        zz = zr * np.cos(theta) + z
    return True

def generate_mandelbulb_points(grid_size=100, scale=2.0, max_iter=10, power=8):
    points = []
    for x in np.linspace(-scale, scale, grid_size):
        for y in np.linspace(-scale, scale, grid_size):
            for z in np.linspace(-scale, scale, grid_size):
                if mandelbulb(x, y, z, max_iter=max_iter, power=power):
                    points.append([x, y, z])
    return np.array(points)

def write_las_file(points, filename="mandelbulb.las"):
    header = laspy.LasHeader(point_format=3, version="1.2")
    las = laspy.LasData(header)
    las.x = points[:, 0]
    las.y = points[:, 1]
    las.z = points[:, 2]
    las.write(filename)

# Parameters for Mandelbulb
grid_size = 100
scale = 2.0
max_iter = 10
power = 8

# Generate Mandelbulb points
points = generate_mandelbulb_points(grid_size=grid_size, scale=scale, max_iter=max_iter, power=power)

# Write points to LAS file
write_las_file(points)