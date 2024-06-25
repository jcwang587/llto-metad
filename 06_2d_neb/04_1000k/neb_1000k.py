from xdatbus import neb_2d
import numpy as np
from scipy.ndimage import minimum_filter
import matplotlib.pyplot as plt


def find_local_minima(data):
    filtered_data = minimum_filter(data, size=100, mode="constant", cval=np.inf)
    local_minima = data == filtered_data
    local_minima_coords = np.argwhere(local_minima)
    return local_minima_coords


fes = np.load("y_fes_1000k.npy")

# copy fes along the reaction coordinate 1
fes = np.tile(fes, (1, 2))

local_minima_coords = find_local_minima(fes)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_1_1000k, mep_fes_1_1000k = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_1_1000k[:, 1], mep_1_1000k[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.show()

np.save("mep_fes_1_1000k.npy", mep_fes_1_1000k)

fes = np.load("y_fes_1000k.npy")

# copy fes along the reaction coordinate 2
fes = np.tile(fes, (2, 1))

local_minima_coords = find_local_minima(fes)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_2_1000k, mep_fes_2_1000k = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_2_1000k[:, 1], mep_2_1000k[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.show()

np.save("mep_fes_2_1000k.npy", mep_fes_2_1000k)
