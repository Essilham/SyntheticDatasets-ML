import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split


def generate_pattern(image_size=8, pattern_type="vertical", noise_level=0.1):
    """
    Generate a synthetic image with a specific pattern.
    Args:
        image_size (int): Size of the square image (image_size x image_size).
        pattern_type (str): Type of pattern ('vertical', 'horizontal', 'diagonal').
        noise_level (float): Amount of noise to add to the image.
    Returns:
        np.array: Synthetic image as a 2D numpy array.
    """
    image = np.zeros((image_size, image_size))

    if pattern_type == "vertical":
        image[:, ::2] = 1  # Vertical stripes
        label = 0
    elif pattern_type == "horizontal":
        image[::2, :] = 1  # Horizontal stripes
        label = 1
    elif pattern_type == "diagonal":
        np.fill_diagonal(image, 1)  # Diagonal pattern
        label = 2
    else:
        raise ValueError("Unsupported pattern type.")

    # Add noise
    image += noise_level * np.random.rand(image_size, image_size)
    image = np.clip(image, 0, 1)  # Ensure values are between 0 and 1
    return image, label


def create_labeled_datasets(output_dir="dataset", image_size=8, num_samples=300, noise_level=0.1):
    """
    Generate labeled datasets for training, validation, and testing.
    Args:
        output_dir (str): Directory to save the datasets.
        image_size (int): Size of the square images.
        num_samples (int): Total number of images across all sets.
        noise_level (float): Noise level in the images.
    Returns:
        dict: Partitioned datasets with 'train', 'val', and 'test' keys.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Generate synthetic data
    X = []
    y = []
    pattern_types = ["vertical", "horizontal", "diagonal"]

    for _ in range(num_samples):
        pattern_type = np.random.choice(pattern_types)
        image, label = generate_pattern(image_size=image_size, pattern_type=pattern_type, noise_level=noise_level)
        X.append(image)
        y.append(label)

    X = np.array(X)
    y = np.array(y)

    # Split data into training, validation, and testing sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    datasets = {
        "train": {"X": X_train, "y": y_train},
        "val": {"X": X_val, "y": y_val},
        "test": {"X": X_test, "y": y_test},
    }

    # Save datasets
    for split, data in datasets.items():
        split_dir = os.path.join(output_dir, split)
        os.makedirs(split_dir, exist_ok=True)
        for i, (image, label) in enumerate(zip(data["X"], data["y"])):
            filename = f"{split}_{i}_label_{label}.png"
            filepath = os.path.join(split_dir, filename)
            plt.imsave(filepath, image, cmap="gray")
        print(f"Saved {split} dataset with {len(data['X'])} images to {split_dir}")

    return datasets


# Run the script to generate datasets
datasets = create_labeled_datasets(output_dir="dataset", image_size=8, num_samples=300, noise_level=0.1)
