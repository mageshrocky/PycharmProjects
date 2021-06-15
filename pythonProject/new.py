import datetime
import pymysql

data = pymysql.connect(host='localhost', user='root', passwd='', database='bank')
z = data.cursor()
z.execute('use bank')

print('WELCOME TO BANK OF MAGESH')
c = datetime.datetime.now()
print(c)


class Bank:

    def personal_details(self):

        print('YOUR PERSONAL DETAILS')
        print('name:', self.name)
        print('mob_no:', self.mob_num)
        print('mail_id:', self.mail_id)
        print('balance:', self.balance)
        print('account number:', self.acc_num)
        z.execute("INSERT INTO BANKING (ACC_NO,CUSTOMER_NAME,MOB_NO,MAIL_ID,BALANCE) VALUES(%s,%s,%s,%s,%s)",
                  (self.acc_num, self.name, self.mob_num, self.mail_id, self.balance))
        data.commit()

    def new_user(self):
        print('FILL YOUR DETAILS')
        self.name = input('enter your name:')
        self.mob_num = int(input('enter your mobile number:'))
        self.mail_id = input('enter your mail_id:')
        self.balance = int(input('enter the amount:'))
        self.acc_num = int(input('create your account number:'))

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

    def e_user(self):
        an = input('enter your account number:')
        z.execute('select * from banking where ACC_NO =%s', an)
        details = z.fetchone()
        print(details)
        x.select()


x = Bank()
ask = input('1:NEW USER OR 2:EXISTING USER:')
if ask == '1':
    x.new_user()
    x.select()
elif ask == '2':
    x.e_user()