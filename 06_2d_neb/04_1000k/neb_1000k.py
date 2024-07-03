from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt


fes = np.load("y_fes_1000k.npy")

# copy fes along the reaction coordinate 1
mirrored_fes = np.flip(fes, axis=1)
fes = np.concatenate((mirrored_fes, fes), axis=1)

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], axis=1)

local_minima_coords = local_minima(fes, size=20)
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
plt.savefig("mep_1_1000k.png")
plt.show()

np.save("mep_fes_1_1000k.npy", mep_fes_1_1000k)

fes = np.load("y_fes_1000k.npy")

# copy fes along the reaction coordinate 2
fes = np.tile(fes, (2, 1))

# remove the middle 13 rows of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], axis=0)

local_minima_coords = local_minima(fes, size=20)
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
plt.savefig("mep_2_1000k.png")
plt.show()

np.save("mep_fes_2_1000k.npy", mep_fes_2_1000k)
