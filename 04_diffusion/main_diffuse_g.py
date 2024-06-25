import numpy as np


def hop_rate(kb, h, r, t, g):
    return (kb * t / h) * np.exp(-g / (r * t))


# Constants in eV units
kb_eV = 8.617333262e-5  # Boltzmann constant in eV/K
h_eV = 6.582119569e-16  # Planck's constant in eV·s
r_eV = 8.617333262e-5  # Gas constant in eV/K

# Parameters
s_1 = 3e-10
s_2 = 4e-10
n = 2
m22cm2 = 1e4

# Calculate rate and diffusion coefficients
r_t100_1 = hop_rate(kb_eV, h_eV, r_eV, 100, 0.17)
d_t100_1 = r_t100_1 * (s_1 ** 2) / 2 / n * m22cm2
print("rate_t100_1:", r_t100_1)
print("diffusion_coefficient_t100_1:", d_t100_1)

r_t100_2 = hop_rate(kb_eV, h_eV, r_eV, 100, 0.26)
d_t100_2 = r_t100_2 * (s_1 ** 2) / 2 / n * m22cm2
print("rate_t100_2:", r_t100_2)
print("diffusion_coefficient_t100_2:", d_t100_2)

r_t300_1 = hop_rate(kb_eV, h_eV, r_eV, 300, 0.12)
d_t300_1 = r_t300_1 * (s_1 ** 2) / 2 / n * m22cm2
print("rate_t300_1:", r_t300_1)
print("diffusion_coefficient_t300_1:", d_t300_1)

r_t700_1 = hop_rate(kb_eV, h_eV, r_eV, 700, 0.20)
d_t700_1 = r_t700_1 * (s_2 ** 2) / 2 / n * m22cm2
print("rate_t700_1:", r_t700_1)
print("diffusion_coefficient_t700_1:", d_t700_1)

r_t1000_1 = hop_rate(kb_eV, h_eV, r_eV, 1000, 0.17)
d_t1000_1 = r_t1000_1 * (s_2 ** 2) / 2 / n * m22cm2
print("rate_t1000_1:", r_t1000_1)
print("diffusion_coefficient_t1000_1:", d_t1000_1)

f = 96485.3329  # Faraday constant in C/mol
r = 8.314462618  # Gas constant in J/(mol·K)

# Calculate ionic conductivity S cm-1
sigma = f ** 2 * d_t300_1 / (r * 300)
