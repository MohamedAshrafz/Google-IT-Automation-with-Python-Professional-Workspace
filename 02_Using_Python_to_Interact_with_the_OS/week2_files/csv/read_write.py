import csv
import os


def printList(list):
    print()
    print("**********************Start**************************")
    for index, dict in enumerate(list):
        print("Index: {} - Contain: {}".format(index, dict))
    print("**********************End****************************")
    print()


cd = r"E:\Python\Google_IT_Automation_with_Python\02_Using_Python_to_Interact_with_the_OS\week2_files\csv".replace(r"\\", r"/")

os.chdir(cd)

print(os.getcwd())

file_list = []
keys = []
newd = {}

with open("Book1.csv") as file:
    csv_text = csv.reader(file)
    for index_i, row in enumerate(csv_text):
        if index_i == 0:
            keys = row[:]
            keys[0] = keys[0][3:]
        else:
            file_list.append({})
            for index, key in enumerate(keys):
                file_list[index_i - 1][key] = row[index]

printList(file_list)

# sum = 0
# for dict in file_dict.values():
#     sum += int(dict["salary"])

# print(sum)

file_list.sort(key=lambda x: int(x["salary"]), reverse=True)

printList(file_list)

with open("new_file.csv", "w", newline="", encoding="utf-8") as new_csv_file:
    writer = csv.writer(new_csv_file)
    for index, dict in enumerate(file_list):
        if index == 0:
            newf = list(dict.keys())
            newc = list(dict.values())
            writer.writerow(newf)
            writer.writerow(newc)
        else:
            newc = list(dict.values())
            writer.writerow(newc)

# write using DictWriter
with open("written_using_dict.csv", "w", newline="", encoding="utf-8") as new_csv_file:
    writer = csv.DictWriter(new_csv_file, fieldnames=file_list[0].keys())
    writer.writeheader()
    writer.writerows(file_list)

# read using DictReader
with open("written_using_dict.csv", newline='', encoding="utf-8") as read_file:
    csv_text = csv.DictReader(read_file)
    for row in csv_text:
        print(row)
