import pymysql

#db = pymysql.connect(host='localhost', user='root', passwd='', database='sample')
db1 = pymysql.connect(host='localhost', user='root', passwd='', database='magesh')

x = db1.cursor()
x.execute('use magesh')
try:
    x.execute('create table demo(name varchar(30),age int)')

except Exception as e:
    print(e)

name = input('enter your name:')
age = int(input('enter your age:'))

x.execute('INSERT INTO demo(name,age)VALUES(%s,%s)', (name, age))
db1.commit()
x.execute('select * from demo')
c = x.fetchall()
print(type(c))
db1.close()
