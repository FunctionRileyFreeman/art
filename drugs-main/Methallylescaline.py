import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for Methallylescaline visualization
fig_methallylescaline, ax_methallylescaline = plt.subplots(figsize=(8, 8))

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_methallylescaline = np.random.rand(50, 50)

# Apply Methallylescaline effect by enhancing neural activity
neural_activity_methallylescaline = np.sqrt(neural_activity_methallylescaline)

# Display the neural activity as an image
ax_methallylescaline.imshow(neural_activity_methallylescaline, cmap='viridis', interpolation='nearest')

# Add title and remove axes
ax_methallylescaline.set_title('Neural Activity Under Methallylescaline Influence')
ax_methallylescaline.axis('off')

# Show the plot for Methallylescaline
plt.show()
