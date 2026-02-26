import numpy as np
import matplotlib.pyplot as plt

# Paramètres
S0 = 100      # Prix initial
mu = 0.08    # Drift annuel (8%)
sigma = 0.20 # Volatilité annuelle (20%)
T = 1.0      # Horizon 1 an
N = 252      # Nombre de pas (jours)
M = 1000     # Nombre de trajectoires

dt = T / N
t = np.linspace(0, T, N)

# Simulation vectorisée (M trajectoires simultanées)
Z = np.random.standard_normal((M, N))  # Chocs aléatoires
increments = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
log_returns = np.cumsum(increments, axis=1)
S = S0 * np.exp(log_returns)  # Shape: (M, N)

# Visualisation
plt.figure(figsize=(12, 6))
plt.plot(t, S[:50].T, alpha=0.3, linewidth=0.8)
plt.xlabel('Temps (années)')
plt.ylabel('Prix S_t')
plt.title(f'GBM — {M} trajectoires (50 affichées)')
plt.show()

# Distribution finale
S_T = S[:, -1]
print(f"Prix moyen à T: {S_T.mean():.2f}")
print(f"Écart-type:     {S_T.std():.2f}")
print(f"Prix théorique: {S0 * np.exp(mu * T):.2f}")
