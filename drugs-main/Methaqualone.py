import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_quaaludes = np.random.rand(50, 50)

# Apply Quaaludes effect by smoothing neural activity
neural_activity_quaaludes = np.convolve(neural_activity_quaaludes.flatten(), np.ones(5)/5, mode='same').reshape(50, 50)

# Create a figure and axis for Quaaludes visualization
fig_quaaludes, ax_quaaludes = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_quaaludes.imshow(neural_activity_quaaludes, cmap='cividis', interpolation='nearest')

# Add title and remove axes
ax_quaaludes.set_title('Neural Activity Under Quaaludes Influence')
ax_quaaludes.axis('off')

# Show the plot for Quaaludes
plt.show()
