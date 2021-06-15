import re

a = "welcome to BIX IT ACADEMY"
x = re.split('\s',a)
print(x)

x = re.split('\s',a,3)
print(x)

x = re.sub('\s','#',a,2)
print(x)

x = re.search('o',a)
print(x.span())
print(x.string)
print(x.group())

x = re.findall("A",a)
print(x)


list = ['7339228061','8456137981','9381587965','9994562138']
for record in list:
    if re.match(r'[789]\d{9}',record):
        print(record)

amt1 = (input('enter'))
amt = re.compile(r'[1000]')
res = amt.search(amt1)
if res:
    print('ok')
else:
    print('not ok')