import re

result = re.search(r"([a-c]y)(dog|cat)", "cycat")

print(result.groups())
print(result[0])
print(result[1])
print(result[2])

############################################################################################

def check_zip_code (text):
  # The first ([^^][0-9]{5}) & the second (-[0-9]{4}) capture groups (has to use () to define capture group)
  # (notice if you used (()) this is considered as to separate capture gorups)
  result = re.search(r"([^^][0-9]{5})(-[0-9]{4})?", text)
  if result is not None:
    print(result.groups())
    print(result[0])
    print(result[1])
    print(result[2])
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

############################################################################################

def rearrange_name(name):
  result = re.search(r"^([\w \.\-]*), ([\w \.\-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

############################################################################################

# using boundery specifier
print(re.findall(r"\b\w{5}\b", "hi there really"))
# notice without using the boundery specifier 
print(re.findall(r"\w{5}", "hi there really"))
# you can use open ended 
print(re.findall(r"\b\w{5,}\b", "hi there really"))

############################################################################################

def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

############################################################################################

# using split function 
print(re.split(r"[.?!]", "one sentence. another one? and this is the last!"))
# notice of we want to capture the splitting characters we use capture parentheses 
print(re.split(r"([.?!])", "one sentence. another one? and this is the last!"))

# using sub to replace regexes
print(re.sub(r"[\w%\.\-\+]+@[\w%\.\-]+", "[REMOVED]", "you can use my mail which is: thisIsMyMail.hi@yahoo.com"))
# using backslask number as a reference to capture group
print(re.sub(r"([\w%\.\-\+]+)@([\w%\.\-]+)", r"the user is \1 in the domain \2", "you can use my mail which is: thisIsMyMail.hi@yahoo.com"))
