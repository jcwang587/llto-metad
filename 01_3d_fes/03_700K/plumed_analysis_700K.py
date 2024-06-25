import xdatbus as xdb
import shutil


def remove_lines(filename, num_lines):
    with open(filename, 'r') as file:
        # Skip the first num_lines
        for _ in range(num_lines):
            file.readline()

        # Read the rest of the file
        remaining_content = file.read()

    with open(filename, 'w') as file:
        file.write(remaining_content)


aimd_path = 'B:/projects/cc1_3d_metad/04_700K'

# copy to the local folder
shutil.copy(aimd_path + '/HILLSPOT', './HILLSPOT')

remove_lines('HILLSPOT', 488)

hillspot_path = 'HILLSPOT'
hills_path = 'HILLS_700K'
xdb.hillspot2hills(hillspot_path, hills_path, ['x', 'y', 'z'],
                   height_conversion=1, sigma_conversion=1, del_inter=False)

# read HILLSPOT into a pandas dataframe
import numpy as np

hills = np.loadtxt('HILLS_700K', skiprows=1)

# 3d scatter plot with data column 1, 2, 3 as x, y, z
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(hills[:, 1], hills[:, 2], hills[:, 3], c=hills[:, 3], marker='o')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# view on the x-y plane
# ax.view_init(90, 0)

plt.show()
