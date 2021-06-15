import re
def n():
    name = input('enter your name:')
    try:
        if re.match(r'^[A-Z]{1}[a-z]{2,20}$',name):
            print(name)

        else:
            raise
    except:
        print('please Enter valid name')
        n()

n()

def an(accn):
    count= 10101
    count += accn
    return accn
accn = an(accn= int(input('entr numbr:')))
an(accn)


