import numpy as np
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Julia Set")

# Maximum number of iterations for each point on the complex plane
max_iterations = 100

# Colors to be used for each possible iteration count
colors = np.zeros((max_iterations, 3), dtype=int)

# Create the colors to be used for each possible iteration count
for n in range(max_iterations):
    hu = np.sqrt(n / max_iterations)
    colors[n] = (int(hu * 255), int(hu * 255), int(150))

def julia_set(screen, ca, cb, zoom, offset_x, offset_y):
    xmin, xmax = -zoom + offset_x, zoom + offset_x
    ymin, ymax = -zoom + offset_y, zoom + offset_y
    dx = (xmax - xmin) / WIDTH
    dy = (ymax - ymin) / HEIGHT

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

            if n == max_iterations:
                color = (0, 0, 0)
            else:
                color = colors[n]

            screen.set_at((i, j), color)
            x += dx
        y += dy

def main():
    ca, cb = -0.7, 0.27015
    zoom = 1.5
    offset_x, offset_y = 0.0, 0.0
    running = True
    dragging = False
    last_mouse_pos = None

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    dragging = True
                    last_mouse_pos = event.pos
                elif event.button == 4:  # Mouse wheel up
                    zoom /= 1.1
                elif event.button == 5:  # Mouse wheel down
                    zoom *= 1.1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    dx = (event.pos[0] - last_mouse_pos[0]) * (zoom * 2 / WIDTH)
                    dy = (event.pos[1] - last_mouse_pos[1]) * (zoom * 2 / HEIGHT)
                    offset_x -= dx
                    offset_y -= dy
                    last_mouse_pos = event.pos

        screen.fill((0, 0, 0))
        julia_set(screen, ca, cb, zoom, offset_x, offset_y)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()