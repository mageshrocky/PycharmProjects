num = int(input('enter the number:'))

for i in range(num):
    option = input('skip,exit or print')
    if option == 'print':
        print(i)
    elif option == 'skip':
        continue
    elif option == 'exit':
        break

print('goodbye!')