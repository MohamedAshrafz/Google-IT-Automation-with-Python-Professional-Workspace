#!/usr/bin/env python3

import re
import csv


# import os

# os.chdir(
#     r"E:\Python\Google_IT_Automation_with_Python\02_Using_Python_to_Interact_with_the_OS\week3_regex".replace(
#         "\\", "/"
#     )
# )


def contains_domain(address, domain):
    domain_pattern = r'[\w\.-]+@' + domain + '$'
    domain_pattern = r"[\w\.-]+@" + domain + "$"
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r'' + old_domain + '$'
    old_domain_pattern = r"" + old_domain + "$"
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    old_domain, new_domain = "abc.edu", "xyz.edu"

    # replace <username>
    # csv_file_location = "user_emails.csv"
    csv_file_location = "/home/student-01-21d877cb70ab/data/user_emails.csv"
    # report_file = "updated_user_emails.csv"
    report_file = "/home/student-01-21d877cb70ab/data" + "/updated_user_emails.csv"

    email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, "r") as f:
        data_list = list(csv.reader(f))
        email_list = [data[1].strip() for data in data_list[1:]]

        for email_address in email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                new_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(new_email)

        email_key = " " + "Email Address"
        email_index = data_list[0].index(email_key)

        for user in data_list[1:]:
            for old_email_domail, new_email_domain in zip(
                old_domain_email_list, new_domain_email_list
            ):

                if user[email_index] == " " + old_email_domail:
                    user[email_index] = " " + new_email_domain
    f.close    

    with open(report_file, "w+", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data_list)
        output_file.close()


main()
