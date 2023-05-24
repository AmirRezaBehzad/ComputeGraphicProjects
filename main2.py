import numpy as np
import matplotlib.pyplot as plt


# This is the linear replacement function implementation

def linear_replacement(image, constant=0, factor=1):
    max_value = 255  # Maximum pixel value for 8-bit depth
    replaced_image = constant + (factor * image)
    replaced_image = np.clip(replaced_image, 0, max_value).astype(np.uint8)
    return replaced_image

# Load the image using Matplotlib and NumPy
image = plt.imread('image.jpg')

# Convert the image to a NumPy array
image_np = np.array(image)

# Define the constant and factor for linear replacement
constant = 20
factor = 1

# Perform linear replacement
replaced_image = linear_replacement(image_np, constant=constant, factor=factor)

# Display the original and replaced images with their titles using Matplotlib
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(image_np)
axs[0].set_title('Original Image')

axs[1].imshow(replaced_image)
axs[1].set_title('Replaced Image')

for ax in axs:
    ax.axis('off')

plt.tight_layout()
plt.show()
