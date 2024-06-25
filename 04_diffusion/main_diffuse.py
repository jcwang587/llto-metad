import numpy as np


def hop_rate(nu, t, ea):
    return nu * np.exp(-ea / (1.38064852e-23 * t))


nu = 1e12
ev2j = 1.60217662e-19
s_1 = 3e-10
s_2 = 4e-10

r_t100_1 = hop_rate(nu, 100, 0.17 * ev2j)
d_t100_1 = r_t100_1 * (s_1 ** 2) / 4 * 1e4
print("rate_t100_1", r_t100_1)
print("diffusion_coefficient_t100_1", d_t100_1)
r_t100_2 = hop_rate(nu, 100, 0.26 * ev2j)
d_t100_2 = r_t100_2 * (s_1 ** 2) / 4 * 1e4
print("rate_t100_2", r_t100_2)
print("diffusion_coefficient_t100_2", d_t100_2)

r_t300_1 = hop_rate(nu, 300, 0.12 * ev2j)
d_t300_1 = r_t300_1 * (s_1 ** 2) / 4 * 1e4
print("rate_t300_1", r_t300_1)
print("diffusion_coefficient_t300_1", d_t300_1)

r_t700_1 = hop_rate(nu, 700, 0.20 * ev2j)
d_t700_1 = r_t700_1 * (s_2 ** 2) / 4 * 1e4
print("rate_t700_1", r_t700_1)
print("diffusion_coefficient_t700_1", d_t700_1)

r_t1000_1 = hop_rate(nu, 1000, 0.17 * ev2j)
d_t1000_1 = r_t1000_1 * (s_2 ** 2) / 4 * 1e4
print("rate_t1000_1", r_t1000_1)
print("diffusion_coefficient_t1000_1", d_t1000_1)


