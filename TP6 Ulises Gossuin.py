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

goals = [
    [0, 1, 2, 1, 0, 3, 1, 2, 4, 0],
    [1, 0, 2, 1, 0, 2, 1, 3, 2, 1],
    [2, 2, 0, 2, 1, 0, 1, 1, 3, 1],
    [1, 1, 2, 0, 0, 2, 0, 1, 2, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 1],
    [3, 2, 0, 2, 1, 0, 2, 1, 4, 0],
    [1, 1, 1, 0, 0, 2, 0, 1, 2, 0],
    [2, 3, 1, 1, 0, 1, 1, 0, 2, 1],
    [4, 2, 3, 2, 2, 4, 2, 2, 0, 2],
    [0, 1, 1, 0, 1, 0, 0, 1, 2, 0]
]

n = len(goals)
wins = [0] * n
ties = [0] * n
loses = [0] * n
favor_goals = [0] * n
against_goals = [0] * n
points = [0] * n

for i in range(n):

    for j in range(n):

        if i != j:

            goals_team_i = goals[i][j]
            goals_team_j = goals[j][i]

            favor_goals[i] += goals_team_i
            against_goals[i] += goals_team_j

            if goals_team_i > goals_team_j:

                wins[i] += 1
                points[i] += 3

            elif goals_team_i < goals_team_j:

                loses[i] += 1

            else:

                ties[i] += 1

for i in range(n):

    print("Equipo:", i + 1)
    print("Triunfos:", wins[i])
    print("Empates:", ties[i])
    print("Derrotas:", loses[i])
    print("Goles a favor:", favor_goals[i])
    print("Goles en contra:", against_goals[i])
    print("Diferencia de goles:", (favor_goals[i] - against_goals[i]))
    print("Puntos:", points[i])
   
#Ejercicio 9

import random
import sys

a=0
b=0
c=0
d=0
e1 = 0
f = 0
m = [['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X']]

n = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]

o = '-'
p = 5

def g():
    v()
    print('A')

    a = int(input('Ingresa un valor en la horizontal X: '))

    if a > 5:

        print('ERROR, INGRESE UN NÚMERO MENOR A 5')

        g()

    b = int(input('Ingresa un valor en la vertical Y: '))
    if b > 5:
        print('ERROR, INGRESE UN NÚMERO MENOR A 5')
        g()

    m[a][b] = n[a][b]

    v()

    c = int(input('Ingresa un valor en la horizontal: '))

    if c > 5:
        print('ERROR, INGRESE UN NÚMERO MENOR A 5')
        m[a][b] = '-'
        g()
    else:
        d = int(input('Ingresa un valor en la vertical: '))
        if d > 5:
            print('ERROR, INGRESE UN NÚMERO MENOR A 5')
            m[a][b] = '-'
            g()

        m[c][d] = n[c][d]

        q(a,b,c,d)

        v()

def i():
    v()
    print('B')

    a = int(input('Ingresa un valor en la horizontal: '))
    if a > 5:
        print('ERROR, INGRESE UN NÚMERO MENOR A 5')
        i()

    b = int(input('Ingresa un valor en la vertical: '))
    if b > 5:
        print('ERROR, INGRESE UN NÚMERO MENOR A 5')
        i()

    m[a][b] = n[a][b]

    v()

    c = int(input('Ingresa un valor en la horizontal: '))
    if c > 5:
        print('ERROR, INGRESE UN NÚMERO MENOR A 5')
        m[a][b] = '-'
        i()
    else:
        d = int(input('Ingresa un valor en la vertical: '))
        if d > 5:
            print('ERROR, INGRESE UN NÚMERO MENOR A 5')
            m[a][b] = '-'
            i()

        m[c][d] = n[c][d]

        r(a,b,c,d)

        v()

def q(a,b,c,d):
    global e1
    if m[a][b] != m[c][d]:
        m[c][d] = "-"
        m[a][b] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))

        if respuesta == 's':
            i()
        elif respuesta == 'n':

            print('El jugador tiene',e1,'pares')
            print('El jugador tiene',f,'pares')
            if e1 > f:

                print('El ganador fue el jugador A')

            elif f > e1:

                print('El ganador fue el jugador B')

            elif f == e1:

                print('Fue un empate!')
                
            elif e1 == f:

                print('Fue un empate!')
            sys.exit()
    else:
        e1 += 1 
        g()

def r(a,b,c,d):
    global f
    if m[a][b] != m[c][d]:
        m[c][d] = "-"
        m[a][b] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))
        if respuesta == 's':
            g()

        elif respuesta == 'n':
            print(e1)
            print(f)
            if e1 > f:
                print('El jugador tiene',e1,'pares')
            elif f > e1:
                print('El jugador tiene',f,'pares')
            elif f == e1:
                print('Fue un empate!')
            elif e1 == f:
                print('Fue un empate!')
            sys.exit()
    else:
        f += 1
        i()

def v():
    contador = 0
    print('  0 1 2 3 4 5 \n')

    for a in range(6):
        print(contador, '', end = '')
        contador += 1
        for b in range(6):
            print((m[a][b]),'', end = '')

        print('\n')

def main():
    while p == 5:
        random.shuffle(n)
        for a in n:
            random.shuffle(a)
        g()

main()

#Ejercicio 10

def obtener_diagonales(matrix):

    dimension = len(matrix)

    principal_diagonal = []

    inverse_diagonal = []

    for i in range(dimension):

        principal_diagonal.append(matrix[i][i])

        inverse_diagonal.append(matrix[i][dimension - 1 - i])

    return principal_diagonal, inverse_diagonal


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

principal_diagonal, inverse_diagonal = obtener_diagonales(matrix)

print("Diagonal Principal:", principal_diagonal)

print("Diagonal Inversa:", inverse_diagonal)

#Ejercicio 11

divise_dic = {'euro': '€', 'dollar': '$', 'yen': '¥'}



divise = input("Ingresa una divisa: ").lower()




if divise in divise_dic:

    simbol = divise_dic[divise]

    print("El símbolo de ", divise, " es ", simbol)

else:

    print("La divisa ", divise, " no está en el diccionario")

#Ejercicio 12

name = input("Ingresa tu nombre: ")

age = input("Ingresa tu edad: ")

address = input("Ingresa tu dirección: ")

phone_number = input("Ingresa tu número de teléfono: ")

user_information = {
    
    'name': name,
    'age': age,
    'address': address,
    'phone_number': phone_number
}

message = f"{user_information['name']} tiene {user_information['age']} años, vive en {user_information['address']} y su número de teléfono es {user_information['phone_number']}."

print(message)

#Ejercicio 13

fruit_price = {

    'manzana': 1.2,
    'banana': 0.8,
    'uva': 2.5,
    'pera': 1.0,
    'naranja': 1.5
}


fruit = input("Ingresa el nombre de la fruta: ").lower()
weight = float(input("Ingresa la cantidad en kilos: "))


if fruit in fruit_price:

    precio_total = fruit_price[fruit] * weight

    print("El precio de ", weight, " kilos de ", fruit, " es $", precio_total)
else:

    print("la fruta ",  fruit, " no está en la lista de precios.")




