create_list = [i for i in range(10,50)]
print(create_list)

even_number = [i for i in range (10,50) if i %2 == 0]
print(even_number)

even_odd = [i if i%2 == 0 else 'odd' for i in range(10,20)]
print(even_odd)

my_list = [i*i for i in range(10,50)]
print(my_list)

