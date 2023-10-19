#Ejercicio 1

num_list = []

while True:

 num = int(input("Ingrese un número para meter a la lista: "))

 if num != 0:

  num_list.append(num)

  print("Numero ingresado a la lista")

 else:

  print("Saliendo del programa...")

  break
 
print("--------------")

count = 1

for i in num_list:
 
 print("Casilla ", count, " = ", i )

 count += 1

#Ejercicio 2

while True:

    num_to_remove = int(input("Ingrese un número para eliminar de la lista: "))

    if num_to_remove in num_list:

        num_list.remove(num_to_remove)

        print(f"Se eliminó la primera ocurrencia de ", num_to_remove,  " de la lista.")

        break

    else:

        print(num_to_remove, " no se encuentra en la lista. Intente de nuevo.")



print("--------------------------")
print("Lista actualizada:")

count = 1

for i in num_list:

    print("Casilla ", count, " = ", i)

    count += 1


#Ejercicio 3
print("--------------------------------------------------")
print("SUMATORIA DE TODOS LOS NÚMEROS DE LA LISTA")

sumatory = 0

for i in num_list:
   
   sumatory += i



print("La suma de todos los nùmeros ingresados es: ", sumatory)



#Ejercicio 4

num_list_minor = []

num_limit = int(input("Ingrese un número, se incluiran en otro arreglo todos los números menores a este en la lista:  "))

for i in num_list:
   
   if i < num_limit:
      
     num_list_minor.append(i)


print("----------------------------------------------------")
print("Lista final")


count = 1

for i in num_list_minor:
   
   print("Casilla ", count, " = ", i )

   count += 1




#Ejercicio 5
print("----------------------------------")
print("Volviendo la lista en una tupla")


num_count_tuple = []

for i in num_list:
   
   count = num_list.count(i)

   num_count_tuple.append((i, count))


count = 1

for i in num_count_tuple:
   
   print("Casilla ", count, " = ", i)

   count += 1

#Ejercicio 6

primary = []

secondary = []

while True:

    primary_names = input("Ingrese el nombre de pila de los alumnos de primaria: (X para salir) ")

    primary_names = primary_names.lower()

    if primary_names == "x":

        print("Terminando de ingresar nombres de primaria...")

        break

    else:

        print("Nombre ingresado...")

        primary.append(primary_names)
 


while True:

    secondary_names = input("Ingrese el nombre de pila de los alumnos de secundaria: (X para salir) ")

    secondary_names = secondary_names.lower()

    if secondary_names == "x":

        print("Terminando de ingresar nombres de secudaria...")

        break

    else:

        print("Nombre ingresado...")

        secondary.append(secondary_names)
    
print("------------------------------------")

all_names = set(primary).union(set(secondary))

print("Todos los nombres de alumnos sin repeticiones: ", all_names)

repeated_names = set(primary).intersection(set(secondary))

print("Los nombres que ser repiten entre el nivel secundario y primario son: ", repeated_names)

no_repeated_names = set(primary).difference(set(secondary))

print("Los nombres de nivel primario que no se repiten en el secundario son: ", no_repeated_names)

#Ejercicio 7

names_list = []

count = 1

string_count = {}

while True:

    print("Cadena número ", count)

    names = input("Ingrese cadena de texto: (A las 50 parará) ")

    count += 1

    names_list.append(names)   

    if count == 51:

        print("Terminando de ingresar nombres...")

        break

for i in names_list:

    for j in i:

        string_count[j] = string_count.get(j, 0) + 1

for char, count_char in string_count.items():

    print("Caracter: ", char, " Veces que aparece: ", count_char)


#Ejercicio 8

def sort_list(list, amount):

 numbers = [x for x in list if isinstance(x, int)]

 words = [x for x in list if isinstance(x, str)]

 numbers.sort()

 words.sort()

 sorted_list = numbers + words

 return sorted_list



list = []


amount = int(input("Ingrese el tamaño del array: "))

for i in range(0, amount):

    value = input("Ingrese el valor en su arreglo (puede ser una cadena o un número): ")

    list.append(value)


print("La lista ordenada quedaría como: ", sort_list(list, amount))

#Ejercicio 9

def sorted_list(list, amount):

 if amount < 1:

    return list
 
 middle = amount // 2

 left = list[:middle]

 right = list[middle:]

 return merge(left, right)







def merge(left, right):

 result = []

 i = j = 0

 while i < len(left) and j < len(right):
   
   if left[i] < right[j]:
     
     result.append(left[j])

     i += 1

   else:
     
     result.append(left[j])

     j += 1

 result.extend(left[i:])
 result.extend(right[j:])

 return result




list = []

amount = int(input("Ingrese el tamaño del array: "))

for i in range(1, amount):

    value = input("Ingrese el número en su arreglo: ")

    list.append(value)


print("La lista ordenada quedaría como: ", sorted_list(list, amount))