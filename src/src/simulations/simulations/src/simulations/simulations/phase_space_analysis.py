import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

"""
Phase space analysis of Euler–Arnold system
Comparison:
- Uniform dissipation
- Selective dissipation
- Two regimes: K ≈ 0 and K ≈ 3
"""

# -------------------------
# System with dissipation
# -------------------------
def euler_arnold_dissipative(t, xi, h, gamma):
    x1, x2, x3, x4, x5, x6 = xi
    h1, h2, h3, h4, h5, h6 = h

    dx1 = x2*x3*(h2 - h3) + x5*x6*(h5 - h6) - gamma[0]*x1
    dx2 = x3*x1*(h3 - h1) + x6*x4*(h6 - h4) - gamma[1]*x2
    dx3 = x1*x2*(h1 - h2) + x4*x5*(h4 - h5) - gamma[2]*x3

    dx4 = x3*x5*(-h3 - h5) + x2*x6*(h2 + h6) - gamma[3]*x4
    dx5 = x1*x6*(-h1 - h6) + x3*x4*(h3 + h4) - gamma[4]*x5
    dx6 = x2*x4*(-h2 - h4) + x1*x5*(h1 + h5) - gamma[5]*x6

    return [dx1, dx2, dx3, dx4, dx5, dx6]

# -------------------------
# Initial condition
# -------------------------
xi0 = [-0.499422, 0.513364, 0.779068, 0.844301, -0.127379, 0.625175]

# -------------------------
# Parameter sets
# -------------------------
h_case1 = [0.966405, 0.0567617, 0.983445, 0.077315, 0.915247, 0.0762157]  # K ≈ 0
h_case2 = [0.966405, 0.0567617, 0.983445, 0.077315, 0.915247, 1.85638]   # K ≈ 3

# -------------------------
# Dissipation
# -------------------------
gamma_uniform = np.array([0.01]*6)
gamma_selective = np.array([0, 0, 0, 0.1, 0.1, 0.1])

# -------------------------
# Time setup
# -------------------------
t_span = (0, 500)
t_eval = np.linspace(0, 500, 20000)
cut = 2000

# -------------------------
# Solver
# -------------------------
def solve_system(h, gamma):
    return solve_ivp(
        euler_arnold_dissipative,
        t_span,
        xi0,
        args=(h, gamma),
        t_eval=t_eval,
        method='DOP853',
        rtol=1e-10,
        atol=1e-10
    )

# Solve all cases
sol_k0_u = solve_system(h_case1, gamma_uniform)
sol_k0_s = solve_system(h_case1, gamma_selective)

sol_k3_u = solve_system(h_case2, gamma_uniform)
sol_k3_s = solve_system(h_case2, gamma_selective)

# -------------------------
# Phase plot (active modes)
# -------------------------
a, b = 0, 3  # x1 vs x4

fig, ax = plt.subplots(1, 2, figsize=(10,5))

# K ≈ 0
ax[0].plot(sol_k0_u.y[a][cut:], sol_k0_u.y[b][cut:], label="Uniform γ", alpha=0.7)
ax[0].plot(sol_k0_s.y[a][cut:], sol_k0_s.y[b][cut:], label="Selective γ", alpha=0.7)
ax[0].set_title("K ≈ 0")
ax[0].set_xlabel("x1")
ax[0].set_ylabel("x4")
ax[0].axis("equal")
ax[0].legend()
ax[0].grid(alpha=0.3)

# K ≈ 3
ax[1].plot(sol_k3_u.y[a][cut:], sol_k3_u.y[b][cut:], label="Uniform γ", alpha=0.7)
ax[1].plot(sol_k3_s.y[a][cut:], sol_k3_s.y[b][cut:], label="Selective γ", alpha=0.7)
ax[1].set_title("K ≈ 3")
ax[1].set_xlabel("x1")
ax[1].set_ylabel("x4")
ax[1].axis("equal")
ax[1].legend()
ax[1].grid(alpha=0.3)

plt.tight_layout()

# Save figure
plt.savefig("figures/phase_space_comparison.png", dpi=300)

plt.show()
