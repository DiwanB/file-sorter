"""
-------------------------------------------------------
Automatically sorts files in a path inputted by the user.
Usage:
-Run the script
-Enter a file path
Outputs:
-all files sorted by file path, in different folders
for each file path
-------------------------------------------------------
Author:  Diwan Bhangal
Email:   diwanbhangal04@gmail.ca
__updated__ = "2024-02-20"
-------------------------------------------------------
"""
# Imports
import os, shutil

# Constants

is_valid_path = False
while is_valid_path == False:
    path = input("Enter the path of the folder containing the unsorted files: ")
    path = path.replace("\\", "/")
    is_valid_path = os.path.exists(path);
    if is_valid_path == False:
        print("Not a valid path!")
    else:
        last_char = path[len(path)-1];
        if last_char != "/":
            path = path + "/"
print(f"Items in path:", os.listdir(path))
file_names = os.listdir(path)
folder_names = ["PDF Files", "PNG Files", "JPG Files", "MP3 Files", "MP4 Files", "Text Files", "Executable Files", "Shortcut Files", "GIF Files"]
file_types = [".pdf", ".png", ".jpg", ".mp3", ".mp4", ".txt", ".exe", ".lnk", ".gif"]
for i in range(0, len(folder_names)):
    print(f"Does {folder_names[i]} exist:", os.path.exists(path + folder_names[i]))
    if not (os.path.exists(path + folder_names[i])):
        os.makedirs(path + folder_names[i])
for file in file_names:
    for filetype, folder in zip(file_types, folder_names):
        if filetype in file and not os.path.exists(path + folder + '/' + file):
            shutil.move(path + file, path + folder + '/' + file)
        
