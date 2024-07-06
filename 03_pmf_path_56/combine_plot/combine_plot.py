from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Load the data
a_700k = np.load('700k_a.npy')
c_700k = np.load('700k_c.npy')
a_1000k = np.load('1000k_a.npy')
c_1000k = np.load('1000k_c.npy')

fes_a_700k = np.load('700k_a_fes.npy')
fes_a_700k = fes_a_700k - np.min(fes_a_700k)
fes_c_700k = np.load('700k_c_fes.npy')
fes_c_700k = fes_c_700k - np.min(fes_c_700k)
fes_a_1000k = np.load('1000k_a_fes.npy')
fes_a_1000k = fes_a_1000k - np.min(fes_a_1000k)
fes_c_1000k = np.load('1000k_c_fes.npy')
fes_c_1000k = fes_c_1000k - np.min(fes_c_1000k)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
ax1.set_xlabel(r'$\xi_2$', fontsize=20, labelpad=10)
ax1.set_ylabel('Potential of Mean Force (eV)', fontsize=20, labelpad=10)

ax1.plot(a_1000k, fes_a_1000k, color='#1a80bb', lw=5)
ax1.plot(c_1000k, fes_c_1000k, color='#ea801c', lw=2)
ax1.plot(a_700k, fes_a_700k, color='#1a80bb', lw=2, ls='--')
ax1.plot(c_700k, fes_c_700k, color='#ea801c', lw=5, ls='--', dashes=(1.6, 0.55))
ax1.plot(a_1000k, fes_a_1000k, color='#1a80bb', lw=9, alpha=0.3)
ax1.plot(c_700k, fes_c_700k, color='#ea801c', lw=9, alpha=0.3)
ax1.tick_params(axis='y', labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(True, which='major', axis='x', linestyle='--')
ax1.grid(True, which='major', axis='y', linestyle='--')

# set x range
ax1.set_xlim(0, 1)

# set y range
ax1.set_ylim(0, 0.22)


def remove_zero_tick_label(x, pos):
    return "" if x == 0 else f"{x:.2f}"


ax1.yaxis.set_major_formatter(FuncFormatter(remove_zero_tick_label))

# set x major 0.2 and minor ticks 0.1
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
ax1.yaxis.set_major_locator(MultipleLocator(0.05))
ax1.yaxis.set_minor_locator(MultipleLocator(0.01))

# set legend in two columns
ax1.legend(['1000K Path-5', '1000K Path-6', '700K Path-5', '700K Path-6'],
           fontsize=16, loc='upper center', ncol=2)

plt.tight_layout()
plt.savefig('combine_plot_700k_1000k.tif', dpi=300)
plt.show()
