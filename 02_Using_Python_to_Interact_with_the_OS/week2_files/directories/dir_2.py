import os 

# change directory
os.chdir(
    "e:/Python/Google_IT_Automation_with_Python"
    + "/02_Using_Python_to_Interact_with_the_OS/week2_files/directories"
)

print(os.path.abspath(""))

print(os.listdir())

# getting the absolute path of this new directory 
dir = os.path.abspath("new_dir_by_code")
print(dir)

for name in os.listdir(dir):
    # adding the file names to the absolute directory 
    # independant from the os path notation
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

