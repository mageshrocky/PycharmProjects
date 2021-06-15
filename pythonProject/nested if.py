mark = int(input('enter the mark:'))
subject = input('enter the subject:')

if mark > 90:
    if subject == 'python':
        print('good marks in python')
    else:
        print('enter the valid subject')
else:
    print('enter the mark greater than 90')