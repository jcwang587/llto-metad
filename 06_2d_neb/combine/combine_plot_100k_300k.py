from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter


# Load the data
fes_smooth_1_100k = np.load('../01_100k/mep_fes_13_100k.npy')
fes_smooth_1_100k = fes_smooth_1_100k - np.min(fes_smooth_1_100k)
fes_smooth_2_100k = np.load('../01_100k/mep_fes_32_100k.npy')
fes_smooth_2_100k = fes_smooth_2_100k - np.min(fes_smooth_2_100k)
fes_smooth_3_100k = np.load('../01_100k/mep_fes_01_100k.npy')
fes_smooth_3_100k = fes_smooth_3_100k - np.min(fes_smooth_3_100k)
fes_smooth_4_100k = np.load('../01_100k/mep_fes_20_100k.npy')
fes_smooth_4_100k = fes_smooth_4_100k - np.min(fes_smooth_4_100k)
fes_smooth_1_300k = np.load('../02_300k/mep_fes_13_300k.npy')
fes_smooth_1_300k = fes_smooth_1_300k - np.min(fes_smooth_1_300k)
fes_smooth_2_300k = np.load('../02_300k/mep_fes_32_300k.npy')
fes_smooth_2_300k = fes_smooth_2_300k - np.min(fes_smooth_2_300k)
fes_smooth_3_300k = np.load('../02_300k/mep_fes_01_300k.npy')
fes_smooth_3_300k = fes_smooth_3_300k - np.min(fes_smooth_3_300k)
fes_smooth_4_300k = np.load('../02_300k/mep_fes_20_300k.npy')
fes_smooth_4_300k = fes_smooth_4_300k - np.min(fes_smooth_4_300k)

# get s_bins from the length of fes_smooth
s_bins_1_100k = np.linspace(0, 1, len(fes_smooth_1_100k))
s_bins_2_100k = np.linspace(0, 1, len(fes_smooth_2_100k))
s_bins_3_100k = np.linspace(0, 1, len(fes_smooth_3_100k))
s_bins_4_100k = np.linspace(0, 1, len(fes_smooth_4_100k))
s_bins_1_300k = np.linspace(0, 1, len(fes_smooth_1_300k))
s_bins_2_300k = np.linspace(0, 1, len(fes_smooth_2_300k))
s_bins_3_300k = np.linspace(0, 1, len(fes_smooth_3_300k))
s_bins_4_300k = np.linspace(0, 1, len(fes_smooth_4_300k))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot H_bins as a histogram
ax1.set_xlabel(r'$\xi_1$', fontsize=20, labelpad=10)
ax1.set_ylabel('Potential of Mean Force (eV)', fontsize=20, labelpad=10)
ax1.plot(s_bins_1_100k, fes_smooth_1_100k, color='#0000a2', lw=2)
ax1.plot(s_bins_2_100k, fes_smooth_2_100k, color='#bc272d', lw=2)
ax1.plot(s_bins_3_100k, fes_smooth_3_100k, color='#e9c716', lw=2)
ax1.plot(s_bins_4_100k, fes_smooth_4_100k, color='#50ad9f', lw=2)
ax1.plot(s_bins_1_300k, fes_smooth_1_300k, color='#0000a2', lw=2, ls='--')
ax1.plot(s_bins_2_300k, fes_smooth_2_300k, color='#bc272d', lw=2, ls='--')
ax1.plot(s_bins_3_300k, fes_smooth_3_300k, color='#e9c716', lw=4, ls='--', dashes=(2, 0.7))
ax1.plot(s_bins_4_300k, fes_smooth_4_300k, color='#50ad9f', lw=2, ls='--')
ax1.tick_params(axis='y', labelsize=16)
ax1.tick_params(axis='x', labelsize=16)
ax1.grid(True, which='major', axis='x', linestyle='--')
ax1.grid(True, which='major', axis='y', linestyle='--')

# set x range
ax1.set_xlim(0, 1)
# set y range
ax1.set_ylim(0, 0.5)


def remove_zero_tick_label(x, pos):
    return "" if x == 0 else f"{x:.1f}"


ax1.yaxis.set_major_formatter(FuncFormatter(remove_zero_tick_label))

# set x major 0.2 and minor ticks 0.1
ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
ax1.yaxis.set_major_locator(MultipleLocator(0.1))
ax1.yaxis.set_minor_locator(MultipleLocator(0.02))

# set legend in two columns
ax1.legend(['100K Path-1', '100K Path-2', '100K Path-3', '100K Path-4',
            '300K Path-1', '300K Path-2', '300K Path-3', '300K Path-4'],
           fontsize=16, loc='upper center', ncol=2)

plt.tight_layout()
plt.savefig('combine_plot_100k_300k.tif', dpi=300)
plt.show()
