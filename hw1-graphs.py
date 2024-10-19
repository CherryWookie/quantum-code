import numpy as np
import matplotlib.pyplot as plt

# This code is to visualize the wave functions for the first three states,
# in addition to the ground state for the first homework problem. Thanks to some help from Chatgpt
# Michael Sell 2024

# Define the parameters
a = 1  # Length of the well (can be adjusted)

# Define the wavefunctions
def psi_odd(n, x, a):
    return np.sqrt(1/a) * np.sin(n * np.pi * x / 2 * a)

def psi_even(n, x, a):
    return np.sqrt(1/a) * np.cos((((2*n + 1) * np.pi * x)) / 2 * a)

# Create an array for the x-axis (the domain of the functions)
x = np.linspace(0, a, 1000)

# Calculate the wavefunctions for the first four states
psi_0 = psi_even(0,x,a) # Ground State
psi_1 = psi_odd(1, x, a)  # Ground state (n = 1, odd)
psi_2 = psi_even(2, x, a)  # First excited state (n = 2, even)
psi_3 = psi_odd(3, x, a)  # Second excited state (n = 3, odd)
psi_4 = psi_even(5/2, x, a)  # Third state (n = 4, even)


# Plot the wavefunctions
plt.figure(figsize=(8, 6))

# Plot ground state
plt.plot(x, psi_0, label=r'$\psi_0(x) = \sqrt{\frac{1}{a}} \sin\left(\frac{\pi x}{2a}\right)$', color='red')

plt.plot(x, psi_1, label=r'$\psi_1(x) = \sqrt{\frac{1}{a}} \sin\left(\frac{\pi x}{2a}\right)$', color='blue')

# Plot first excited state
plt.plot(x, psi_2, label=r'$\psi_2(x) = \sqrt{\frac{1}{a}} \cos\left(\frac{5\pi x}{2a}\right)$', color='orange')

# Plot second excited state
plt.plot(x, psi_3, label=r'$\psi_3(x) = \sqrt{\frac{1}{a}} \sin\left(\frac{3\pi x}{2a}\right)$', color='green')

# # Plot third state
# plt.plot(x, psi_4, label=r'$\psi_4(x) = \sqrt{\frac{1}{a}} \cos\left(\frac{5\pi x}{2a}\right)$', color='red')

# Add labels and legend
plt.title('First Three Stationary States of the Overdamped Rotating Pendulum (Including n = 0)')
plt.xlabel('Position x (in units of a)')
plt.ylabel('Wavefunction $\psi(x)$')
plt.legend(loc='upper right')

# Show the plot
plt.grid(True)
plt.show()
