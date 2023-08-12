import numpy as np
import matplotlib.pyplot as plt

width, height = 800, 800
max_iter = 100

# Define the properties of the fractal
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

image = np.zeros((height, width))

for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break 
            z = z * z + c
        ratio = i / max_iter
        image[y, x] = ratio

plt.imshow(image, extent=(xmin, xmax, ymin, ymax))
plt.show()
