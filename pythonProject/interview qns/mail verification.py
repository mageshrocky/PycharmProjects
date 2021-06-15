x = '0303'
l1 = []
l2 = []
ask = int(input('How many users do you want to register?:'))

while ask>0:
    print(ask)
    user_name = input('Enter your username:')
    pswd = int(input('Enter your password:'))
    if user_name in l1:
        print('username already exist')
        continue
    else:
        l1.append(user_name)
        l2.append(pswd)
        ask -=1
f = dict(zip(l1, l2))
print(f)
log_in = input('Do you want to login[y/n]:')
if log_in == 'y':
    mail_id = input('Enter your mail_id:')
    password = int(input('enter your password:'))
    if mail_id in f.keys():
        if f[mail_id] == password:
            print('login successful!')
        else:
            print('mail_id & password doesnt match')
            k = input('forgot password[y/n]:')
            if k == 'y':
                print('you will receive an OTP')
                print(x)
                v = input('please enter your OTP:')
                if x == v:
                    new = int(input('enter new password:'))
                    f[mail_id] = new
                    print(f)
                    mail_id = input('Enter your mail_id:')
                    password = int(input('enter your password:'))
                    if mail_id in f.keys():
                        if f[mail_id] == password:
                            print('login successful!')
                            print(mail_id, password)
                        else:
                            print('wrong password')
elif log_in == 'n':
    print('All accounts are successfully registered!')
    print(f)

