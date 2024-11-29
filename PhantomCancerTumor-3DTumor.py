import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D


# Generate a 3D synthetic phantom with a tumor
def create_tumor_phantom(size=128, tumor_radius=20, tumor_position=(64, 64, 64), tumor_density=1.0):
    # Create a 3D grid
    x, y, z = np.indices((size, size, size))

    # Create a spherical tumor
    cx, cy, cz = tumor_position
    tumor_mask = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 <= tumor_radius ** 2
    tumor = np.zeros((size, size, size))
    tumor[tumor_mask] = tumor_density

    # Create background tissue
    background = np.random.normal(0.2, 0.05, (size, size, size))  # Noise to simulate tissue

    # Combine tumor with background
    phantom = background + tumor

    # Smooth for realism
    phantom = gaussian_filter(phantom, sigma=2)

    return phantom


# Visualize the 3D tumor structure
def plot_tumor_slice(phantom, slice_idx):
    plt.figure(figsize=(8, 6))
    plt.imshow(phantom[:, :, slice_idx], cmap="hot")
    plt.title(f"Tumor Phantom (Slice {slice_idx})")
    plt.colorbar(label="Intensity")
    plt.axis("off")
    plt.show()


def plot_tumor_3d(phantom, threshold=0.5):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Extract coordinates of the high-intensity region (tumor)
    coords = np.array(np.where(phantom > threshold))
    ax.scatter(coords[0], coords[1], coords[2], c=phantom[phantom > threshold], cmap="hot", s=1)

    ax.set_title("3D Tumor Structure")
    plt.show()


# Generate the phantom
size = 128
tumor_radius = 20
tumor_position = (64, 64, 64)
phantom = create_tumor_phantom(size=size, tumor_radius=tumor_radius, tumor_position=tumor_position)

# Visualize a 2D slice of the phantom
plot_tumor_slice(phantom, slice_idx=64)

# Visualize the 3D structure
plot_tumor_3d(phantom, threshold=0.5)
