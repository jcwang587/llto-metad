import numpy as np
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess


def calculate_length(mep):
    diff = np.diff(mep, axis=0)
    segment_lengths = np.sqrt(np.sum(diff ** 2, axis=1))
    return np.sum(segment_lengths)


# define the constants
kb = 8.617333262145e-5
t = 100

# load npy file
fes = np.load('fes_data_3d.npy')
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

# Create a Plotly figure
fig = go.Figure()

# Adding scatter plots
fig.add_trace(go.Scatter3d(x=result_1[:, 0], y=result_1[:, 1], z=result_1[:, 2], mode='markers',
                           marker=dict(size=0.5, color='red'), name='result_1'))
fig.add_trace(go.Scatter3d(x=result_2[:, 0], y=result_2[:, 1], z=result_2[:, 2], mode='markers',
                           marker=dict(size=0.5, color='blue'), name='result_2'))
fig.add_trace(go.Scatter3d(x=result_3[:, 0], y=result_3[:, 1], z=result_3[:, 2], mode='markers',
                           marker=dict(size=0.5, color='green'), name='result_3'))
fig.add_trace(go.Scatter3d(x=result_4[:, 0], y=result_4[:, 1], z=result_4[:, 2], mode='markers',
                           marker=dict(size=0.5, color='yellow'), name='result_4'))

# Setting labels
fig.update_layout(scene=dict(
    xaxis_title='a',
    yaxis_title='b',
    zaxis_title='c'),
    margin=dict(l=0, r=0, b=0, t=0))

# Show the plot
fig.write_html('3d_plot_mep_100k.html')


