from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt


fes = np.load("y_fes_700k.npy")
fes_3d = np.load("fes_data_3d.npy")

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=1)
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=0)

# remove the middle in 3 dimensions
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=1)
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=0)
fes_3d = np.delete(fes_3d, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=2)

mid_1_700k = fes[26, :] - np.min(fes[26, :])
mid_2_700k = fes[:, 26] - np.min(fes[:, 26])

min_y_700k = []
for i in range(len(mid_1_700k)):
    # find the minimum value of the 3D FES
    min_y_700k.append(np.min(fes_3d[:, i, :]))

np.save("mid_fes_1_700k.npy", mid_1_700k)
np.save("mid_fes_2_700k.npy", mid_2_700k)
np.save("min_y_700k.npy", min_y_700k)