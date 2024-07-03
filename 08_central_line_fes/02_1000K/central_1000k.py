from xdatbus import neb_2d, local_minima
import numpy as np
import matplotlib.pyplot as plt


fes = np.load("y_fes_1000k.npy")

# remove the middle 13 columns of 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=1)
fes = np.delete(fes, [0, 1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63], axis=0)

mid_1_700k = fes[26, :] - np.min(fes[26, :])
mid_2_700k = fes[:, 26] - np.min(fes[:, 26])

np.save("mid_fes_1_1000k.npy", mid_1_700k)
np.save("mid_fes_2_1000k.npy", mid_2_700k)
