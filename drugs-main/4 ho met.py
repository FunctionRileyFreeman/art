import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for 4-HO-MET visualization
fig_4homet, ax_4homet = plt.subplots(figsize=(8, 8))

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_4homet = np.random.rand(50, 50)

# Apply 4-HO-MET effect by enhancing neural activity
neural_activity_4homet = np.sqrt(neural_activity_4homet)

# Display the neural activity as an image
ax_4homet.imshow(neural_activity_4homet, cmap='viridis', interpolation='nearest')

# Add title and remove axes
ax_4homet.set_title('Neural Activity Under 4-HO-MET Influence')
ax_4homet.axis('off')

# Show the plot for 4-HO-MET
plt.show()
