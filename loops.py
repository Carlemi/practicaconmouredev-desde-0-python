###  Loops

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  #Es opcional
    print('Mi condición es mayor o igual que 10')
print('La ejecución continúa')


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('se detiene la ejecución')
        break
    print(my_condition)

print('La ejecución continúa')

# For

my_list = [30, 24, 62, 52, 35, 35, 17] 

for element in my_list:
    print(element)


my_tuple = (30, 1.80, 'Carlos', 'Mendoza')

for element in my_tuple:
    print(element)

my_set = {'Carlos', 'Mendoza', 30}
for element in my_set:
    print(element)

my_dict = {'Nombre':'Carlos', 'Apellido':'Mendoza', 'Edad':30, 1:'Python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('El bucle for para diccionario ha finalizado')

print('La ejecución continúa')