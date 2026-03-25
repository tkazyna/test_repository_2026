import os
import shutil

# create folder
os.makedirs("my_folder/subfolder", exist_ok=True)

# list files
print("All files:", os.listdir("."))

# find .txt files
for file in os.listdir("."):
    if file.endswith(".txt"):
        print("TXT file:", file)

# Copy
shutil.copy("data.txt", "my_folder/data_copy.txt")

# Move
shutil.move("data.txt", "my_folder/subfolder/data_moved.txt")