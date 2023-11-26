import re

# notice the behaviour without the \b (word boundries)
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

# \w matches any word character (equivalent to [a-zA-Z0-9_])
# \d matches a digit (equivalent to [0-9])
# \s matches any whitespace character (equivalent to [\r\n\t\f\v  ])
# \b assert position at a word boundary: (^\w|\w$|\W\w|\w\W)


# \W matches any non-word character (equivalent to [^a-zA-Z0-9_])
# \D matches any character that's not a digit (equivalent to [^0-9])
# \S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
# \B assert position where \b does not match