import numpy as np
import matplotlib.pyplot as plt

# This is the histogram equalization function implementation

def histogram_equalization(image):
    # Calculate histogram
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Apply histogram equalization
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    equalized_image = equalized_image.reshape(image.shape)

    return equalized_image


# Example
image = np.array([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [90, 100, 110, 120],
                  [130, 140, 150, 160],
                  [170, 180, 190, 200],
                  [210, 220, 230, 240]])

equalized_image = histogram_equalization(image)

# Plotting the original and equalized images with their titles
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()