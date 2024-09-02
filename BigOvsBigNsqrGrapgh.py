import matplotlib.pyplot as plt
import numpy as np

# Generate data points
n = np.arange(1, 11)  # Values of n from 1 to 10

# O(n) and O(n^2) functions
o_n = n
o_n_squared = n**2

# Plot the curves
plt.plot(n, o_n, label='O(n)')
plt.plot(n, o_n_squared, label='O(n^2)')

# Set labels and title
plt.xlabel('n')
plt.ylabel('Operations')
plt.title('O(n) vs O(n^2)')

# Add legend
plt.legend()

# Show the plot
plt.show()
