
#Ejercicio 1

word = input("Ingrese una palabra: ")

for k in range(10):

 print(word)

#Ejercicio 2

age = int(input("Ingrese su edad: "))

for i in range(age):

    print(i + 1)

#Ejercicio 3

num = int(input("Ingrese un número entero positivo: "))

for i in range(num):

 if (i % 2 != 0):
  
  print(i, end= ", " )

#Ejercicio 4

num = int(input("Ingrese un número positivo: "))

for i in range(num, -1, -1):

 print(i, end=", ")

#Ejercicio 5

inv = int(input("Ingrese la cantidad que inversinó: "))

anual_interest = int(input("Ingrese su interés anual en $: "))

years = int(input("Ingrese la cantidad de años que durará la inversión: "))

for i in range(years):

    inv = inv + anual_interest;

    print("Su inversión generó: ", anual_interest )

    print("---------------------------")

print("El dinero total que recaudó con esa inversión fue de: ", inv)

#Ejercicio 6

num= int(input("Ingrese un número entero: "))

for i in range(1, num + 1):
        
  print('*' * i)

#Ejercicio 7

print("TABLAS DE MULTIPLICAR: ")

for i in range(11):
 
   for j in range(11):
  
    print(i, " x ", j ," = ", i*j)


   print("--------------")

#Ejercicio 8

num = int(input("Ingrese un número entero: "))

num_impares = num if num % 2 != 0 else num - 1

for i in range(num_impares, 0, -2):
 
 for j in range(i, num_impares + 1, 2):
     
     print(j, end=" ")
     
 print()

 #Ejercicio 9

 
password = input("Ingrese una contraseña, esta se guardara y tendra que ingresarla después: ")
exit = False

while exit == False:

 tried = input("Ingrese su contraseña: ")

 if(tried != password):
  
  print("Su contraseña es incorrecta, intentalo nuevamente")

 elif(tried == password):
   
      exit = True

print("Ha accedido al sistema")

#Ejercicio 10

num = int(input("Ingrese un número entero: "))

primo = True

for i in range(2, int(num**0.5) + 1):
  
    if num % i == 0:

      primo = False
      
if (primo == True):

 print("El número ingresado es primo")

else:

 print("El número ingresado no es primo")


 #Ejercicio 11

word = input("Ingrese una palabra: ")

final = " "

lenght = word.__len__()

for i in range(lenght, 0, -1):

  final = final + word[i - 1] 

print(final)

#Ejercicio 12

word = input("Ingrese una palabra: ").lower()

char = input("Ingrese una letra: ")

cont = 0


for i in word:
    
    if ( i == char):
        
        cont += 1


print("La cantidad de veces que se encontro esa letra es: ", cont)


#Ejercicio 13

word = input("Ingrese una palabra: ").lower()


while word != "salir":
    
    print("ECO: ", word)

    word = input("Ingrese una palabra nuevamente, si introduce (salir) saldrá: ").lower()

#Ejercicio 14

num1 = int(input("Ingrese un número: "))

num2 = int(input("Ingrese un segundo número, más grande que el anterior: "))


if (num1 > num2):

    print("Error, números mal ingresados")

else:

    for i in range(num1, num2, +1):

        if i % 2 == 0:

            print(i)
            print("Es par")
            print("------------------")

        elif i % 2 == 1:

            print(i)
            print("Es inpar")
            print("------------------")

#Ejercicio 15

num1 = int(input("Ingrese un número, entero, mayor que 0: "))

if num1 == 0 or num1 < 0:

  print("Ingrese un número válido")

else:

  for i in range(1, num1, +1):

    if num1 % i == 0:

      print("Divisor: ", i)

print("Divisor: ", num1)

#Ejercicio 16

amount = int(input("Ingrese la cantidad de números que quiere ingresar, se contarán los negativos: "))

neg = 0

for i in range(0, amount, +1):

 num = int(input("Ingrese un número: "))

 if num < 0:

  neg += 1

print("Negativos: ", neg ) 

#Ejercicio 17

phrase = input("Ingrese una frase, se hará un listado de todas las vocales que aparecen: ")

a = False

e = False

iv = False

o = False

u = False


for i in phrase:


    if i == "a":

      a = True
    
    if i == "e":

      e = True
    
    if i == "i":

      iv = True
    
    if i == "o":
      o = True
    
    if i == "u":

      u = True

if a == True:
 print("Contiene A")

if e == True:
 print("Contiene E")

if iv == True:
 print("Contiene I")

if o == True:
 print("Contiene O")

if u == True:
 print("Contiene U")

#Ejercicio 18

fibo = [0, 1]

for i in range(2, 10):
    next = fibo[i - 1] + fibo[i - 2]
    fibo.append(next)
   

for numero in fibo:
    print(numero)

#Ejercicio 19

destiny = int(input("Ingrese una cantidad destino para su alcancia: "))

num = 0

sum = 0

print("Tope: ", destiny)


if destiny < 0:

    print("Error, se ingresó un número negativo")

else:

 while sum < destiny:


    num = int(input("Ingrese el dinero a ingresar: " ))

    if num < 0:
       
       print("Error, número negativo, ingrese un número válido")

    else:

       sum = sum + num


print("Alcanzo el límite, ", destiny)

#Ejercicio 20

num = 0

sum = 0

salir = False

while salir != True:

    num = int(input("Ingrese un número, ingrese 0 para salir: "))

    if num == 0:

        salir = True

    else:

        sum = num + sum

print("La suma de todos los números es de: ", sum)

#Ejercicio 21

num = 0

high = 0

salir = False

while salir != True:

    num = int(input("Ingrese un número, ingrese 0 para salir: "))

    if num == 0:

        salir = True

    else:

        if num > high:

            high = num

print("El mayor de todos los números que ingresó es: ", high)

#Ejercicio 22

num = 0

salir = False

digits = 0

pares = 0

while salir != True:

    num = int(input("Ingrese un número, ingrese -1 para salir: "))

    if num == -1:

        salir = True

    else:

        num_str = str(num)

        if num_str.__len__() == 1:

            print("Su número no se puede sumar por que solo tiene una cifra, ", num )

        else:

         for i in num_str:

            digits = int(i) + digits

        print("La suma de los dígitos: ", digits)

        digits = 0

        if num % 2 == 0:
           
           pares+=1






print("La cantidad los números pares que ingresó es: ", pares)

#Ejercicio 23

salir = False

while salir != True:

 amount = int(input("Ingrese el monto de sus compras, ingrese 0 para salir: "))

 if amount == 0:
  
  salir = True

print("Saliendo del programa")

#Ejercicio 24

salir = False

sum = 0

while salir != True:

 amount = int(input("Ingrese el monto de sus compras, ingrese 0 para salir: "))

 if amount < 0:
  
  print("Error, ingrese un número válido")

 else:
  
  if amount == 0:
  
   salir = True

  else:
   
   sum = amount + sum

print("El total es de: ", sum)


if sum > 1000:
 
 print("Más de 1000, se aplica descuento del 10%")

 off = 0.10 * sum

 print("Su precio final con descuento es: ", sum - off)

#Ejercicio 25

num = int(input("Ingrese un número: ")) 

if num < 0:
    print("El factorial no está definido para números negativos.")

elif num == 0:

    print("El factorial de 0 es 1.")

else:

    factorial = 1

    for i in range(1, num + 1):

        factorial *= i

    print("El factorial de ", num, " es ", factorial)