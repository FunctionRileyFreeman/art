import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_5meodmt = np.random.rand(50, 50)

# Apply 5-MeO-DMT effect by distorting neural activity
neural_activity_5meodmt = np.random.rand(50, 50) * neural_activity_5meodmt ** 3

# Create a figure and axis for 5-MeO-DMT visualization
fig_5meodmt, ax_5meodmt = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_5meodmt.imshow(neural_activity_5meodmt, cmap='inferno', interpolation='nearest')

# Add title and remove axes
ax_5meodmt.set_title('Neural Activity Under 5-MeO-DMT Influence')
ax_5meodmt.axis('off')

# Show the plot for 5-MeO-DMT
plt.show()
