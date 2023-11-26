#!/usr/bin/env python3

import csv
import os

cd = "E:\\Python\\Google_IT_Automation_with_Python\\02_Using_Python_to_Interact_with_the_OS\\week2_files".replace(
    "\\", "/"
)

os.chdir(cd)


def read_employees(csv_file_location):
    with open(csv_file_location, newline="", encoding="utf-8") as file:
        csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
        employee_reader = csv.DictReader(file, dialect="empDialect")
        employee_list = []
        for row in employee_reader:
            employee_list.append(row)
    return employee_list

def process_data(employee_list):
    department_dictionary = {}
    for employee_data in employee_list:
        if employee_data["Department"] not in department_dictionary:
            department_dictionary[employee_data["Department"]] = 1
        else:
            department_dictionary[employee_data["Department"]] += 1
    return department_dictionary

def write_report(dictionary, report_file):
    with open(report_file, "+w") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')



employee_list = read_employees("employees.txt")
for row in employee_list:
    print(row)

dictionay = process_data(employee_list)

for key, value in dictionay.items():
    print(key + " value = " + str(value))

write_report(dictionay, "report.txt")
