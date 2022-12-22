import os


# Function to find all files in a directory and its subdirectories
def find_files(directory):
    # Iterate over the files and directories in the specified directory
    for root, dirs, files in os.walk(directory):
        # Yield the files in the current directory
        for file in files:
            yield os.path.join(root, file)


# Find the files in the current directory and its subdirectories
files = find_files('.')

# Print the found files
for file in files:
    print(file)
