# Synthetic Dataset Creation

This script generates labeled synthetic image datasets for machine learning experiments. It supports creating simple patterns like **vertical stripes**, **horizontal stripes**, and **diagonal patterns**, with options for adding noise and customizing image sizes.

## Features
1. **Generate Custom Datasets**:
   - Adjustable parameters for image size, noise level, and total number of samples.
   - Patterns include:
     - Vertical stripes (Label: 0)
     - Horizontal stripes (Label: 1)
     - Diagonal patterns (Label: 2).

2. **Labeled and Partitioned Datasets**:
   - Datasets are automatically split into training, validation, and testing sets.
   - Labels are embedded in filenames (e.g., `train_0_label_0.png`).

3. **Ready-to-Use Outputs**:

   - Images are saved in PNG format, organized by dataset splits.

## Example Usage
1. Run the script to generate datasets:
python generate_imagify.py

![val_30_label_1](https://github.com/user-attachments/assets/68b66d18-d70b-4d7a-9e28-ce2686844d8d)
![val_28_label_2](https://github.com/user-attachments/assets/d45d3ae2-2517-4298-9d25-a64bfa6e9727)
![val_44_label_0](https://github.com/user-attachments/assets/f0eb9a5a-f653-46fc-9367-5a9a9ccd4cb1)

