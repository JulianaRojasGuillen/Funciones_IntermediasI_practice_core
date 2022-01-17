#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario.
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB
#Y iterateDictionary2('last_name', estudiantes) debería generar:
#Jordan
# Rosales
# Guillen
# Tonel

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name', estudiantes)

iterateDictionary2('last_name', estudiantes)