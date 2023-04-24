import os
import random

# Define the path to the directory containing the images
path = "data/images"

# Define the list of valid file extensions
valid_extensions = [".jpg", ".JPG", ".png", ".jpeg"]

# Initialize empty lists to store the paths to the images
image_paths = []
train_paths = []
valid_paths = []

# Loop through all files in the directory
for filename in os.listdir(path):
    # Check if the file has a valid extension
    if any(filename.endswith(extension) for extension in valid_extensions):
        # If so, add the path to the list of image paths
        image_paths.append(os.path.join(path, filename))

# Randomly shuffle the list of image paths
random.shuffle(image_paths)

# Split the list of image paths into training and validation sets
split_index = int(0.7 * len(image_paths))
train_paths = image_paths[:split_index]
valid_paths = image_paths[split_index:]

# Write the training and validation paths to their respective text files
with open(os.path.join(path, "train.txt"), "w") as train_file:
    for train_path in train_paths:
        train_file.write(train_path + "\n")

with open(os.path.join(path, "valid.txt"), "w") as valid_file:
    for valid_path in valid_paths:
        valid_file.write(valid_path + "\n")
