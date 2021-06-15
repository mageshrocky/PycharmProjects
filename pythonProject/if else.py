mark = int(input('enter the mark:'))
if 75 <= mark < 90:
    print(f'{mark} is better')

elif mark >= 90:
    print(f'{mark} is best')

elif 40 < mark < 75:
    print(f'{mark} is good')

elif mark < 40:
    print(f'{mark} is fail')
