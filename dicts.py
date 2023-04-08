## Dictionaries

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Carlos', 'Apellido':'Mendoza', 'Edad':30, 1:'Python'}

my_dict = {'Nombre':'Carlos', 
           'Apellido':'Mendoza', 
           'Edad':30, 
           'Lenduajes':{'Python', 'Swift', 'Kotlin'},
           1:1.80
           }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))


print(my_dict['Nombre'])

my_dict['Nombre'] = 'Lucas'
print(my_dict['Nombre'])

my_dict['Calle'] = 'El banquito'
print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Mendoza' in my_dict)
print('Mendoz' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = ['Nombre', 1, 'Piso']
print(my_new_dict)
my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))


print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, 'CarlosDev')
print(my_new_dict)

print(list(my_new_dict))



