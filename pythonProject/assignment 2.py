import datetime

print('welcome to BANK OF MAGESH')

time = datetime.datetime.now()
print(time)

class user:
    def __init__(self,acc_num, name, mob_num, mail_id, balance):
        self.acc_num = acc_num
        self.name = name
        self.mob_num = mob_num
        self.mail_id = mail_id
        self.balance = balance
    def dic(self):
        l1 = []
        l2 = []
        l1.append(self.acc_num)
        l2.append(self.name)
        j = dict(zip(l1,l2))
        print(j)




    def personal_details(self):
        print('acc_no:', self.acc_num)
        print('customer_name:', self.name)
        print('mob_num:', self.mob_num)
        print('mail_id:', self.mail_id)
        print('initial amount:', self.balance)


class bank_account(user):
    def __init__(self,  acc_num, name, mob_num, mail_id, balance):
        super().__init__(acc_num, name, mob_num, mail_id, balance)
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



ask = (input('1:NEW_USER or 2:EXISTING_USER:'))
if ask == '1':
    print('fill your details')
    acc_num = int(input('enter your acc_num:'))
    name = input('enter your name:')
    mob_num = int(input('enter your mob_num:'))
    mail_id = input('enter your mail_id:')
    balance = int(input('enter your initial payment:'))
    x = bank_account(acc_num, name, mob_num, mail_id,balance)
    x.personal_details()
    x.select()

else:



