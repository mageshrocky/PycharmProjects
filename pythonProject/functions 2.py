def welcome():
    print('welcome to my bucket_list')


def bucket_list():
    welcome()
    x = 'biriyani','fried rice','grill','shawarma'
    for i in x:
        print(i)
        ask = input('eaten or not:')
        if ask == 'eaten':
            print(f'{i} is eaten')
        elif ask == 'not':
            print(f'{i} is not eaten')


bucket_list()




