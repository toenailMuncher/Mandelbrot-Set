import numpy as np
import matplotlib.pyplot as plt
import datetime

now = datetime.datetime.now()

colourmaps = \
['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

def plot(x, X, y, Y, cmap='Blues'):
    delta = (X - x) / 3000
    re = np.linspace(x, X, int((X - x) / delta))
    im = np.linspace(y, Y, int((Y - y) / delta))
    re, im = np.meshgrid(re, im)
    c = (re + 1j * im).reshape(im.shape[0], -1).T

    z = np.zeros_like(c)
    escape = np.zeros_like(np.absolute(c))

    for i in range(50):
        z = z * z + c
        z[np.isnan(z)] = 0
        z[np.isinf(z)] = 0
        idx = (np.absolute(z) > 4) & (escape == 0)
        escape[idx] = i

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(escape, extent=(x, X, y, Y), cmap=cmap)
    plt.show()

def plot_at(x, y, D, cmap='Blues'):
    return plot(x - D, x + D, y - D, y + D, cmap)

def interactive_zoom():
    x, y = -0.725, -0.26
    D = 0.3
    cmap = 'Blues'
    while True:
        plot_at(x, y, D, cmap)
        user_input = input("Enter zoom factor (e.g., 0.5 to zoom in, 2 to zoom out), or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        try:
            zoom_factor = float(user_input)
            D /= zoom_factor
        except ValueError:
            print("Invalid input. Please enter a numeric value for the zoom factor.")
        user_input = input("Enter new colormap (or press Enter to keep current): ")
        if user_input:
            cmap = user_input

interactive_zoom()