import os
import datetime

# change directory
# r is to indicate that this is a raw string (do not interpret any special character but sent it it to the function as it is)
os.chdir(r"E:\Python\Google_IT_Automation_with_Python\02_Using_Python_to_Interact_with_the_OS\week2_files\files".replace("\\", "/"))

print("getcwd() - " + os.getcwd())

with open("new_file.txt", "w") as newFile:
    newFile.write("hi there, how are you little one?")

print("getsize() - " + str(os.path.getsize("new_file.txt")))
print("getmtime() - " + str(os.path.getmtime("new_file.txt")))
print("fromtimestamp() - " + str(datetime.datetime.fromtimestamp(os.path.getmtime("new_file.txt"))))
print("abspath(\"new_file.txt\") - " + os.path.abspath("new_file.txt"))


os.rename("new_file.txt", "masterpiece.txt")

print("os.path.exists(\"new_file.txt\") - " + str(os.path.exists("new_file.txt")))
print("os.path.exists(\"masterpiece.txt\") - " + str(os.path.exists("masterpiece.txt")))

# if os.path.exists("new_file.txt"):
#     os.remove("new_file.txt")

# if os.path.exists("masterpiece.txt"):
#     os.remove("masterpiece.txt")