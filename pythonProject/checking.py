import re
def val():
    name2 = input('enter the name:')
    name = re.compile(r'^[A-Z]{1}[a-z]{2,20}')
    res = name.search(name2)
    try:
        if res:
            return name2
        else:
            raise
    except Exception as e:
        print('invalid')

val()



