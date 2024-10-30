# Mandelbrot Set Visualizations

This project explores fractals like the Mandelbrot Set, Julia Set, and Mandelbulb using Python with Pygame and Matplotlib.

Inspired by [The Coding Train's](https://www.youtube.com/user/shiffman) tutorials on fractals and creative coding.

## Fractals in Python

Starting with the Mandelbrot Set in 2D using Pygame, then moving to Julia Sets for animations. The goal is to create a 3D Mandelbulb using point clouds and voxels.

### Mandelbrot Set
The Mandelbrot Set follows a simple formula:

> z = z^2 + c

Each point on the complex plane is checked to see if it diverges or stays bounded, creating the fractal.

![Mandelbrot Set](images/mandelbrot_set.png)

### Julia Set Visualization
The Julia Set is similar to the Mandelbrot Set but uses a fixed value (c). Changing this value creates different patterns.

![Julia Set](images/julia_set.png)

### Mandelbulb: A 3D Adventure
The Mandelbulb is a 3D version of the Mandelbrot Set, visualized using point clouds and voxels.

![Mandelbulb](images/mandelbulb.png)

## Tools Used
- **Pygame**: For 2D rendering.
- **Matplotlib**: For 3D visualization.
- **Python**: Core language for all visualizations.

## Project Roadmap
1. **Mandelbrot Set in 2D**: Render using Pygame, explore colors and zoom levels.
2. **Julia Sets**: Create and animate different Julia Sets.
3. **Mandelbulb in 3D**: Create a 3D version using Matplotlib.

## Gallery
Examples of generated fractals:

![Gallery](images/gallery.png)

- **Mandelbrot Set**: Zoomed-in details.
- **Julia Sets**: Animated transformations.
- **Mandelbulb**: 3D views.

## How to Run
1. **Clone the Repository**.
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Scripts**:
   - Mandelbrot Set: `python mandelbrot.py`
   - Julia Set: `python julia.py`
   - Mandelbulb: `python mandelbulb.py`
