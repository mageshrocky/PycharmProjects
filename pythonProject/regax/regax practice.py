import re

str = "lavanya"
x = re.findall("a",str)
print(x)

y = re.search('a',str)
print(y)

def validatemail(email):
     return re.match(r'[a-z0-9]{5,10}@[a-z]{3,6}\.[a-z]{2,4}', email)

for i in range(5):
    email = input('enter the mail id:')
    valid = validatemail(email)
    if valid:
        print('your mail id is correct')
    else:
        raise ('the mail id you have entered is wrong')
