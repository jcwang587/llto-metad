import numpy as np


def hop_rate(kb, h, r, t, g):
    return (kb * t / h) * np.exp(-g / (r * t))


# Constants in eV units
kb_eV = 8.617333262e-5  # Boltzmann constant in eV/K
h_eV = 6.582119569e-16  # Planck's constant in eV·s
r_eV = 8.617333262e-5  # Gas constant in eV/K
na = 6.02214076e23  # Avogadro's number in mol^-1
f = 96485.3329  # Faraday constant in C/mol
r = 8.314462618  # Gas constant in J/(mol·K)

# Parameters
t = 300
d = 11.636 / 3 * 1e-10
s = np.pi * d / 4 * (0.674887 - 0.269337)

# Calculate rate and diffusion coefficients
r_t300 = hop_rate(kb_eV, h_eV, r_eV, t, 0.16)
d_t300 = r_t300 * (s ** 2) / 4
print("rate_t300:", r_t300)
print("diffusion_coefficient_t300:", d_t300)

lbd = d_t300 * f ** 2 / (r * t)
print("lambda:", lbd)

v = 11.636 * 11.636 * 7.905  # in angstrom^3
c = 6 / na / (v / 1e30)

sigma = lbd * c / 100
print("sigma:", sigma)
