import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity = np.random.rand(50, 50)

# Apply Ketamine effect by distorting neural activity
neural_activity = neural_activity + np.random.randn(50, 50) * 0.3

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax.imshow(neural_activity, cmap='plasma', interpolation='nearest')

# Add title and remove axes
ax.set_title('Neural Activity Under Ketamine Influence')
ax.axis('off')

# Show the plot
plt.show()
