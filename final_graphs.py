import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.05457e-34  
m = 1.66e-27        
k_B = 1.38e-23   
n_0 = 1e20

# Range of particle density (Chosen based on internet findings)
n = np.linspace(1e25, 1e29, 100)  

# Critical temperature Tc
Tc = (2 * np.pi * hbar**2 / (m * k_B)) * (n / 2.612)**(2/3)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(n, Tc, label='Critical Temperature $T_c$')
plt.xlabel('Particle Density ($n$) [particles/m³]')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(True)
plt.show()

