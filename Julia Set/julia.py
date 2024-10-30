import pygame
import numpy as np
import math

# Screen dimensions
WIDTH, HEIGHT = 640, 360

# Mandelbrot parameters
max_iterations = 100
angle = 0

# Initialize colors array
colors = []

# Set up colors for each iteration
for n in range(max_iterations):
    hue = math.sqrt(n / max_iterations)
    r = int(255 * hue)
    g = int(255 * (1 - hue))
    b = 150
    colors.append((r, g, b))

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Julia Set")
clock = pygame.time.Clock()

# Main loop

running = True
while running:
    screen.fill((255, 255, 255))

    # Calculate parameters for Julia Set
    ca = math.cos(angle * 3.213)
    cb = math.sin(angle)
    angle += 0.02

    # Complex plane dimensions
    w = 5
    h = w * HEIGHT / WIDTH

    xmin = -w / 2
    ymin = -h / 2
    xmax = xmin + w
    ymax = ymin + h

    # Calculate step increments for complex plane
    dx = (xmax - xmin) / WIDTH
    dy = (ymax - ymin) / HEIGHT

    # Iterate over each pixel
    y = ymin
    for j in range(HEIGHT):
        x = xmin
        for i in range(WIDTH):
            a, b = x, y
            n = 0
            while n < max_iterations:
                aa = a * a
                bb = b * b
                if aa + bb > 4.0:
                    break
                twoab = 2.0 * a * b
                a = aa - bb + ca
                b = twoab + cb
                n += 1

            # Set pixel color
            if n == max_iterations:
                color = (0, 0, 0)  # Black for points that never escape
            else:
                color = colors[n]  # Precomputed color for each iteration

            screen.set_at((i, j), color)
            x += dx
        y += dy

    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 FPS

    # Event handling (close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()