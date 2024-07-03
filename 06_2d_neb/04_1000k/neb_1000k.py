from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt

fes = np.load("y_fes_1000k.npy")
mirrored_fes = np.flip(fes, axis=1)
fes = np.concatenate((mirrored_fes, fes), axis=1)

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], axis=1)

local_minima_coords = local_minima(fes, size=20)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_1000k_path6_mir_rev, mep_fes_1000k_path6_mir_rev = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_1000k_path6_mir_rev[:, 1], mep_1000k_path6_mir_rev[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.savefig("mep_1000k_path6-mir-rev.png")
plt.show()

np.save("mep_fes_1000k_path6-mir-rev.npy", mep_fes_1000k_path6_mir_rev)


fes = np.load("y_fes_1000k.npy")
mirrored_fes = np.flip(fes, axis=1)
fes = np.concatenate((fes, mirrored_fes), axis=1)

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], axis=1)

local_minima_coords = local_minima(fes, size=20)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_1000k_path6_mir, mep_fes_1000k_path6_mir = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_1000k_path6_mir[:, 1], mep_1000k_path6_mir[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.savefig("mep_1000k_path6-mir.png")
plt.show()

np.save("mep_fes_1000k_path6-mir.npy", mep_fes_1000k_path6_mir)


fes = np.load("y_fes_1000k.npy")
mirrored_fes = np.flip(fes, axis=0)
fes = np.concatenate((mirrored_fes, fes), axis=0)

# remove the middle 14 rows of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], axis=0)

local_minima_coords = local_minima(fes, size=20)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_1000k_path5_mir_rev, mep_fes_1000k_path5_mir_rev = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_1000k_path5_mir_rev[:, 1], mep_1000k_path5_mir_rev[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.savefig("mep_1000k_path5-mir-rev.png")
plt.show()

np.save("mep_fes_1000k_path5-mir-rev.npy", mep_fes_1000k_path5_mir_rev)


fes = np.load("y_fes_1000k.npy")
mirrored_fes = np.flip(fes, axis=0)
fes = np.concatenate((fes, mirrored_fes), axis=0)

# remove the middle 14 rows of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], axis=0)

local_minima_coords = local_minima(fes, size=20)
n_images = 100
n_steps = 1000
spring_constant = 0.2

mep_1000k_path5_mir, mep_fes_1000k_path5_mir = neb_2d(
    fes,
    local_minima_coords[0],
    local_minima_coords[1],
    n_images,
    n_steps,
    spring_constant,
)

# plot the minimum energy path
plt.imshow(fes, cmap="viridis")
plt.plot(mep_1000k_path5_mir[:, 1], mep_1000k_path5_mir[:, 0], "ro-")
plt.xlabel("Reaction coordinate 1")
plt.ylabel("Reaction coordinate 2")
for i, (x, y) in enumerate(local_minima_coords):
    plt.text(y, x, f"{i}", color="red")
plt.colorbar()
plt.savefig("mep_1000k_path5-mir.png")
plt.show()

np.save("mep_fes_1000k_path5-mir.npy", mep_fes_1000k_path5_mir)

print("max mep_1000k_path6-mir-rev.npy", np.max(mep_fes_1000k_path6_mir_rev)-np.min(mep_fes_1000k_path6_mir_rev))
print("max mep_1000k_path6-mir.npy", np.max(mep_fes_1000k_path6_mir)-np.min(mep_fes_1000k_path6_mir))
print("max mep_1000k_path5-mir-rev.npy", np.max(mep_fes_1000k_path5_mir_rev)-np.min(mep_fes_1000k_path5_mir_rev))
print("max mep_1000k_path5-mir.npy", np.max(mep_fes_1000k_path5_mir)-np.min(mep_fes_1000k_path5_mir))
