import numpy as np
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess

# define the constants
kb = 8.617333262145e-5
t = 300

# load npy file
fes = np.load('fes_data_3d.npy')
x = np.load('x_data_1d.npy')
y = np.load('y_data_1d.npy')
z = np.load('z_data_1d.npy')
fes_size = fes.shape

# split into 4 part with 1: first half of x, first half of z, 2: first half of x, second half of z, 3: second half of
# x, first half of z, 4: second half of x, second half of z
fes_1 = fes[0:fes_size[0] // 2, :, 0:fes_size[2] // 2]
fes_2 = fes[0:fes_size[0] // 2, :, fes_size[2] // 2:]
fes_3 = fes[fes_size[0] // 2:, :, 0:fes_size[2] // 2]
fes_4 = fes[fes_size[0] // 2:, :, fes_size[2] // 2:]

# Calculate indices for each section
x_half = len(x) // 2
z_half = len(z) // 2

# Part 1: First half of x, all y, first half of z
x_part_1 = x[:x_half]
x_part_2 = x[x_half:]
z_part_1 = z[:z_half]
z_part_2 = z[z_half:]

# Create mesh grids for coordinates
X1, Y, Z1 = np.meshgrid(x_part_1, y, z_part_1, indexing='ij')
X1_flat = X1.flatten()
Y_flat = Y.flatten()
Z1_flat = Z1.flatten()
fes_1_flat = fes_1.flatten()
H_1 = np.exp(-fes_1_flat / (kb * t))
result_1 = np.column_stack((X1_flat, Y_flat, Z1_flat, fes_1_flat, H_1))

X1, Y, Z2 = np.meshgrid(x_part_1, y, z_part_2, indexing='ij')
X1_flat = X1.flatten()
Y_flat = Y.flatten()
Z2_flat = Z2.flatten()
fes_2_flat = fes_2.flatten()
H_2 = np.exp(-fes_2_flat / (kb * t))
result_2 = np.column_stack((X1_flat, Y_flat, Z2_flat, fes_2_flat, H_2))

X2, Y, Z1 = np.meshgrid(x_part_2, y, z_part_1, indexing='ij')
X2_flat = X2.flatten()
Y_flat = Y.flatten()
Z1_flat = Z1.flatten()
fes_3_flat = fes_3.flatten()
H_3 = np.exp(-fes_3_flat / (kb * t))
result_3 = np.column_stack((X2_flat, Y_flat, Z1_flat, fes_3_flat, H_3))

X2, Y, Z2 = np.meshgrid(x_part_2, y, z_part_2, indexing='ij')
X2_flat = X2.flatten()
Y_flat = Y.flatten()
Z2_flat = Z2.flatten()
fes_4_flat = fes_4.flatten()
H_4 = np.exp(-fes_4_flat / (kb * t))
result_4 = np.column_stack((X2_flat, Y_flat, Z2_flat, fes_4_flat, H_4))

x_mid = (x[0] + x[-1]) / 2
z_mid = (z[0] + z[-1]) / 2
x_center = x[0]
z_center = z[0]
radius = x_mid - x[0]
theta = np.linspace(0, np.pi / 2, 100)
arc_x = x_center + radius * np.cos(theta)
arc_z = z_center + radius * np.sin(theta)
arc_points_1 = np.column_stack((arc_x, arc_z))
arc_points_2 = np.column_stack((arc_x, 4 - arc_z))
arc_points_3 = np.column_stack((4 - arc_x, arc_z))
arc_points_4 = np.column_stack((4 - arc_x, 4 - arc_z))

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
fig.add_trace(go.Scatter3d(x=arc_points_1[:, 0], y=np.ones(100) * 2, z=arc_points_1[:, 1], mode='markers',
                           marker=dict(size=5, color='red'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_2[:, 0], y=np.ones(100) * 2, z=arc_points_2[:, 1], mode='markers',
                           marker=dict(size=5, color='blue'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_3[:, 0], y=np.ones(100) * 2, z=arc_points_3[:, 1], mode='markers',
                           marker=dict(size=5, color='green'), name='arc_points'))
fig.add_trace(go.Scatter3d(x=arc_points_4[:, 0], y=np.ones(100) * 2, z=arc_points_4[:, 1], mode='markers',
                           marker=dict(size=5, color='yellow'), name='arc_points'))

# Setting labels
fig.update_layout(scene=dict(
    xaxis_title='a',
    yaxis_title='b',
    zaxis_title='c'),
    margin=dict(l=0, r=0, b=0, t=0))

# Show the plot
fig.write_html('3d_plot.html')

# project the HILLS_700K data onto the arc
M = len(result_1)
N = len(arc_points_1)

s_1 = []
c = 1.0
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc1: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            -c * (result_1[i][0] - arc_points_1[j, 0]) ** 2 - c * (result_1[i][2] - arc_points_1[j, 1]) ** 2)
        s_b += np.exp(-c * (result_1[i][0] - arc_points_1[j, 0]) ** 2 - c * (result_1[i][2] - arc_points_1[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_1.append(s_i)

result_1 = np.column_stack((result_1, s_1))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_1 = np.linspace(min(s_1), max(s_1), 101)
H_bins_1 = np.zeros(100)
for i in range(100):
    for j in range(M):
        if s_bins_1[i] <= s_1[j] < s_bins_1[i + 1]:
            H_bins_1[i] += result_1[j][4]

# convert H to free energy
fes_bins_1 = -kb * t * np.log(H_bins_1)
fes_bins_1 -= min(fes_bins_1)
fes_smooth_1 = lowess(fes_bins_1, s_bins_1[:-1], frac=0.1, return_sorted=False)

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


s_2 = []
c = 1.0
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc2: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            -c * (result_2[i][0] - arc_points_2[j, 0]) ** 2 - c * (result_2[i][2] - arc_points_2[j, 1]) ** 2)
        s_b += np.exp(-c * (result_2[i][0] - arc_points_2[j, 0]) ** 2 - c * (result_2[i][2] - arc_points_2[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_2.append(s_i)

result_2 = np.column_stack((result_2, s_2))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_2 = np.linspace(min(s_2), max(s_2), 101)
H_bins_2 = np.zeros(100)
for i in range(100):
    for j in range(M):
        if s_bins_2[i] <= s_2[j] < s_bins_2[i + 1]:
            H_bins_2[i] += result_2[j][4]

# convert H to free energy
fes_bins_2 = -kb * t * np.log(H_bins_2)
fes_bins_2 -= min(fes_bins_2)
fes_smooth_2 = lowess(fes_bins_2, s_bins_2[:-1], frac=0.1, return_sorted=False)

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


s_3 = []
c = 1.0
for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc3: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            -c * (result_3[i][0] - arc_points_3[j, 0]) ** 2 - c * (result_3[i][2] - arc_points_3[j, 1]) ** 2)
        s_b += np.exp(-c * (result_3[i][0] - arc_points_3[j, 0]) ** 2 - c * (result_3[i][2] - arc_points_3[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_3.append(s_i)

result_3 = np.column_stack((result_3, s_3))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_3 = np.linspace(min(s_3), max(s_3), 101)
H_bins_3 = np.zeros(100)
for i in range(100):
    for j in range(M):
        if s_bins_3[i] <= s_3[j] < s_bins_3[i + 1]:
            H_bins_3[i] += result_3[j][4]

# convert H to free energy
fes_bins_3 = -kb * t * np.log(H_bins_3)
fes_bins_3 -= min(fes_bins_3)
fes_smooth_3 = lowess(fes_bins_3, s_bins_3[:-1], frac=0.1, return_sorted=False)

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


s_4 = []
c = 1.0

for i in range(M):
    s_a = 0.0
    s_b = 0.0
    print("arc4: ", i)
    for j in range(N):
        s_a += (j - 1) * np.exp(
            -c * (result_4[i][0] - arc_points_4[j, 0]) ** 2 - c * (result_4[i][2] - arc_points_4[j, 1]) ** 2)
        s_b += np.exp(-c * (result_4[i][0] - arc_points_4[j, 0]) ** 2 - c * (result_4[i][2] - arc_points_4[j, 1]) ** 2)
    s_i = 1 / (N - 1) * s_a / s_b
    s_4.append(s_i)

result_4 = np.column_stack((result_4, s_4))

# generate the 100 bins for s and if s falls into the bin, add the H value to the same bin
s_bins_4 = np.linspace(min(s_4), max(s_4), 101)
H_bins_4 = np.zeros(100)
for i in range(100):
    for j in range(M):
        if s_bins_4[i] <= s_4[j] < s_bins_4[i + 1]:
            H_bins_4[i] += result_4[j][4]

# convert H to free energy
fes_bins_4 = -kb * t * np.log(H_bins_4)
fes_bins_4 -= min(fes_bins_4)
fes_smooth_4 = lowess(fes_bins_4, s_bins_4[:-1], frac=0.1, return_sorted=False)

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
np.save('../combine_plot/300k_fes_smooth_1.npy', fes_smooth_1)
np.save('../combine_plot/300k_fes_smooth_2.npy', fes_smooth_2)
np.save('../combine_plot/300k_fes_smooth_3.npy', fes_smooth_3)
np.save('../combine_plot/300k_fes_smooth_4.npy', fes_smooth_4)
# export the s_bins_1, s_bins_2, s_bins_3, s_bins_4 to a npy file
np.save('../combine_plot/300k_s_bins_1.npy', s_bins_1[:-1])
np.save('../combine_plot/300k_s_bins_2.npy', s_bins_2[:-1])
np.save('../combine_plot/300k_s_bins_3.npy', s_bins_3[:-1])
np.save('../combine_plot/300k_s_bins_4.npy', s_bins_4[:-1])
