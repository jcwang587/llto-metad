import numpy as np
import alphashape
from matplotlib import pyplot as plt
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess


def calculate_length(mep):
    diff = np.diff(mep, axis=0)
    segment_lengths = np.sqrt(np.sum(diff ** 2, axis=1))
    return np.sum(segment_lengths)


def get_alpha_shape(points, alpha=0.05):
    if len(points) > 3:
        alpha_shape = alphashape.alphashape(points[:, [0, 2]], alpha)
        boundary_points = np.array(list(alpha_shape.exterior.coords))
    else:
        boundary_points = points[:, [0, 2]]
    return boundary_points


# load npy file
fes = np.load('fes_data_3d.npy')
fes_2d = np.min(fes, axis=1)
fes_size = fes.shape
mep_1 = np.load('../../06_2d_neb/01_100k/mep_13_100k.npy')
mep_2 = np.load('../../06_2d_neb/01_100k/mep_32_100k.npy')
mep_3 = np.load('../../06_2d_neb/01_100k/mep_20_100k.npy')
mep_4 = np.load('../../06_2d_neb/01_100k/mep_01_100k.npy')

# get the length of the mep
length_1 = calculate_length(mep_1)
length_2 = calculate_length(mep_2)
length_3 = calculate_length(mep_3)
length_4 = calculate_length(mep_4)

# define the sphere radius
ra = (length_1 + length_2 + length_3 + length_4) / 4 / 4

# mep_1
unique_indices = set()
x_1 = []
y_1 = []
z_1 = []
for mep_points in mep_1:
    print("mep1: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        x_1.append(i)
                        y_1.append(j)
                        z_1.append(k)

# mep_2
unique_indices = set()
x_2 = []
y_2 = []
z_2 = []
for mep_points in mep_2:
    print("mep2: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        x_2.append(i)
                        y_2.append(j)
                        z_2.append(k)

# mep_3
unique_indices = set()
x_3 = []
y_3 = []
z_3 = []
for mep_points in mep_3:
    print("mep3: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        x_3.append(i)
                        y_3.append(j)
                        z_3.append(k)

# mep_4
unique_indices = set()
x_4 = []
y_4 = []
z_4 = []
for mep_points in mep_4:
    print("mep4: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        x_4.append(i)
                        y_4.append(j)
                        z_4.append(k)

# Create mesh grids for coordinates
result_1 = np.column_stack((x_1, y_1, z_1))
result_2 = np.column_stack((x_2, y_2, z_2))
result_3 = np.column_stack((x_3, y_3, z_3))
result_4 = np.column_stack((x_4, y_4, z_4))

# Get alpha shape boundary points for each result
alpha_shape_1 = get_alpha_shape(result_1, alpha=0.8)
alpha_shape_2 = get_alpha_shape(result_2, alpha=0.8)
alpha_shape_3 = get_alpha_shape(result_3, alpha=0.8)
alpha_shape_4 = get_alpha_shape(result_4, alpha=0.8)

# Plot the alpha shape boundary points
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# increase the font size
plt.rcParams.update({'font.size': 18})

plt.imshow(fes_2d, cmap="viridis", extent=(0.0, 64.0, 64.0, 0.0))
plt.plot(mep_1[:, 1], mep_1[:, 0], "ro-")
plt.plot(mep_2[:, 1], mep_2[:, 0], "bo-")
plt.plot(mep_3[:, 1], mep_3[:, 0], "go-")
plt.plot(mep_4[:, 1], mep_4[:, 0], "yo-")
plt.xlabel("c", fontsize=28)
plt.ylabel("a", fontsize=28)
plt.colorbar()

# Plot the closed alpha shape boundary
ax.plot(np.append(alpha_shape_1[:, 1], alpha_shape_1[0, 1]),
        np.append(alpha_shape_1[:, 0], alpha_shape_1[0, 0]), c='r')
ax.plot(np.append(alpha_shape_2[:, 1], alpha_shape_2[0, 1]),
        np.append(alpha_shape_2[:, 0], alpha_shape_2[0, 0]), c='b')
ax.plot(np.append(alpha_shape_3[:, 1], alpha_shape_3[0, 1]),
        np.append(alpha_shape_3[:, 0], alpha_shape_3[0, 0]), c='g')
ax.plot(np.append(alpha_shape_4[:, 1], alpha_shape_4[0, 1]),
        np.append(alpha_shape_4[:, 0], alpha_shape_4[0, 0]), c='y')

# show a 64*64 grid lines
ax.set_xticks(np.linspace(0, 64, 6))
ax.set_yticks(np.linspace(0, 64, 6))
ax.grid(True)

# set the ticks font size
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Create tick labels, excluding 0
xtick_labels = [f'{x:.1f}' if x != 0 and x != 1 else '' for x in np.linspace(0, 1, 6)]
ytick_labels = [f'{y:.1f}' if y != 0 and y != 1 else '' for y in np.linspace(1, 0, 6)]

# Change the tick labels to 0-1 range, excluding 0
ax.set_xticklabels(xtick_labels)
ax.set_yticklabels(ytick_labels)

plt.savefig("Figure S1b.tif", dpi=300)
plt.show()
