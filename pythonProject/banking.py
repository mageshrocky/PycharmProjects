import datetime
import pymysql

data = pymysql.connect(host='localhost', user='root', passwd='', database='BANK')
z = data.cursor()
z.execute('use BANK')

print('welcome to BANK OF MAGESH ROCKY')

time = datetime.datetime.now()
print(time)


class User:
    def __init__(self):
        pass

    def new_user(self, acc_num, name, mob_num, mail_id, balance):
        self.acc_num = acc_num
        self.name = name
        self.mob_num = mob_num
        self.mail_id = mail_id
        self.balance = balance

    def personal_details(self):
        print('acc_no:', self.acc_num)
        print('customer_name:', self.name)
        print('mob_num:', self.mob_num)
        print('mail_id:', self.mail_id)
        print('initial amount:', self.balance)
        z.execute("INSERT INTO BANKING (ACC_NO,CUSTOMER_NAME,MOB_NO,MAIL_ID,BALANCE) VALUES(%s,%s,%s,%s,%s)",
                  (self.acc_num, self.name, self.mob_num, self.mail_id, self.balance))
        data.commit()


class Bank_account(User):

    def select(self):
        opt = input('3:deposit or 4:withdraw or 5:balance or 6:exit:')
        if opt == '3':
            x.deposit()
        elif opt == '4':
            x.withdraw()
        elif opt == '5':
            x.balance_enquiry()
        elif opt == '6':
            print('process ended')

    def deposit(self):
        amount = int(input('enter the amount:'))
        self.balance = self.balance + amount
        z.execute('update BANKING set BALANCE=%s where CUSTOMER_NAME=%s', (self.balance, self.name))
        data.commit()
        print(f'your account balance is {self.balance}')
        x.select()

    def withdraw(self):
        amount = int(input('enter the amount:'))
        try:
            if self.balance > 5000:
                self.balance = self.balance - amount
                z.execute('update BANKING set BALANCE=%s where CUSTOMER_NAME=%s', (self.balance, self.name))
                data.commit()
                print(f'your current balance is {self.balance}')
            else:
                raise
        except:
            print('you have insufficient balance')
        x.select()

    def balance_enquiry(self):
        print(f'your available balance is {self.balance}')
        x.select()


ask = (input('1:NEW_USER or 2:EXISTING_USER:'))
if ask == '1':
    print('fill your details')
    acc_num = int(input('enter your acc_num:'))
    name = input('enter your name:')
    mob_num = int(input('enter your mob_num:'))
    mail_id = input('enter your mail_id:')
    balance = int(input('enter your initial payment:'))
    x = Bank_account()
    x.new_user()
    x.personal_details()
    x.select()

import datetime
import re
from numpy import random

z = random.randint(9, size=8)
print('WELCOME TO BANK OF MAGESH')
c = datetime.datetime.now()
print(c)
d = {}


class Bank:

    def personal_details(self):
        self.balance = self.initial_amount
        print('name:', self.name)
        print('mob_no:', self.mob_no)
        print('mail_id:', self.mail_id)
        print('balance:', self.balance)
        print('this is your account number')
        print(z)

    def new_user(self):
        self.name = input('enter your name:')
        if re.match(r'^[A-Z]{1}[a-z]{2,20}$', self.name):
            return self.name
        else:
            print('Invalid name, name first letter must be capital others will be in small letter')
            x.new_user()
        self.mob_no = input('enter your mobile number:')
        if re.match(r'[6789]{1}\d{9}$', self.mob_no):
            return self.mob_no
        else:
            print('Mobile number not exceed 10 digits')
            x.new_user()
        self.mail_id = input('enter your mail_id:')
        if re.match(r'[a-z0-9]{5,10}@[a-z]{3,6}\.[a-z]{2,4}$', self.mail_id):
            return self.mail_id
        self.initial_amount = int(input('enter the amount:'))
        if self.initial_amount >= 5000:
            return self.initial_amount
        else:
            print('initial must be 5000rs or more')
            x.new_user()
        self.acc_no = z
        self.personal_details()

    def select(self):
        opt = input('3:deposit or 4:withdraw or 5:balance or 6:exit:')
        if opt == '3':
            x.deposit()
        elif opt == '4':
            x.withdraw()
        elif opt == '5':
            x.balance_enquiry()
        elif opt == '6':
            print('process ended')

    def deposit(self):
        amount = int(input('enter the amount:'))
        self.balance = self.balance + amount
        print(f'your account balance is {self.balance}')
        x.select()

    def withdraw(self):
        amount = int(input('enter the amount:'))
        try:
            if self.balance > 5000:
                self.balance = self.balance - amount
                print(f'your current balance is {self.balance}')
            else:
                raise
        except:
            print('you have insufficient balance')
        x.select()

    def balance_enquiry(self):
        print(f'your available balance is {self.balance}')
        x.select()


x = Bank()
ask = input('1:NEW USER OR 2:EXISTING USER:')
if ask == '1':
    x.new_user()
    x.select()
