import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_mix = np.random.rand(50, 50)

# Apply combined effect by enhancing neural activity
neural_activity_mix = (neural_activity_mix ** 2) * 1.5  # Concerta
neural_activity_mix += (np.random.rand(50, 50) ** 3) * 2  # Cocaine
neural_activity_mix += (np.random.rand(50, 50) ** 2) * 1.2  # MDMA

# Create a figure and axis for mixed visualization
fig_mix, ax_mix = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_mix.imshow(neural_activity_mix, cmap='hot', interpolation='nearest')

# Add title and remove axes
ax_mix.set_title('Neural Activity Under Concerta, Cocaine, and MDMA Influence')
ax_mix.axis('off')

# Show the plot for mixed influence
plt.show()
