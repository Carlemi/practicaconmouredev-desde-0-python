### conditionals

'''edad1 = 20
edad2 = 21

if edad1 >= edad2:
    print('Sí es mayor!')
else:
    print('no, la edad es menor')  ##esto es prueba para el commit'''   

my_condition = False

if my_condition: #Es lo mismo que if my_condition == True:
    print('se ejecuta la condición del if')

print('La ejecución continúa')


my_condition = 5 * 5

if my_condition == 10: 
    print('Se ejecuta la segunda condición del segundo if')

if my_condition > 10 and my_condition < 20: 
    print('Es mayor que 10 y menor que 20')

elif my_condition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20')

print('La ejecución continúa')

my_string = ''

if not my_string:
    print('Mi cadena de texto  es vacía')

if my_string == 'Mi cadena de textooooo':
    print('Estas cadenas de texto coinciden')