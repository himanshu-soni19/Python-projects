import os
import random

# "\" are used as escape characters in python which will give us warning so, or we can use \\ or raw string r"".
# (In a raw string, backslashes are treated as literal characters rather than escape characters)

p = "G:\\mr. robot"  # this path is for windows, if you are using linux path will be like p = "/mnt/g/mr. robot".
os.chdir(p)   # to change dir in p.


folder_name = random.choice(os.listdir(p))  # here we are choosing random folder from the list of folders in p.

folder_path = str(os.path.realpath(folder_name))  # this is the path of the random folder chosen.
os.chdir(folder_path)                            # changing dir to the folder_path.
file_name = random.choice(os.listdir(folder_path))  # choosing random file from the folder_path dir.

print("Enjoy!")

os.system(file_name)  # playing file
