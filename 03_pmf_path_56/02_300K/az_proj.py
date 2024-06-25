import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# define the constants
kb = 8.617333262145e-5
t = 300
beta = 1 / (kb * t)

# load npy file
fes = np.load('fes_data_3d.npy')
x = np.load('x_data_1d.npy')
y = np.load('y_data_1d.npy')
z = np.load('z_data_1d.npy')
fes_size = fes.shape

# define the grid size
dx = (max(x) - min(x)) / (len(x) - 1)
dy = (max(y) - min(y)) / (len(y) - 1)
dz = (max(z) - min(z)) / (len(z) - 1)

# Calculate F(z) by looping through z
fes_z = np.zeros(len(z))

for idx_z in range(len(z)):
    sum_exp = 0
    for idx_x in range(len(x)-1):
        for idx_y in range(len(y)-1):
            exp_i_j = np.exp(-beta * fes[idx_x, idx_y, idx_z])
            exp_i1_j = np.exp(-beta * fes[idx_x+1, idx_y, idx_z])
            exp_i_j1 = np.exp(-beta * fes[idx_x, idx_y+1, idx_z])
            exp_i1_j1 = np.exp(-beta * fes[idx_x+1, idx_y+1, idx_z])
            sum_exp += (exp_i_j + exp_i1_j + exp_i_j1 + exp_i1_j1) / 4
    fes_z[idx_z] = -kb * t * np.log(sum_exp * dx * dy)

fes_z = fes_z - min(fes_z)
z_norm = (z - min(z)) / (max(z) - min(z))

data = pd.DataFrame({'Relative Coordinate (c)': z_norm, 'Free Energy (eV)': fes_z})

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Relative Coordinate (c)', y='Free Energy (eV)', color='#193E8F', lw=3)

plt.xlabel('Relative Coordinate (c)', fontsize=20, weight='bold', labelpad=10)
plt.ylabel('Free Energy (eV)', fontsize=20, weight='bold', labelpad=10)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.xlim(data['Relative Coordinate (c)'].min(), data['Relative Coordinate (c)'].max())
plt.ylim(data['Free Energy (eV)'].min(), data['Free Energy (eV)'].max())

plt.tight_layout()
plt.savefig('fes_c.png', format='png', dpi=300, bbox_inches='tight')

plt.show()


# Calculate F(x) by looping through x
fes_x = np.zeros(len(x))

for idx_x in range(len(x)):
    sum_exp = 0
    for idx_y in range(len(y)-1):
        for idx_z in range(len(z)-1):
            exp_i_j = np.exp(-beta * fes[idx_x, idx_y, idx_z])
            exp_i1_j = np.exp(-beta * fes[idx_x, idx_y, idx_z+1])
            exp_i_j1 = np.exp(-beta * fes[idx_x, idx_y+1, idx_z])
            exp_i1_j1 = np.exp(-beta * fes[idx_x, idx_y+1, idx_z+1])
            sum_exp += (exp_i_j + exp_i1_j + exp_i_j1 + exp_i1_j1) / 4
    fes_x[idx_x] = -kb * t * np.log(sum_exp * dy * dz)

fes_x = fes_x - min(fes_x)
x_norm = (x - min(x)) / (max(x) - min(x))

data = pd.DataFrame({'Relative Coordinate (a)': x_norm, 'Free Energy (eV)': fes_x})

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_context('paper')

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Relative Coordinate (a)', y='Free Energy (eV)', color='#193E8F', lw=3)

plt.xlabel('Relative Coordinate (a)', fontsize=20, weight='bold', labelpad=10)
plt.ylabel('Free Energy (eV)', fontsize=20, weight='bold', labelpad=10)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.xlim(data['Relative Coordinate (a)'].min(), data['Relative Coordinate (a)'].max())
plt.ylim(data['Free Energy (eV)'].min(), data['Free Energy (eV)'].max())

plt.tight_layout()
plt.savefig('fes_a.png', format='png', dpi=300, bbox_inches='tight')

plt.show()
