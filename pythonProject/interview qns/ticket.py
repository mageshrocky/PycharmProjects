import datetime
from numpy import random

x = datetime.datetime.now()
train_num = random.randint(9, size=5)

print('Welcome to INDIAN RAILWAYS')
print('HAPPY JOURNEY', x)
print(f'your train number is {train_num}')

d = {'beach': 1,
     'fort': 2,
     'park': 3,
     'egmore': 4,
     'chetpet': 5,
     'nungambakam': 6,
     'kodambakkam': 7,
     'mambalam': 8,
     'saidapet': 9,
     'guindy': 10,
     'mount': 11,
     'palavanthangal': 12,
     'minambakkam': 13,
     'tirusulam': 14,
     'pallavaram': 15,
     'chrompet': 16,
     'sanatorium': 17,
     'tambaram': 18
     }

start = input('enter your starting point:')
destination = input('enter your destination:')
i = d[start]
j = d[destination]
cj = j - i
passengers = int(input('how many passengers?:'))
ret = input('return[Y/N]:')
count = 0
fare = 5
if cj < 10:
    if passengers == 1:
        if ret == 'Y':
            print(fare * 2)
        elif ret == 'N':
            print(fare)
    elif passengers > 1:
        count += passengers
        if ret == 'Y':
            u = (fare * count) * 2
            print(u)
elif cj > 10:
    if passengers == 1:
        if ret == 'Y':
            g = (fare + 5) * 2
            print(g)
        elif ret == 'N':
            g = (fare + 5)
            print(g)
    elif passengers > 1:
        if ret == 'Y':
            g = (fare + 5) * 2
            count += passengers
            u = (g * count)
            print(u)
        elif ret == 'N':
            g = (fare + 5)
            count += passengers
            u = (g * count)
            print(u)
