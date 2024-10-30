import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Mandelbulb parameters
power = 12
max_iter = 10
threshold = 2
resolution = 100

# Initial zoom range
zoom_factor = 1.5
zoom_depth = 3  # Number of zoom levels

# Center of zoom
x_center, y_center, z_center = 0, 0, 0

# Plot each zoom level
for zoom in range(zoom_depth):
    x_vals, y_vals, z_vals = [], [], []

    # Adjust grid size based on zoom factor
    x_range = np.linspace(x_center - zoom_factor, x_center + zoom_factor, resolution)
    y_range = np.linspace(y_center - zoom_factor, y_center + zoom_factor, resolution)
    z_range = np.linspace(z_center - zoom_factor, z_center + zoom_factor, resolution)

    # Generate Mandelbulb points
    for x in x_range:
        for y in y_range:
            for z in z_range:
                zx, zy, zz = x, y, z
                r = (zx**2 + zy**2 + zz**2)**0.5
                if r == 0:  # Avoid division by zero
                    continue
                theta = np.arccos(zz / r)
                phi = np.arctan2(zy, zx)
                escape = True

                for i in range(max_iter):
                    if r > threshold:
                        escape = False
                        break
                    r = r**power
                    theta *= power
                    phi *= power
                    zx = r * np.sin(theta) * np.cos(phi) + x
                    zy = r * np.sin(theta) * np.sin(phi) + y
                    zz = r * np.cos(theta) + z

                if escape:
                    x_vals.append(x)
                    y_vals.append(y)
                    z_vals.append(z)

    # Plot the current zoom level
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_vals, y_vals, z_vals, c='black', s=0.1)
    ax.set_box_aspect([1,1,1])
    ax.set_title(f"Zoom Level {zoom + 1}")
    plt.show()

    # Reduce the zoom factor for next level
    zoom_factor /= 2