import numpy as np
import matplotlib.pyplot as plt
from src.system import euler_arnold
from src.solver import solve_system

# Initial condition
xi0 = [-0.499422, 0.513364, 0.779068, 0.844301, -0.127379, 0.625175]

# Parameters
h_case1 = [0.966405, 0.0567617, 0.983445, 0.077315, 0.915247, 0.0762157]  # K ≈ 0
h_case2 = [0.966405, 0.0567617, 0.983445, 0.077315, 0.915247, 1.85638]   # K ≈ 3

# Time setup
t_span = (0, 500)
t_eval = np.linspace(0, 500, 50000)

# Solve systems
sol1 = solve_system(euler_arnold, xi0, h_case1, t_span, t_eval)
sol2 = solve_system(euler_arnold, xi0, h_case2, t_span, t_eval)

# Plot setup
pairs = [(0,3), (4,5), (2,5)]
fig, ax = plt.subplots(2, 3, figsize=(12,7))

cut = 3000
start = 2000

for i, (a, b) in enumerate(pairs):

    # K ≈ 0
    ax[0,i].plot(sol1.y[a][cut:], sol1.y[b][cut:], linewidth=0.3)
    ax[0,i].set_title(f"K≈0 : xi{a+1} vs xi{b+1}")
    ax[0,i].axis('equal')

    # K ≈ 3
    ax[1,i].plot(sol2.y[a][start:], sol2.y[b][start:], linewidth=0.3)
    ax[1,i].set_title(f"K≈3 : xi{a+1} vs xi{b+1}")
    ax[1,i].axis('equal')

plt.tight_layout()
plt.savefig("figures/phase_space.png", dpi=300, bbox_inches='tight')
plt.show()
