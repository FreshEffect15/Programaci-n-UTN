def bubble_sort(arr, amount):

    print("-------------------")

    print("BUBBLE SORT")

    for j in range(amount):

        for i in range(amount - 1):

            if arr[i] > arr[i + 1]:

                temp = arr[i]

                arr[i] = arr[i + 1]

                arr[i + 1] = temp

    print("La lista quedó como:")

    for i in range(amount):
    
     print(list[i], "  \n")

def selection_sort(arr, amount):

    print("--------------------")

    print("SELECTION SORT")

    for i in range(amount):

        min_index = i

        for j in range(i + 1, amount):

            if arr[j] < arr[min_index]:

                min_index = j

        temp = arr[i]

        arr[i] = arr[min_index]

        arr[min_index] = temp

    print("La lista quedó como:")

    for i in range(amount):
    
      print(list[i], "  \n")

def insert_sort(arr, amount):

    print("--------------------------")

    print("INSERT SORT")

    for i in range(1, amount):

        x = arr[i]

        j = i - 1

        while j >= 0 and x < arr[j]:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = x

        print("La lista quedó como:")

        for i in range(amount):
    
          print(list[i], "  \n")

def lineal_search(arr, amount, target):

    print("LINEAL SEARCH")

    for i in arr:

        if i == target:

            print("Se ha encontrado el elemento que ha estado buscando...")

def binary_search(arr, amount, target):

    print("BINARY SEARCH")

    left  = 0 

    right = amount - 1

    while left <= right:

        mid = (left + right) 

        if arr[mid] == target:

            print("Se encontró el elemento")
          
        elif arr[mid] < target:

            left = mid + 1

        else:

            right = mid - 1




list = []

amount = int(input("Ingrese la cantidad de números para el arreglo: "))

for i in range(amount):

    print("Ingrese el número para la posición:", i + 1)

    num = int(input())

    list.append(num)

print("ORDENAMIENTOS")

bubble_sort(list, amount)

selection_sort(list, amount)

insert_sort(list, amount)

print("BUSQUEDAS")

target = int(input("Ingrese el valor que quiere buscar"))

lineal_search(list, amount, target)

print("Solo si ingresó una lista ordenada, la lista binaria se realizara correctamente")

binary_search(list, amount, target)



