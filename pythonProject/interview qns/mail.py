x = '0303'
l1 = []
l2 = []
ask = int(input('How many users do you want to register?:'))

while ask > 0:
    print(ask)
    user_name = input('Enter your username:')
    pswd = int(input('Enter your password:'))
    if user_name in l1:
        print('username already exist')
        continue
    else:
        l1.append(user_name)
        l2.append(pswd)
        ask -= 1
f = {'user': l1, 'pwd': l2}
print(f)
log_in = input('Do you want to login[y/n]:')
if log_in == 'y':
    mail_id = input('Enter your mail_id:')
    password = int(input('enter your password:'))
    if mail_id in f['user']:
        try:
            if l1.index(mail_id) == l2.index(password):
                print('login successful!')
        except:
            print('mail_id & password doesnt match')
        k = input('forgot password[y/n]:')
        if k == 'y':
            print('you will receive an OTP')
            print(x)
            otp = (input('please enter your OTP:'))
            if x == otp:
                i = l1.index(mail_id)
                l2.pop(i)
                new = int(input('enter new password:'))
                l2.insert(i, new)
                print(f)
                mail_id = input('Enter your mail_id:')
                password = int(input('enter your password:'))
                if mail_id in f['user']:
                    try:
                        if l1.index(mail_id) == l2.index(password):
                            print('login successful!')
                            print(mail_id, password)
                    except:
                        print('wrong password')
    else:
        print('invalid username')
elif log_in == 'n':
    print('All accounts are successfully registered!')
    print(f)
