import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_concerta = np.random.rand(50, 50)

# Apply Concerta effect by enhancing neural activity
neural_activity_concerta = neural_activity_concerta ** 2

# Create a figure and axis for Concerta visualization
fig_concerta, ax_concerta = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_concerta.imshow(neural_activity_concerta, cmap='hot', interpolation='nearest')

# Add title and remove axes
ax_concerta.set_title('Neural Activity Under Concerta Influence')
ax_concerta.axis('off')

# Show the plot for Concerta
plt.show()
