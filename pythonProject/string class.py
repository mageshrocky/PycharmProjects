name = ['nisar', 'magesh', 'parthiban', 'lokesh']
k = 'kar,thick'
num = [101, 102, 103, 104, 105, 106]

#string methods

print(name[1])
print(len(name))
print('lokesh' in name)
print(k.upper())
print(k.lower())
print(k.strip())
print(k.replace('k','p'))
print(k.split(","))
print(max(num))
print(min(num))
print(sum(num))

m_nake = 'parthi'
data = "My \"name\" is \n{}"
print('my name is {}'.format(m_nake))

print(data.format(m_nake))
for record in name:
    if record == 'magesh':
        print('record found')

#slicing strings
print(k[:5])
print(k[2:6])
print(k[5:])
print(k[-3:-1])