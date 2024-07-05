from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Load the data
s_bins_1_100k = np.load('100k_s_bins_1.npy')
s_bins_2_100k = np.load('100k_s_bins_2.npy')
s_bins_3_100k = np.load('100k_s_bins_3.npy')
s_bins_4_100k = np.load('100k_s_bins_4.npy')
s_bins_1_300k = np.load('300k_s_bins_1.npy')
s_bins_2_300k = np.load('300k_s_bins_2.npy')
s_bins_3_300k = np.load('300k_s_bins_3.npy')
s_bins_4_300k = np.load('300k_s_bins_4.npy')

fes_smooth_1_100k = np.load('100k_fes_smooth_1.npy')
fes_smooth_1_100k = fes_smooth_1_100k - np.min(fes_smooth_1_100k)
fes_smooth_2_100k = np.load('100k_fes_smooth_2.npy')
fes_smooth_2_100k = fes_smooth_2_100k - np.min(fes_smooth_2_100k)
fes_smooth_3_100k = np.load('100k_fes_smooth_3.npy')
fes_smooth_3_100k = fes_smooth_3_100k - np.min(fes_smooth_3_100k)
fes_smooth_4_100k = np.load('100k_fes_smooth_4.npy')
fes_smooth_4_100k = fes_smooth_4_100k - np.min(fes_smooth_4_100k)
fes_smooth_1_300k = np.load('300k_fes_smooth_1.npy')
fes_smooth_1_300k = fes_smooth_1_300k - np.min(fes_smooth_1_300k)
fes_smooth_2_300k = np.load('300k_fes_smooth_2.npy')
fes_smooth_2_300k = fes_smooth_2_300k - np.min(fes_smooth_2_300k)
fes_smooth_3_300k = np.load('300k_fes_smooth_3.npy')
fes_smooth_3_300k = fes_smooth_3_300k - np.min(fes_smooth_3_300k)
fes_smooth_4_300k = np.load('300k_fes_smooth_4.npy')
fes_smooth_4_300k = fes_smooth_4_300k - np.min(fes_smooth_4_300k)

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
ax1.plot(s_bins_3_300k, fes_smooth_3_300k, color='#e9c716', lw=2, ls='--')
ax1.plot(s_bins_4_300k, fes_smooth_4_300k, color='#50ad9f', lw=5, ls='--', dashes=(1.6, 0.55))
ax1.plot(s_bins_4_300k, fes_smooth_4_300k, color='#50ad9f', lw=9, alpha=0.3)
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
