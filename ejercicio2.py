#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista estudiantes
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        print(f"first_name - {some_list[i]['first_name']}, last_name - {some_list[i]['last_name']}")

iterateDictionary(estudiantes) 

