import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_bromazolam = np.random.rand(50, 50)

# Apply Bromazolam effect by smoothing neural activity
neural_activity_bromazolam = np.convolve(neural_activity_bromazolam.flatten(), np.ones(5)/5, mode='same').reshape(50, 50)

# Create a figure and axis for Bromazolam visualization
fig_bromazolam, ax_bromazolam = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_bromazolam.imshow(neural_activity_bromazolam, cmap='cividis', interpolation='nearest')

# Add title and remove axes
ax_bromazolam.set_title('Neural Activity Under Bromazolam Influence')
ax_bromazolam.axis('off')

# Show the plot for Bromazolam
plt.show()
