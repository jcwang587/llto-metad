from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt


fes = np.load("y_fes_300k.npy")

local_minima_coords = local_minima(fes)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_13_300k, mep_fes_13_300k = neb_2d(
    fes,
    local_minima_coords[1],
    local_minima_coords[3],
    n_images,
    n_steps,
    spring_constant,
)

mep_32_300k, mep_fes_32_300k = neb_2d(
    fes,
    local_minima_coords[3],
    local_minima_coords[2],
    n_images,
    n_steps,
    spring_constant,
)

mep_20_300k, mep_fes_20_300k = neb_2d(
    fes,
    local_minima_coords[2],
    local_minima_coords[0],
    n_images,
    n_steps,
    spring_constant,
)

mep_01_300k, mep_fes_01_300k = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_13_300k[:, 1], mep_13_300k[:, 0], "ro-")
plt.plot(mep_32_300k[:, 1], mep_32_300k[:, 0], "bo-")
plt.plot(mep_20_300k[:, 1], mep_20_300k[:, 0], "go-")
plt.plot(mep_01_300k[:, 1], mep_01_300k[:, 0], "yo-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.savefig("mep_300k.png")
plt.show()

np.save("mep_fes_13_300k.npy", mep_fes_13_300k)
np.save("mep_fes_32_300k.npy", mep_fes_32_300k)
np.save("mep_fes_20_300k.npy", mep_fes_20_300k)
np.save("mep_fes_01_300k.npy", mep_fes_01_300k)
