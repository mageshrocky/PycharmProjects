sec_code = 1234
balance = 1500
user = input('withdrawal or balance enquiry:')
pin = int(input('enter the pin:'))

if user == 'withdrawal':
    if pin == sec_code:
        print('collect your cash')
    else:
        print('enter a valid pin')

elif user == 'balance enquiry':
    if pin == sec_code:
        print(f'{balance} is your current balance')
    else:
        print('enter a valid pin')

else:
    print('choose the correct option')
