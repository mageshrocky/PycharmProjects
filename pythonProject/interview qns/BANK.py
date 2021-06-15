import pymysql


db=pymysql.connect(host="localhost",user='root',password="",database='bank')
x=db.cursor()
x.execute("use bank")
#x.execute('create table account(name varchar(30),accountno int,mobileno int,mail varchar(30),balance int)')
#x.execute('create table amount(name varchar(30),accountno int,balance int)')


class bank():


    def openacc(self):
        n=input("Enter Name: ")
        ac=input("enter account number: ")
        p=int(input("enter mobile number: "))
        mail=input("enter mail Id: ")
        ob=int(input("enter opening balance: "))
        data1=(ac,n,p,mail,ob)
        sql1='insert into banking values(%s,%s,%s,%s,%s)'
        c=db.cursor()
        c.execute(sql1,data1)
        db.commit()
        print("Data Entered Successfully")
        obj.main()

    def deposit_Amount(self):
        am=int(input("Enter Amount: "))
        ac=input("Enter Account number: ")
        a="select balance from banking where accountno=%s"
        data=(ac,)
        c=db.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        tam=myresult[0]+am
        sql="update account set balance=%s where accountno=%s"
        d=(tam,ac)
        c.execute(sql,d)
        db.commit()
        obj.main()

    def withdraw_amount(self):
        am=int(input("Enter Amount: "))
        ac=input("Enter Account No: ")
        a="Select balance from account where accountno=%s"
        data=(ac,)
        c=db.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        tam=myresult[0]-am
        sql="update account set balance=%s where accountno=%s"
        d=(tam,ac)
        c.execute(sql,d)
        db.commit()
        obj.main()


    def balance(self):
        ac=input("Enter Account No: ")
        a="Select balance from account where accountno=%s "
        data=(ac,)
        c=db.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        print("Balance Amount:",ac,"is",myresult[0])
        obj.main()

    def dispacc(self):
        ac=input("Enter Account No:")
        a="select*from account where accountno=%s"
        data=(ac,)
        c=db.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        for i in myresult:
            print(i,end=" ")
        obj.main()

    def close_account(self):
        ac=input("Enter Account No:")
        sql1="delete from account where accountno=%s"
        data=(ac,)
        c=db.cursor()
        c.execute(sql1,data)
        db.commit()
        obj.main()

    def main(self):
        print("WELCOME TO ABC BANK......")
        print("""
        1.OPEN NEW ACCOUNT
        2.DEPOSIT AMOUNT
        3.WITHDRAW AMOUNT
        4.BALANCE ENQUIRY
        5.DISPLAY CUSTOMER DETAILS
        6.CLOSE AN ACCOUNT
        7.EXIT
        """)
        choice=input("Enter Task No: ")
        while True:
            if(choice=='1'):
                obj.openacc()
            elif(choice=='2'):
                obj.deposit_Amount()
            elif(choice=='3'):
                obj.withdraw_amount()
            elif(choice=='4'):
                obj.balance()
            elif(choice=='5'):
                obj.dispacc()
            elif(choice=='6'):
                obj.close_account()
            elif(choice=='7'):
                exit()
            else:
                print("wrong choice.")
            obj.main()

obj=bank()

obj.main()