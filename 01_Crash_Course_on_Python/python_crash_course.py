# # for loops in python
# print("hi")
# friends = ["mohamed", "andrew", "amr", "george"]
# for friend in friends:
#     print("9 " + " 8")


# # using , in print function
# print("hi", "there")
# hi = "hi"
# there = "there"
# print(hi + "" + there)


# # returning multiple values from a function
# def hoursMinutesAndSeconds(seconds):
#     hours = seconds // (60 * 60)
#     minutes = (seconds - hours * (60 *60)) // 60
#     seconds = seconds - (hours * (60 *60) + minutes * 60)
#     return hours, minutes, seconds

# hours, minutes, seconds = hoursMinutesAndSeconds(5000)
# print(hours)
# print(minutes)
# print(seconds)

# print(False)


# # if and elif
# num = 20
# if (num > 0 and num <= 5):
#     print("the number:", str(num) + "\nis bigger than 0 and less than or equal 5")
# elif (num > 5 and num <= 7):
#     print("the number:", str(num) + "\nis bigger than 5 and less than or equal 7")
# else:
#     print("the number:", str(num) + "\nis bigger than 7")

# print("Hello World")

# test_num = 12
# if test_num > 15:
#     print(test_num / 4)
# else:
#     print(test_num + 3)

# def difference(x, y):
#     z = x - y
#     return z


# print("difference(5, 3)", end=" ")
# print("difference(5, 3)", end=" ")

# number = 4
# if number * 4 < 15:
#  print(number / 4)
# elif number < 5:
#  print(number + 3)
# else:
#  print(number * 2 % 5)

# for number in range(6):
#     print(number, end = " ")

# for x in range(10):
#     for y in range(x):
#         print(y)

# for count in range(1, 6):
#     print(count+1)

# speed_limits = {"street": 35, "highway": 65, "school": 15}
# print(speed_limits["highway"])

# music_genres = ["rock", "pop", "country"]
# music_genres.append("blues")
# print(music_genres)

# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

##################################################################################

# def count_factors(given_number):

#   # To include the "given_number" variable as a "factor", initialize
#   # the "factor" variable with the value 1 (if the "factor" variable
#   # were to start at 2, the "given_number" itself would be excluded).
#   factor = 1
#   count = 0

#   # This "if" block will run if the "given_number" equals 0.
#   if given_number == 0:
#     # If True, the return value will be 0 factors.
#     return 0

#   # The while loop will run while the "factor" is still less than
#   # the "given_number" variable.
#   while factor <= given_number:
#     # This "if" block checks if the "given_number" can be divided by
#     # the "factor" variable without leaving a remainder. The modulo
#     # operator % is used to test for a remainder.
#     if given_number % factor == 0:
#       # If True, then the "factor" variable is added to the count of
#       # the "given_number"’s integer factors.
#       count += 1
#     # When exiting the if block, increment the "factor" variable by 1
#     # to divide the "given_number" variable by a new "factor" value
#     # inside the while loop.
#     factor += 1

#   # When the interpreter exits either the while loop or the top if
#   # block, it will return the value of the "count" variable.
#   return count

# print(count_factors(0)) # Count value will be 0
# print(count_factors(3)) # Should count 2 factors (1x3)
# print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
# print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# # and 4x6).

# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.

##################################################################################

# def addition_table(given_number):
#     iterated_number = 1
#     my_sum = 1

#     while iterated_number <= 5:

#         my_sum = given_number + iterated_number

#         if my_sum > 100:
#             break

#         print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
#         iterated_number += 1


# addition_table(5)
# addition_table(17)
# addition_table(30)

##################################################################################


# # Fill in the blanks so that the while loop continues to run while the
# # "divisor" variable is less than the "number" parameter.

# def sum_divisors(number):
# # Initialize the appropriate variables
#   divisor = 1
#   total = 0

#   # Avoid dividing by 0 and negative numbers
#   # in the while loop by exiting the function
#   # if "number" is less than one
#   if number < 1:
#     return 0

#   # Complete the while loop
#   while divisor < number:
#     if number % divisor == 0:
#       total += divisor
#     # Increment the correct variable
#     divisor += 1

#   # Return the correct variable
#   return total


# print(sum_divisors(0)) # Should print 0
# print(sum_divisors(3)) # Should print 1
# # 1
# print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# # 114

##################################################################################


# def multiplication_table(number):
#     multiply = 1
#     result = -1

#     while multiply <= 5:
#         result = number * multiply

#         if result > 25:
#             break

#         print(str(number) + "x" + str(multiply) + "=" + str(result))
#         multiply += 1

# multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15

# multiplication_table(5)
# # Should print:
# # 5x1=5
# # 5x2=10
# # 5x3=15
# # 5x4=20
# # 5x5=25

# multiplication_table(8)
# # Should print:
# # 8x1=8
# # 8x2=16
# # 8x3=24

##################################################################################

# values = [23, 52, 89, 37, 48]

# sum = 0
# length = 0

# for value in values:
#     sum += value
#     length += 1

# print("The sum =: " + str(sum) + " - The average = " + str(float(sum)/length))

################################## Important #####################################

# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     # If number is equal to 1, it's a power (base**0).
#     return number == 1

#   # Recursive case: keep dividing number by base.
#   return is_power_of(number / base, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

##################################################################################

# massage = "A kong string with a silly typo"
# print(massage)

# massage = massage[:2] + "l" + massage[3:]
# print(massage)

################################## Regex #########################################


# import re
# "Forest".isnumeric()

# print(" ".join(["hi", "there,", "Mohamed"]))
# print(".. ".join(["hi", "there,", "Mohamed"]))

# print("This is another example".split())

# testMsg = "This example contain: elephant, dog and lion"
# removeIndex = testMsg.index(":")
# testMsg = testMsg[removeIndex + 2:]
# editedMsg = re.split(": |, | and ", testMsg)
# print(editedMsg)

################################## format method #################################


# def student_grade(name, grade):
#     return "{name} received {grade}% on the exam".format(name=name, grade=grade)


# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

##################################################################################

# # not formatted probably
# def to_celsius(inF):
#     return (inF - 32) * 5 / 9

# for temp in range(0, 101, 10):
#     print(str(temp) + " C | " + str(to_celsius(temp)) + " F")

# # formatted probably

# def to_celsius(inF):
#     return (inF - 32) * 5 / 9

# for temp in range(0, 101, 10):
#     print("{inFe:>3} F | {inCe:>6.2f} C".format(inFe = temp, inCe = to_celsius(temp)))

##################################################################################

# x = ["Hi", ",",  "there", "you", "little", "dude", "."]
# print(type(x))
# print(x)
# print("Hi" in x)
# print("hi" in x)
# print(x[0:2])

########################### Getting index in for loop ############################

# x = ["Hi", ",", "there", "you", "little", "dude", "."]
# for index, word in enumerate(x):
#     print("{} - {}".format(index + 1, word))

########################### List Comprehensions ##################################

# multiples = [x * 7 for x  in range (1, 11)]
# print(multiples)

# langs = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lenths = [len(lang) for lang in langs]
# print(lenths)

# z = [x for x in range(0, 101) if ((x % 3) == 0)]
# print(z)

##################################################################################

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# oldExt = "hpp"
# newExt = "h"

# newfilenames = []
# for fName in filenames:
#     if (oldExt in fName):
#         newfilenames.append(fName[:-len(oldExt)] + newExt)
#     else:
#         newfilenames.append(fName)

# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

##################################################################################

# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   for index, word in enumerate(words):
#     # Create the pig latin word and add it to the list
#     newWord = "{}{}ay".format(word[1:], word[0])
#     # Turn the list back into a phrase

#     say += newWord
#     if (index != len(words) - 1):
#       say += " "

#   return say

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

##################################################################################

# def group_list(group, users):
#   newStr = "{}: {}".format(group, ", ".join(users))
#   return newStr

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike,
#                                                                    # Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

##################################################################################

# def guest_list(guests):
# 	for name, age, prof in guests:
# 		print("{} is {} years old and works as {}".format(name, age, prof))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# #Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """

##################################################################################


# def format_address(address_string):
#     house_number = ""
#     street_name = ""

#     # Separate the house number from the street name.
#     address_parts = address_string.split()

#     for address_part in address_parts:
#         # Complete the if-statement with a string method.
#         if address_part.isnumeric():
#             house_number = address_part
#         else:
#             street_name += address_part + " "
#     # Remove the extra space at the end of the last "street_name".
#     street_name = street_name.rstrip(" ")

#     # Use a string method to return the required formatted string.
#     return "House number {number} on a street named {name}".format(
#         number=house_number, name=street_name
#     )


# print(format_address("123 Main Street"))
# # Should print: "House number 123 on a street named Main Street"


# print(format_address("1001 1st Ave"))
# # Should print: "House number 1001 on a street named 1st Ave"


# print(format_address("55 North Center Drive"))
# # Should print "House number 55 on a street named North Center Drive"

##################################################################################

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)
# help("")


