import os
import shutil

# Write
with open("data.txt", "w") as f:
    f.write("Hello еруку\nThis is a test file\n")

# REad
with open("data.txt", "r") as f:
    print(f.read())

# Add
with open("data.txt", "a") as f:
    f.write("New line added\n")

# check what i added
with open("data.txt", "r") as f:
    print(f.read())

#Copy
shutil.copy("data.txt", "backup.txt")

# Delete
#if os.path.exists("backup.txt"):
#    os.remove("backup.txt")