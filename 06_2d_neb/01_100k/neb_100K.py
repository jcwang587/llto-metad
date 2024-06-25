from xdatbus import neb_2d
import numpy as np
from scipy.ndimage import minimum_filter
import matplotlib.pyplot as plt


def find_local_minima(data):
    filtered_data = minimum_filter(data, size=3, mode="constant", cval=np.inf)
    local_minima = data == filtered_data
    local_minima_coords = np.argwhere(local_minima)
    return local_minima_coords


fes = np.load("y_fes_100k.npy")

local_minima_coords = find_local_minima(fes)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_13_100k, mep_fes_13_100k = neb_2d(
    fes,
    local_minima_coords[1],
    local_minima_coords[3],
    n_images,
    n_steps,
    spring_constant,
)

mep_32_100k, mep_fes_32_100k = neb_2d(
    fes,
    local_minima_coords[3],
    local_minima_coords[2],
    n_images,
    n_steps,
    spring_constant,
)

mep_20_100k, mep_fes_20_100k = neb_2d(
    fes,
    local_minima_coords[2],
    local_minima_coords[0],
    n_images,
    n_steps,
    spring_constant,
)

mep_01_100k, mep_fes_01_100k = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_13_100k[:, 1], mep_13_100k[:, 0], "ro-")
plt.plot(mep_32_100k[:, 1], mep_32_100k[:, 0], "bo-")
plt.plot(mep_20_100k[:, 1], mep_20_100k[:, 0], "go-")
plt.plot(mep_01_100k[:, 1], mep_01_100k[:, 0], "yo-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.show()

np.save("mep_fes_13_100k.npy", mep_fes_13_100k)
np.save("mep_fes_32_100k.npy", mep_fes_32_100k)
np.save("mep_fes_20_100k.npy", mep_fes_20_100k)
np.save("mep_fes_01_100k.npy", mep_fes_01_100k)
