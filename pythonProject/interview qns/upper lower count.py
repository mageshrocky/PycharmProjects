x = 'BiXiTaCaDeMy'
count1 = 0
count2 = 0

for i in x:
    if i.isupper():
        count1 += 1
    elif i.islower():
        count2 += 1

print(f'count of uppercase letters is {count1}')
print(f'count of lowercase letters is {count2}')