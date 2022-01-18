#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, 
# y luego imprima los valores asociados dentro de la lista de cada clave. 
# Por ejemplo:

# printInfo(dojo)
# # salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank   
# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    listaClaves=list(some_dict.keys())

    for x in range(0,len(listaClaves)):

        nombreClave=listaClaves[x]
        numeroElementos=len(some_dict.get(nombreClave))
        tituloMayusc=nombreClave.upper()
        print(f"{numeroElementos} {tituloMayusc}")
        
        for i in range(0,numeroElementos):
            print(some_dict.get(nombreClave)[i])

printInfo(dojo)




# Otra solución (Coding dojo)
# def print_info(dict):
#     for key,val in dict.items():
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])
# print_info(dojo)


