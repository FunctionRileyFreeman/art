import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for DXM visualization
fig_dxm, ax_dxm = plt.subplots(figsize=(8, 8))

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_dxm = np.random.rand(50, 50)

# Apply DXM effect by distorting neural activity
neural_activity_dxm = neural_activity_dxm + np.random.randn(50, 50) * 0.3

# Display the neural activity as an image
ax_dxm.imshow(neural_activity_dxm, cmap='inferno', interpolation='nearest')

# Add title and remove axes
ax_dxm.set_title('Neural Activity Under DXM Influence')
ax_dxm.axis('off')

# Show the plot for DXM
plt.show()
