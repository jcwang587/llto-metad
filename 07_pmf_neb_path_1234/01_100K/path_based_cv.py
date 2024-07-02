import numpy as np
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess

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

# define the sphere radius
ra = 6

# mep_1
unique_indices = set()
fes_1 = []
x_1 = []
y_1 = []
z_1 = []
for mep_points in mep_1:
    print("mep1: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (j - 31) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        fes_1.append(fes[i, j, k])
                        x_1.append(i)
                        y_1.append(j)
                        z_1.append(k)

# mep_2
unique_indices = set()
fes_2 = []
x_2 = []
y_2 = []
z_2 = []
for mep_points in mep_2:
    print("mep2: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (j - 31) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        fes_2.append(fes[i, j, k])
                        x_2.append(i)
                        y_2.append(j)
                        z_2.append(k)

# mep_3
unique_indices = set()
fes_3 = []
x_3 = []
y_3 = []
z_3 = []
for mep_points in mep_3:
    print("mep3: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (j - 31) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        fes_3.append(fes[i, j, k])
                        x_3.append(i)
                        y_3.append(j)
                        z_3.append(k)

# mep_4
unique_indices = set()
fes_4 = []
x_4 = []
y_4 = []
z_4 = []
for mep_points in mep_4:
    print("mep4: ", mep_points)
    for i in range(fes_size[0]):
        for j in range(fes_size[1]):
            for k in range(fes_size[2]):
                if (i - mep_points[0]) ** 2 + (j - 31) ** 2 + (k - mep_points[1]) ** 2 <= ra ** 2:
                    index_tuple = (i, j, k)
                    if index_tuple not in unique_indices:
                        unique_indices.add(index_tuple)
                        fes_4.append(fes[i, j, k])
                        x_4.append(i)
                        y_4.append(j)
                        z_4.append(k)

# Create mesh grids for coordinates
H_1 = np.exp(-np.array(fes_1) / (kb * t))
result_1 = np.column_stack((x_1, y_1, z_1, fes_1, H_1))

H_2 = np.exp(-np.array(fes_2) / (kb * t))
result_2 = np.column_stack((x_2, y_2, z_2, fes_2, H_2))

H_3 = np.exp(-np.array(fes_3) / (kb * t))
result_3 = np.column_stack((x_3, y_3, z_3, fes_3, H_3))

H_4 = np.exp(-np.array(fes_4) / (kb * t))
result_4 = np.column_stack((x_4, y_4, z_4, fes_4, H_4))


arc_points_1 = mep_1
arc_points_2 = mep_2
arc_points_3 = mep_3
arc_points_4 = mep_4

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
fig.add_trace(go.Scatter3d(x=arc_points_1[:, 0], y=np.ones(100) * 31, z=arc_points_1[:, 1], mode='markers',
                           marker=dict(size=5, color='red'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_2[:, 0], y=np.ones(100) * 31, z=arc_points_2[:, 1], mode='markers',
                           marker=dict(size=5, color='blue'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_3[:, 0], y=np.ones(100) * 31, z=arc_points_3[:, 1], mode='markers',
                           marker=dict(size=5, color='green'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_4[:, 0], y=np.ones(100) * 31, z=arc_points_4[:, 1], mode='markers',
                           marker=dict(size=5, color='yellow'), name='arc_points'))

# Setting labels
fig.update_layout(scene=dict(
    xaxis_title='a',
    yaxis_title='b',
    zaxis_title='c'),
    margin=dict(l=0, r=0, b=0, t=0))

# Show the plot
fig.write_html('3d_plot.html')

# project the data onto the arc
M = len(result_1)
N = len(arc_points_1)
bins_num = 46
s_1 = []
c = 1.0
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc1: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            - c * (result_1[i][0] - arc_points_1[j, 0]) ** 2
            - c * (result_1[i][1] - 31) ** 2
            - c * (result_1[i][2] - arc_points_1[j, 1]) ** 2)
        s_b += np.exp(
            - c * (result_1[i][0] - arc_points_1[j, 0]) ** 2
            - c * (result_1[i][1] - 31) ** 2
            - c * (result_1[i][2] - arc_points_1[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_1.append(s_i)

result_1 = np.column_stack((result_1, s_1))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_1 = np.linspace(min(s_1), max(s_1), bins_num)
H_bins_1 = np.zeros(bins_num - 1)
for i in range(bins_num - 1):
    for j in range(M):
        if s_bins_1[i] <= s_1[j] < s_bins_1[i + 1]:
            H_bins_1[i] += result_1[j][4]

# convert H to free energy
fes_bins_1 = -kb * t * np.log(H_bins_1)
fes_bins_1 -= min(fes_bins_1)
fes_smooth_1 = lowess(fes_bins_1, s_bins_1[:-1], frac=0.2, return_sorted=False)

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
color = '#F47A00'
ax1.set_xlabel(r'$\xi$', fontsize=20, weight='bold', labelpad=10)
ax1.set_ylabel('Histogram', color=color, fontsize=20, weight='bold', labelpad=10)
ax1.plot(s_bins_1[:-1], H_bins_1, color=color, lw=2)
ax1.tick_params(axis='y', labelcolor=color, labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(False)
ax1.grid(True, which='major', axis='x')

# Create a second y-axis for the free energy
ax2 = ax1.twinx()
color = '#193E8F'
ax2.set_ylabel('Free Energy (eV)', color=color, fontsize=20, weight='bold', labelpad=10)
ax2.plot(s_bins_1[:-1], fes_bins_1, color='#B8B8B8', lw=2)
ax2.tick_params(axis='y', labelcolor=color, labelsize=16)
ax2.plot(s_bins_1[:-1], fes_smooth_1, color=color, lw=2)

plt.tight_layout()
plt.savefig('path_based_cv_1.png', dpi=300)
plt.show()

M = len(result_2)
N = len(arc_points_2)
s_2 = []
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc2: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            - c * (result_2[i][0] - arc_points_2[j, 0]) ** 2
            - c * (result_2[i][1] - 31) ** 2
            - c * (result_2[i][2] - arc_points_2[j, 1]) ** 2)
        s_b += np.exp(
            - c * (result_2[i][0] - arc_points_2[j, 0]) ** 2
            - c * (result_2[i][1] - 31) ** 2
            - c * (result_2[i][2] - arc_points_2[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_2.append(s_i)

result_2 = np.column_stack((result_2, s_2))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_2 = np.linspace(min(s_2), max(s_2), bins_num)
H_bins_2 = np.zeros(bins_num - 1)
for i in range(bins_num - 1):
    for j in range(M):
        if s_bins_2[i] <= s_2[j] < s_bins_2[i + 1]:
            H_bins_2[i] += result_2[j][4]

# convert H to free energy
fes_bins_2 = -kb * t * np.log(H_bins_2)
fes_bins_2 -= min(fes_bins_2)
fes_smooth_2 = lowess(fes_bins_2, s_bins_2[:-1], frac=0.2, return_sorted=False)

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
color = '#F47A00'
ax1.set_xlabel(r'$\xi$', fontsize=20, weight='bold', labelpad=10)
ax1.set_ylabel('Histogram', color=color, fontsize=20, weight='bold', labelpad=10)
ax1.plot(s_bins_2[:-1], H_bins_2, color=color, lw=2)
ax1.tick_params(axis='y', labelcolor=color, labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(False)
ax1.grid(True, which='major', axis='x')

# Create a second y-axis for the free energy
ax2 = ax1.twinx()
color = '#193E8F'
ax2.set_ylabel('Free Energy (eV)', color=color, fontsize=20, weight='bold', labelpad=10)
ax2.plot(s_bins_2[:-1], fes_bins_2, color='#B8B8B8', lw=2)
ax2.plot(s_bins_2[:-1], fes_smooth_2, color=color, lw=2)
ax2.tick_params(axis='y', labelcolor=color, labelsize=16)

plt.tight_layout()
plt.savefig('path_based_cv_2.png', dpi=300)
plt.show()

M = len(result_3)
N = len(arc_points_3)
s_3 = []
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc3: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            - c * (result_3[i][0] - arc_points_3[j, 0]) ** 2
            - c * (result_3[i][1] - 31) ** 2
            - c * (result_3[i][2] - arc_points_3[j, 1]) ** 2)
        s_b += np.exp(
            - c * (result_3[i][0] - arc_points_3[j, 0]) ** 2
            - c * (result_3[i][1] - 31) ** 2
            - c * (result_3[i][2] - arc_points_3[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_3.append(s_i)

result_3 = np.column_stack((result_3, s_3))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_3 = np.linspace(min(s_3), max(s_3), bins_num)
H_bins_3 = np.zeros(bins_num - 1)
for i in range(bins_num - 1):
    for j in range(M):
        if s_bins_3[i] <= s_3[j] < s_bins_3[i + 1]:
            H_bins_3[i] += result_3[j][4]

# convert H to free energy
fes_bins_3 = -kb * t * np.log(H_bins_3)
fes_bins_3 -= min(fes_bins_3)
fes_smooth_3 = lowess(fes_bins_3, s_bins_3[:-1], frac=0.2, return_sorted=False)

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
color = '#F47A00'
ax1.set_xlabel(r'$\xi$', fontsize=20, weight='bold', labelpad=10)
ax1.set_ylabel('Histogram', color=color, fontsize=20, weight='bold', labelpad=10)
ax1.plot(s_bins_3[:-1], H_bins_3, color=color, lw=2)
ax1.tick_params(axis='y', labelcolor=color, labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(False)
ax1.grid(True, which='major', axis='x')

# Create a second y-axis for the free energy
ax2 = ax1.twinx()
color = '#193E8F'
ax2.set_ylabel('Free Energy (eV)', color=color, fontsize=20, weight='bold', labelpad=10)
ax2.plot(s_bins_3[:-1], fes_bins_3, color='#B8B8B8', lw=2)
ax2.plot(s_bins_3[:-1], fes_smooth_3, color=color, lw=2)
ax2.tick_params(axis='y', labelcolor=color, labelsize=16)

plt.tight_layout()
plt.savefig('path_based_cv_3.png', dpi=300)
plt.show()

M = len(result_4)
N = len(arc_points_4)
s_4 = []
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc4: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            - c * (result_4[i][0] - arc_points_4[j, 0]) ** 2
            - c * (result_4[i][1] - 31) ** 2
            - c * (result_4[i][2] - arc_points_4[j, 1]) ** 2)
        s_b += np.exp(
            - c * (result_4[i][0] - arc_points_4[j, 0]) ** 2
            - c * (result_4[i][1] - 31) ** 2
            - c * (result_4[i][2] - arc_points_4[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_4.append(s_i)

result_4 = np.column_stack((result_4, s_4))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_4 = np.linspace(min(s_4), max(s_4), bins_num)
H_bins_4 = np.zeros(bins_num - 1)
for i in range(bins_num - 1):
    for j in range(M):
        if s_bins_4[i] <= s_4[j] < s_bins_4[i + 1]:
            H_bins_4[i] += result_4[j][4]

# convert H to free energy
fes_bins_4 = -kb * t * np.log(H_bins_4)
fes_bins_4 -= min(fes_bins_4)
fes_smooth_4 = lowess(fes_bins_4, s_bins_4[:-1], frac=0.2, return_sorted=False)

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
color = '#F47A00'
ax1.set_xlabel(r'$\xi$', fontsize=20, weight='bold', labelpad=10)
ax1.set_ylabel('Histogram', color=color, fontsize=20, weight='bold', labelpad=10)
ax1.plot(s_bins_4[:-1], H_bins_4, color=color, lw=2)
ax1.tick_params(axis='y', labelcolor=color, labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(False)
ax1.grid(True, which='major', axis='x')

# Create a second y-axis for the free energy
ax2 = ax1.twinx()
color = '#193E8F'
ax2.set_ylabel('Free Energy (eV)', color=color, fontsize=20, weight='bold', labelpad=10)
ax2.plot(s_bins_4[:-1], fes_bins_4, color='#B8B8B8', lw=2)
ax2.plot(s_bins_4[:-1], fes_smooth_4, color=color, lw=2)
ax2.tick_params(axis='y', labelcolor=color, labelsize=16)

plt.tight_layout()
plt.savefig('path_based_cv_4.png', dpi=300)
plt.show()

# export the fes_smooth_1, fes_smooth_2, fes_smooth_3, fes_smooth_4 to a npy file
np.save('../combine_plot/100k_fes_smooth_1.npy', fes_smooth_1[1:])
np.save('../combine_plot/100k_fes_smooth_2.npy', fes_smooth_2[1:])
np.save('../combine_plot/100k_fes_smooth_3.npy', fes_smooth_3[1:])
np.save('../combine_plot/100k_fes_smooth_4.npy', fes_smooth_4[1:])
# export the s_bins_1, s_bins_2, s_bins_3, s_bins_4 to a npy file
np.save('../combine_plot/100k_s_bins_1.npy', s_bins_1[1:-1])
np.save('../combine_plot/100k_s_bins_2.npy', s_bins_2[1:-1])
np.save('../combine_plot/100k_s_bins_3.npy', s_bins_3[1:-1])
np.save('../combine_plot/100k_s_bins_4.npy', s_bins_4[1:-1])
