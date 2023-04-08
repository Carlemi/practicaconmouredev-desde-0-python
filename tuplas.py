## Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.80, 'Carlos', 'Mendoza')

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Carlos'))
print(my_tuple.index('Carlos'))

## my_tuple[1] = 1.90  'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[1] = 'Azul'
my_tuple.insert(3, 'verde')
my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple 
# print(my_tuple) NameError: name 'my_tuple' is not defined