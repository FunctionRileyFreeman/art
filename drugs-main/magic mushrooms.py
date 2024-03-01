import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity = np.random.rand(50, 50)

# Apply magic mushrooms effect by distorting neural activity
neural_activity = np.sin(neural_activity * np.pi * 2)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax.imshow(neural_activity, cmap='spring', interpolation='nearest')

# Add title and remove axes
ax.set_title('Neural Activity Under Magic Mushrooms Influence')
ax.axis('off')

# Show the plot
plt.show()
