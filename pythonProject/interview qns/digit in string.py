'''s = input("enter the string:")
for i in s:
    if i.isdigit():
        print("true")
    else:
        print("false")

s = input("enter the string:")

if s.isdigit():
    print("true")
else:
    print("false")'''

def string(s):
    return any(i.isdigit() for i in s)
s = "mnl12"
string(s)

import re
c = "zxc"
if re.search(r"\d", c):
    print("true")
else:
    print("false")