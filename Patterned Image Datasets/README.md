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
python generate_imagefy.py


<img width="227" alt="Screen Shot 2024-11-28 at 9 48 42 PM" src="https://github.com/user-attachments/assets/b415b9e5-cee2-45b4-84f5-3fe6f101b97e">
<img width="229" alt="Screen Shot 2024-11-28 at 9 48 57 PM" src="https://github.com/user-attachments/assets/7aa0e4f0-136f-4af7-95c0-1a47241f0697">
<img width="231" alt="Screen Shot 2024-11-28 at 9 49 32 PM" src="https://github.com/user-attachments/assets/85173da0-de64-4444-a6cd-7f42acd84303">

