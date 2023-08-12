import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

width, height = 400, 400
max_iter = 100

def generate_fractal(xmin, xmax, ymin, ymax):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    c = np.array(np.meshgrid(x, y)).reshape(2, height*width).T
    c = c[:, 0] + 1j*c[:, 1]
    z = np.copy(c)
    img = np.zeros_like(c, dtype=float)
    mask = np.ones_like(c, dtype=bool)

    for i in range(max_iter):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask[np.abs(z) > 2] = False
        img += mask.astype(float)

    img = img / max_iter
    return img.reshape((height, width))

fig, ax = plt.subplots()
im = ax.imshow(generate_fractal(-2.0, 1.0, -1.5, 1.5), extent=(-2.0, 1.0, -1.5, 1.5), animated=True)

zoom_coordinates = [(-0.747, 0.107), (-0.748, 0.107)]

def update(frame):
    index = frame // 500 % 2
    zoom_x, zoom_y = zoom_coordinates[index]
    zoom_level = (frame % 500) / 500 * 3
    
    range_x = 1.5 * (1 - zoom_level)
    range_y = 1.5 * (1 - zoom_level)
    new_xmin = zoom_x - range_x
    new_xmax = zoom_x + range_x
    new_ymin = zoom_y - range_y
    new_ymax = zoom_y + range_y
    im.set_array(generate_fractal(new_xmin, new_xmax, new_ymin, new_ymax))
    return im,

ani = FuncAnimation(fig, update, frames=1000, interval=2, blit=True) # 1000 frames for example
plt.show()