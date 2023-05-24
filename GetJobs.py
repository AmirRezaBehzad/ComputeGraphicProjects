import numpy as np
import matplotlib.pyplot as plt

# This is the logarithm replacement function implementation

def logarithm_replacement(image):
    bit_depth = 8
    max_intensity = 2 ** bit_depth - 1
    log_replaced_image = np.log2(image + 1) * (max_intensity / np.log2(max_intensity + 1))
    log_replaced_image = np.clip(log_replaced_image, 0, max_intensity).astype(np.uint8)
    return log_replaced_image

# Load the image using Matplotlib and NumPy
image = plt.imread('image.jpg')

# Convert the image to grayscale if needed
if image.ndim == 3:
    image = np.mean(image, axis=2)

# Perform the logarithm replacement
replaced_image = logarithm_replacement(image)

# Display the original and replaced images with their titles using Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(replaced_image, cmap='gray')
axes[1].set_title('Logarithm Replaced Image')
axes[1].axis('off')
plt.show()