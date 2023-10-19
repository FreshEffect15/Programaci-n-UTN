#Ejercicio 1

def bubble_sort(list):
 
 for i in range(0, len(list)):
  
  for j in range(0, len(list) - 1):
   
   if list[j] > list[j+1]:

    aux = list[j]

    list[j] = list[j+1]

    list[j+1] = aux

 return list

list = []

amount = int(input("Ingrese la cantidad de números que quiere que tenga el arreglo: "))

for i in range(0, amount):

 print("Ingrese el número para la posición ", (i+1) , ": ")

 num = int(input())

 list.append(num)


sorted_list = bubble_sort(list)

print("La lista ordenada es:", sorted_list)

#Ejercicio 2

def selection_sort(list):

 for i in range(0, len(list)):
  
  min = i

  for j in range (i+1, len(list)):

   if list[min] > list[j]:
    
    min = j

  aux = list[i]

  list[i] = list[min]

  list[min] = aux

 return list

list = []

amount = int(input("Ingrese la cantidad de palabras para el arreglo: "))

for i in range(0, amount):
 
 print("Ingrese el número para la posición: ", 1 )

 word = input()

 list.append(word)

sorted_list = (selection_sort(list))

print("La lista ordenada quedaría como: ", sorted_list)

#Ejercicio 3

libros = [
    {
        'Titulo': 'Moby Dick',
        'Autor': 'Herman Melville',
        'Año': '1851'
    },
    {
        'Titulo': 'Tom Sawyer',
        'Autor': 'Mark Twain',
        'Año': '1876'
    },
    {
        'Titulo': 'Corazón Delator',
        'Autor': 'Edgar Allan Poe',
        'Año': '1843'
    }
]

order = input("Ingrese la función por la que desea ordenar la lista (Título, Autor, Año): ").lower()

if order == "título":
    
    field = 'Titulo'

elif order == "autor":
    
    field = 'Autor'

elif order == "año":
    
    field = 'Año'
else:
    print("Función no válida. Elija entre 'Título', 'Autor' o 'Año'.")

    field = None

if field is not None:
    
    n = len(libros)

    for i in range(n):
        
        min_index = i

        for j in range(i + 1, n):
            
            if libros[j][field] < libros[min_index][field]:
                
                min_index = j

        libros[i], libros[min_index] = libros[min_index], libros[i]

    print("Lista de libros ordenada:")

    for libro in libros:
        
        print(f'Título: {libro["Titulo"]}, Autor: {libro["Autor"]}, Año: {libro["Año"]}')

#Ejercicio 4

def bubble_sort(list):
 
 for i in range(0, len(list)):
  
  for j in range(0, len(list) - 1):
   
   if list[j] < list[j+1]:

    aux = list[j]

    list[j] = list[j+1]

    list[j+1] = aux

 return list

list = []

amount = int(input("Ingrese la cantidad de números que quiere que tenga el arreglo: "))

for i in range(0, amount):

 print("Ingrese el número para la posición ", (i+1) , ": ")

 num = int(input())

 list.append(num)


sorted_list = bubble_sort(list)

print("La lista ordenada es:", sorted_list)

#Ejercicio 6

def counting_sort(list, amount):
 
 maxi = max(list)


 count = [0] * (maxi + 1)

 for i in list:

  count[i] += 1

 sorted_list = []

 for i in range(maxi + 1):
 
  sorted_list.extend([i] * count[i] )

 return sorted_list





list = []

amount = int(input("Ingrese la cantidad de números que quiere que tenga el arreglo: "))

for i in range(0, amount):

 print("Ingrese el número para la posición ", (i+1) , ": ")

 num = int(input())

 list.append(num)

print("La lista ordenada sería: ", counting_sort(list, amount))

#Ejercicio 7


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