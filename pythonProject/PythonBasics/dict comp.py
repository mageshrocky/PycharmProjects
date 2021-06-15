even = {i:'even' for i in range(10, 50) if i %2 == 0}
print(even)

even_odd = {i:'even' if i %2 == 0 else 'odd' for i in range(10, 50)}
print(even_odd)