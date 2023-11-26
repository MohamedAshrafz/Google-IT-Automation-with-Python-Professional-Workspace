import re


print(re.search(r"p.ng", "panging"))
# notice the case sensitivity
print(re.search(r"P.ng", "panging"))
# using the flag re.IGNORECASE
print(re.search(r"P.ng", "panging", re.IGNORECASE))
# using findall to find all accurance of the pattern in the text
print(re.findall(r"P.ng", "pangpanging", re.IGNORECASE))

# using character classes to match more than one character in a position
print(re.findall(r"[pa]y", "py away hey way ray ai python"))
# and for ranges use -
print(re.findall(r"[a-c]y", "ay cy by dy ey fy python"))
# combine ranges 
print(re.findall(r"[a-zA-Z]", "py away hey way ray ai python"))
print(re.findall(r"[a-zA-Z]", "py away hey way ray ai python PY AWAY HEY WAY RAY AI PYTHON"))
# adding space
print(re.findall(r"[a-zA-Z ]", "py away hey way ray ai python"))
# the use of ^ inside the squere bracket
print(re.findall(r"[^a-zA-Z ]", "py away hey way ray ai python.,::?!"))

# the use of the or operator 
print(re.findall(r"dog|cat", "I like both dogs and cats"))

# repetation qualifiers
print(re.search(r"py.*n", "python"))
# notice that the star qualifier is greedy (takes as many characters as possible)
print(re.search(r"py.*n", "python programming"))
# if we only want to match words we can narrow the range on star qualifier
print(re.search(r"py[a-z]*n", "python programming"))


# + qualifier (one or more accurance)
# checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice
def repeating_letter_a(text):
  result = re.search(r"[aA]+.*[aA]+", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
print(repeating_letter_a("aabobrhf")) # True
print(repeating_letter_a("abobrhfagirg")) # True


# # ? qualifier (zero or one occurance)
# print(re.search(r"p?each", "to each their own"))
# print(re.search(r"p?each", "I like peaches"))

# \w (matches any alphanumeric or underscore character) == [a-zA-Z0-9_]
print(re.search(r"\w*", "this is a sentence."))
print(re.search(r"\w*", "this_is_a_sentence."))
# if we want to match the \w itself we use the escaping character backslash \
print(re.findall(r"\\w*", "this_is_a_sentence.\w\w"))

# \w matches any word character (equivalent to [a-zA-Z0-9_])
# \d matches a digit (equivalent to [0-9])
# \s matches any whitespace character (equivalent to [\r\n\t\f\v  ])
# \b assert position at a word boundary: (^\w|\w$|\W\w|\w\W)


# \W matches any non-word character (equivalent to [^a-zA-Z0-9_])
# \D matches any character that's not a digit (equivalent to [^0-9])
# \S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
# \B assert position where \b does not match

# repetation range (inclusive in both sides)
print(re.findall(r"a{2,6}", "aaXaaaXaaaaXaaaaaXaaaaaa"))

# anything not an a then from 2 to 6 a then anything not an a
print(re.findall(r"[^a]+a{2,6}[^a]+", "aaXaaaXaaaaXaaaaaXaaaaaa"))

# start of the text then from 2 to 6 a then anything not an a
print(re.findall(r"^a{2,6}[^a]+", "aaXaaaXaaaaXaaaaaXaaaaaa"))

# anything not an a then from 2 to 6 a then the end of the text
print(re.findall(r"[^a]+a{2,6}$", "aaXaaaXaaaaXaaaaaXaaaaaa"))
