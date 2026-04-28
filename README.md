# Energy Cascade and Symmetry Breaking in a Truncated Euler–Arnold System  
### A Numerical Study of Nonlinear Mode Coupling


## Overview

This project presents a numerical investigation of energy transfer in a finite-dimensional truncation of an Euler–Arnold system. The system serves as a reduced-order model of nonlinear geometric dynamics, capturing essential features of mode coupling and energy redistribution.

The focus is on understanding how initial symmetry and its breaking influence the long-term evolution of energy across interacting modes.



## Physical Motivation

Euler–Arnold equations arise naturally in fluid mechanics and geometric mechanics as geodesic flows on Lie groups. In high-dimensional settings, direct analysis becomes intractable, motivating simplified truncated models that preserve nonlinear interaction structure.

This work explores whether such truncated systems retain signatures of energy cascade behavior and instability under symmetry breaking.



## Model

We consider a finite-dimensional state vector:

x(t) = (x₁(t), x₂(t), ..., xₙ(t))

evolving under nonlinear quadratic interactions:

dx/dt = B(x, x)

where B(x, x) encodes bilinear mode coupling consistent with an Euler–Arnold structure.

The total energy of the system is defined as:

E(t) = (1/2) Σ hᵢ xᵢ(t)²

where hᵢ represents mode-dependent weights arising from the underlying structure of the truncated system.

This weighted energy is used to track redistribution and conservation properties across modes.



## Numerical Method

- Time integration: explicit Runge–Kutta (RK4 / adaptive solver)
- System size: 6-mode truncation
- Initial conditions:
  - Nearly symmetric configuration
  - Strongly asymmetric perturbation
- Observables:
  - Mode energies Eᵢ(t)
  - Total energy E(t)
  - Energy transfer structure across modes

---

## Results


The system exhibits qualitatively distinct behavior depending on the regime of initial conditions and coupling parameters.

### Near-Balanced Initial Conditions (low γ)

For initial conditions close to a balanced configuration, nonlinear interactions between modes remain weak. Mode energies remain broadly distributed, and no persistent concentration in any single mode is observed. The dynamics are characterized by near-oscillatory behavior with limited energy transfer.

---

### Strongly Perturbed Initial Conditions (higher γ)

For more strongly perturbed initial states, nonlinear coupling becomes more pronounced. Energy redistribution across modes is observed, with transient localization followed by spreading across the mode spectrum. This indicates enhanced nonlinear interaction between modes.

---

## Regime Interpretation

The observed behavior suggests the existence of qualitatively different dynamical regimes:

- Weak-interaction regime: small perturbations, limited energy transfer  
- Strong-interaction regime: enhanced coupling and redistribution of energy  

Although no full parameter sweep is performed, the system behavior is consistent with a transition between weakly coupled and strongly coupled dynamics as perturbation strength and weighting structure vary.

---

## Phase-Space Interpretation (Qualitative)

The system can be conceptually understood in a two-parameter space:

- γ : strength of initial perturbation  
- hᵢ distribution : structure of mode coupling  

Within this space, the dynamics qualitatively separate into:

- Weakly interacting regime  
- Transitional regime  
- Strong redistribution regime  

This suggests regime-dependent behavior even in low-dimensional truncations.

## Physical Insight

Symmetry plays a stabilizing role in truncated Euler–Arnold dynamics. When symmetry is broken, nonlinear interactions are amplified, leading to redistribution of energy across modes.

Even in low-dimensional truncations, the system retains structural signatures of energy cascade phenomena typically associated with higher-dimensional fluid dynamics.

---

## Repository Structure

euler-arnold-energy-cascade/
│
├── src/
│   ├── system.py
│   ├── solver.py
│   ├── diagnostics.py
│   └── utils.py
│
├── experiments/
│   ├── symmetric_case.py
│   ├── asymmetric_case.py
│   └── parameter_sweep.py
│
├── results/
│   ├── figures/
│   └── data/
│
├── notebooks/
│   └── analysis.ipynb
│
├── paper/
│   └── main.tex
│
└── README.md

---

## How to Run

git clone https://github.com/your-username/euler-arnold-energy-cascade.git  
cd euler-arnold-energy-cascade  
pip install -r requirements.txt  
python experiments/asymmetric_case.py  

---

## Author

Arpna Mishra  
Interests: Nonlinear dynamics, cosmology, geometric mechanics, and reduced-order models of complex systems

---

## Outlook

This framework can be extended to study:
- Higher-dimensional truncations
- Stability and Lyapunov analysis
- Energy cascade scaling behavior
- Hamiltonian structure of reduced systems
