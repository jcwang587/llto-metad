import numpy as np


def hop_rate(kb, h, t, g):
    return (kb * t / h) * np.exp(-g / (kb * t))


# Constants in SI units
kb_j = 1.380649e-23  # Boltzmann constant in J/K
h_j = 6.62607015e-34  # Planck's constant in J·s
na = 6.02214076e23  # Avogadro's number in mol^-1
f = 96485.3329  # Faraday constant in C/mol
r = 8.314462618  # Gas constant in J/(mol·K)

# Parameters
t = 300  # Temperature in K
g = 0.16 * 1.602176634e-19  # Activation energy in J
s = 11.636 / 6 * np.sqrt(2) * 1e-10

# Calculate rate and diffusion coefficients
r_t300 = hop_rate(kb_j, h_j, t, g)
d_t300 = r_t300 * (s ** 2) / 4
print("rate_t300:", r_t300)
print("diffusion_coefficient_t300:", d_t300)

lbd = d_t300 * f ** 2 / (r * t)
print("lambda:", lbd)

v = 11.636 * 11.636 * 7.905  # in angstrom^3
c = 6 / na / (v / 1e30)  # in mol/m^3

sigma = lbd * c / 100
print("sigma:", sigma)
