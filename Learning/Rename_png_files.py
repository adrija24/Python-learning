import os

folder = "images"

count = 1

for filename in os.listdir(folder):
    if filename.endswith(".png"):
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, f"{count}.png")
        os.rename(old_path, new_path)
        count = count + 1