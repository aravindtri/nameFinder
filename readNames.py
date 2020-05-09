import re

file = open("/Users/ajanarth/Documents/babyNames.txt")
contents = file.read()
names = re.findall("\'([a-z A-Z]+)\'", contents)

file = open("/Users/ajanarth/Documents/babyNames1.txt")
contents = file.read()
names = names + re.findall("\'([a-z A-Z]+)\'", contents)


print(len(names))

lst2 = sorted(names, key=len)

print(lst2)