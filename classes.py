## classes

class EmptyPerson:
    pass
print(EmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
       self.full_name = f'{name} {surname} ({alias})' # Propiedad pública
       self.__name = name  # Propiedad privada
     
    def get_name(self):
        return self.__name


    def walk(self):
        print(f'{self.full_name} Está caminando')

my_person = Person('Carlos', 'Mendoza')
print(my_person.full_name)
print(my_person.get_name())

my_person.walk()
my_other_person = Person('Carlos', 'Mendoza', 'CarlosDev')

print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 'Hector de león (el loco de los perror)'
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)