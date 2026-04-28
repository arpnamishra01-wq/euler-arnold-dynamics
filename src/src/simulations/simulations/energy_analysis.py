import numpy as np
import matplotlib.pyplot as plt
from src.system import euler_arnold
from src.solver import solve_system

# Parameters
h = [1, 3, 6, 3, 2, 10]

# Initial condition
xi0 = [3.0, 4.0, 5.0, 0.0001, 0.01, 1.5]

# Time setup
t_span = (0, 100)
t_eval = np.linspace(0, 100, 10000)

# Solve
sol = solve_system(euler_arnold, xi0, h, t_span, t_eval)

# Extract solution
x1, x2, x3, x4, x5, x6 = sol.y

# Energies
EA = x1**2 + x2**2 + x3**2
EB = x4**2 + x5**2 + x6**2

# Plot
plt.figure()
plt.plot(sol.t, EA, label='E_A')
plt.plot(sol.t, EB, label='E_B')

plt.xlabel("Time")
plt.ylabel("Energy")
plt.title("Energy Transfer Between Modes")

plt.legend()
plt.grid()

plt.savefig("figures/energy_transfer.png", dpi=300, bbox_inches='tight')
plt.show()
