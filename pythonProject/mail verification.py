l1 = ['magesh@gmail.com', 'rajesh@gmail.com', 'nisar@gmail.com', 'hari@gmail.com']
l2 = [101, 102, 103, 104]
f = dict(zip(l1, l2))
username = input('enter your mailid:')
password = int(input('enter password:'))
u = username
if u in f.keys():
    if f[u] == password:
        print('login successfull')
    else:
        print('incorrect password')
else:
    print('enter valid email')

print(f)




