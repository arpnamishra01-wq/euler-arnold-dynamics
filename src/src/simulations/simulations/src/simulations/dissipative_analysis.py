import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from src.system_dissipative import euler_arnold_dissipative

"""
Comparison of dissipation mechanisms:
1. Uniform dissipation (all modes damped)
2. Selective dissipation (only higher modes damped)

Goal:
Understand energy decay and transfer behavior.
"""

# -------------------------
# Initial condition
# -------------------------
xi0 = [-0.499422, 0.513364, 0.779068, 0.844301, -0.127379, 0.625175]

# -------------------------
# Parameters
# -------------------------
h = [0.966405, 0.0567617, 0.983445, 0.077315, 0.915247, 1.85638]

# -------------------------
# Dissipation cases
# -------------------------
gamma_uniform = np.array([0.01]*6)
gamma_selective = np.array([0, 0, 0, 0.1, 0.1, 0.1])

# -------------------------
# Time setup
# -------------------------
t_span = (0, 500)
t_eval = np.linspace(0, 500, 20000)

# -------------------------
# Solver
# -------------------------
def solve_system(gamma):
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

# Solve both cases
sol_uniform = solve_system(gamma_uniform)
sol_selective = solve_system(gamma_selective)

# -------------------------
# Energy computation
# -------------------------
def total_energy(sol):
    return 0.5 * np.sum(sol.y**2, axis=0)

def mode_energy(sol):
    return 0.5 * sol.y**2

E_uniform = total_energy(sol_uniform)
E_selective = total_energy(sol_selective)

# -------------------------
# Plot: total energy comparison
# -------------------------
plt.figure()
plt.plot(sol_uniform.t, E_uniform, label="Uniform γ")
plt.plot(sol_selective.t, E_selective, label="Selective γ")

plt.xlabel("Time")
plt.ylabel("Total Energy")
plt.title("Total Energy Comparison")
plt.legend()
plt.grid()

plt.savefig("figures/energy_comparison.png", dpi=300)
plt.show()

# -------------------------
# Plot: mode energies (selective case)
# -------------------------
E_modes = mode_energy(sol_selective)

plt.figure(figsize=(10,4))
for i in range(6):
    plt.plot(sol_selective.t, E_modes[i], label=f"E{i+1}")

plt.title("Mode Energies (Selective Dissipation)")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend(ncol=3, fontsize=8)
plt.grid()

plt.savefig("figures/mode_energy_selective.png", dpi=300)
plt.show()
