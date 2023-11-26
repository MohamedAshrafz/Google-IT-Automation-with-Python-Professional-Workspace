import os 

# change directory
os.chdir(
    "e:/Python/Google_IT_Automation_with_Python"
    + "/02_Using_Python_to_Interact_with_the_OS/week2_files/directories"
)

# making of the directories and the files indide it
os.mkdir("new_dir_by_code")
os.mkdir("new_dir_by_code/by_code")
with open("new_dir_by_code/new_file.txt", "w") as f:
    f.write("")

with open("new_dir_by_code/new_file2.txt", "w") as f:
    f.write("")

# # # deleting all the files in this directory
# parent = os.path.abspath("new_dir_by_code")
# print(parent)
# if os.path.isdir("new_dir_by_code"):
#     for file in os.listdir("new_dir_by_code"):
#         absFilePath = os.path.join(parent, file)
#         print(absFilePath)
#         if os.path.isdir(absFilePath):
#             os.rmdir(absFilePath)
#         else:
#             os.remove(absFilePath)

# # remove directory if and only if it's empty 
# os.rmdir("new_dir_by_code")
    

print(os.listdir())
print(os.getcwd())