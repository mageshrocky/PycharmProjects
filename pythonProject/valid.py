import re
class val:
    def validate_name(self,name):
        name = re.compile(r'^[A-Z]{1}[a-z]{2,20}$')
        res= name.search(self.name)
        try:
            if res:
                return self.name
            else:
                raise
        except:
            print('please Enter valid name')

    def validate_mail(self,mail_id):
        mail = re.compile(r'[a-z0-9]{5,10}@[a-z]{3,6}\.[a-z]{2,4}$')
        res1 = mail.search(self.mail_id)
        try:
            if res1:
                return self.mail_id
            else:
                raise
        except:
            print('please Enter valid mail_id')
    def validate_mob(self):
        mob = re.compile(r'[6789]{1}\d{9}$')
        res2 = mob.search(self.mob_num)
        try:
            if res2:
                return self.mob_num
            else:
                raise
        except:
            print('please enter valid mob_num')
    def validate_iamt(self):
        amt = re.compile(r'[1000]')
        res3 = amt.search(amt)
        try:
            if res3:
                return self.initial_amount
            else:
                raise
        except:
            print('Initial amount must be $10000')
from datetime import date, timedelta

def dle():
    z = date.today()
    x = int(input('date:'))
    y = z + timedelta(x)
    print(y)

dle()