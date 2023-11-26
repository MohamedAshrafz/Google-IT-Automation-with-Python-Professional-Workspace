import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    file.write("")

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
#   print(type(timestamp))
  return ("{}".format(str(timestamp)[:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd