# Functions

def my_function ():
    print('Esto es una función')

my_function()
my_function()
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(5879, 2554)
sum_two_values('5', '7')
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum
my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname='Mendoza', name='Carlos')

def print_name_with_default(name, surname, alias='Sin alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Carlos', 'Mendoza')
print_name_with_default('Carlos', 'Mendoza', 'CarlosDev')


def print_texts(*texts):
   for text in texts:
       print(text)

print_texts('Hola', 'Python', 'CarlosDev')
print_texts('Hola')

def print_upper_texts(*texts):
   for text in texts:
       print(text.upper())

print_upper_texts('Hola', 'Python', 'CarlosDev')
print_upper_texts('Hola')

