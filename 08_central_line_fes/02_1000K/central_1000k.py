from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt


fes = np.load("y_fes_1000k.npy")
fes_3d = np.load("fes_data_3d.npy")

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=1)
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=0)

# remove the middle in 3 dimensions
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=1)
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=0)
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=2)

mid_1_1000k = fes[26, :] - np.min(fes[26, :])
mid_2_1000k = fes[:, 26] - np.min(fes[:, 26])

min_y_1000k = []
for i in range(len(mid_1_1000k)):
    # find the minimum value of the 3D FES
    min_y_1000k.append(np.min(fes_3d[:, i, :]))

np.save("mid_fes_1_1000k.npy", mid_1_1000k)
np.save("mid_fes_2_1000k.npy", mid_2_1000k)
np.save("min_y_1000k.npy", min_y_1000k)
