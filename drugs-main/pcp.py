import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity = np.random.rand(50, 50)

# Apply PCP effect by distorting neural activity
neural_activity = np.random.rand(50, 50) * neural_activity

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax.imshow(neural_activity, cmap='magma', interpolation='nearest')

# Add title and remove axes
ax.set_title('Neural Activity Under PCP Influence')
ax.axis('off')

# Show the plot
plt.show()
