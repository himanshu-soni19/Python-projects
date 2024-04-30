import subprocess
import os
import random

base_path = r"G:\mr. robot"  # My base directory

# Get a random folder from the base directory
random_folder = random.choice(os.listdir(base_path))

# Construct the full path to the random folder
folder_path = os.path.join(base_path, random_folder)

# Change the current directory to the chosen folder
os.chdir(folder_path)

# Get a random file from the chosen folder
random_file = random.choice(os.listdir(folder_path))

# Print a message
print("Enjoy!")

# Execute the random file using subprocess
file_path = os.path.join(folder_path, random_file)
subprocess.run(file_path, shell=True)
