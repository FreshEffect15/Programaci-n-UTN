#Ejercicio 1

def comprobar_dni(dni):

    if dni.__len__() != 7 and dni.__len__() != 8:

        print("Su DNI no es válido")


    else:

        print("Su DNI es correcto")









dni = input("Ingrese su número de DNI, se comprobará si este es válido o no: ")

comprobar_dni(dni)

#Ejercicio 2

def comprobar_frase(phrase):

    final = phrase.split(" ")

    print("La palabra final de la frase es: ", final[len(final) - 1])

 




phrase = input("Ingrese una frase, se medirá la longitud de la ultima palabra: ")

comprobar_frase(phrase)

#Ejercicio 3


def comprobar_nombres(name):
    
    name_parts = name.split()

    first_name = name_parts[0]
    
    
    last_name = name_parts[-1] if len(name_parts) == 2 else f"{name_parts[1]} {name_parts[-1]}"
    return first_name, last_name


def comprobar_dni(dni):

    if len(dni) != 7 and len(dni) != 8:

        print("DNI inválido")

    else:

        print("DNI válido:", dni)

print("---------SISTEMA IDENTIFICADOR DE SOCIOS---------")

while True:

    
    complete_name = input("Ingrese su nombre completo (ingrese un nombre vacío para salir): ")

    if complete_name.strip() == "":

        print("Saliendo...")

        break
    
    dni = input("Ingrese su DNI: ")
    
    nombres, apellidos = comprobar_nombres(complete_name)

    print("Nombre:", nombres)

    print("Segundo nombre y/o apellido:", apellidos)
    
    
    comprobar_dni(dni)

    #Ejercicio 4

    def comprobar_divisibilidad(num1, num2):

     if num1 % num2 == 0:

        return True
    
     else:

        return False





num1 = int(input("Ingrese un primer número: "))

num2 = int(input("Ingrese un segundo número: "))

if comprobar_divisibilidad(num1, num2) == True:

    print("El primero es múltiplo del segundo")

else:

    print("El primero NO es múltiplo del segundo")

#Ejercicio 5

def temperatura(maxi, mini):

    return (maxi + mini) / 2



days = int(input("Ingrese la cantidad de dias que quiere ingresar: "))

for i in range (0, days, 1):

 maxi = int(input("Ingrese la temperatura máxima del día: "))

 mini = int(input("Ingrese la temperatura mínima: "))

 print("La temperatura media es: ", temperatura(maxi, mini))

#Ejercicio 6

def agregar_espacio(phrase):

 final = ""

 for i in phrase:
  
  final += i + " "

 return final






phrase = input("Ingrese una frase: ")

print(agregar_espacio(phrase))

#Ejercicio 7

def crear_lista():

 list_num = []

 while True:
  
  num = int(input("Ingrese número para la lista, ingrese 0 para salir: "))

  if num != 0:

   list_num.append(num)

  else:
   
   return list_num


def comprobar(list_num):
 
 high = 0

 low = list_num[0]


 for i in list_num:
  
  if i > high:
   
   high = i

  if i < low:
   
   low = i

 return high, low




list_num = crear_lista()

high, low = comprobar(list_num)

print("El mayor es: ", high)

print("El menor es: ", low)

#Ejercicio 8


import math




def calcular_circunferencia(radio):

 perimeter = radio * 2 * math.pi

 area = math.pi * (radio ** 2)

 return perimeter, area



radio = int(input("Ingrese el radio de la circunferencia: "))


calcular_circunferencia(radio)

perimeter, area = calcular_circunferencia(radio)

print("El perimetro de su circunferencia es de: ", perimeter)

print("El area de su circunferencia es de: ", area)


#Ejercicio 9

def login(user_name, password, chances):

    
 if user_name == "usuario1" and password == "asdasd":
  
  return True

 else:
  
  chances -= 1

  print("Error, le quedan ", chances, " intentos")

  return False, chances


  



print("---INGRESE A SU CUENTA---")

chances = 3

correct = False

while chances != 0 and correct == False:

 user_name = input("Ingrese su nombre de usuario: ")

 password = input("Ingrese su contraseña: ")

 correct, chances = login(user_name, password, chances)


if correct == True:
 
 print("HA INGRESADO AL SISTEMA CORRECTAMENTE")

else:
 
 print("ERROR, NO HA PODIDO INGRESAR AL SISTEMA")

#Ejercicio 10

def aplicar_descuento(dic_products, percent):

 total = 0  

 for producto, precio in dic_products.items():

        descuento = (precio * percent) / 100  

        discount_price = precio - descuento  
        
        total += discount_price

 return total
        









percent = int(input("Ingrese el porcentaje de descuento que desea aplicar: "))



dic_products = {

    "Doritos": 700,
    "Pepsi": 300,
    "Mondongo": 100

}

final_price = aplicar_descuento(dic_products, percent)

print("El precio final de su compra es de: ", final_price)

#Ejercicio 11

def aplicar_funcion_a_lista(funcion, lista):
    
    
    resultados = list(map(funcion, lista))

    return resultados


def duplicar(numero):

    return numero * 2


numeros = [1, 2, 3, 4, 5]


resultados = aplicar_funcion_a_lista(duplicar, numeros)


print(resultados)  

    
 #Ejercicio 12

def transformar_frase(phrase):

   words = phrase.split()

   dic = {}

   for i in words:
      
      i = i.strip(' ')

      dic[i] = len(i)

   return dic



phrase = input("Ingrese una frase: ")


dic = transformar_frase(phrase)

print(dic)

#Ejercicio 13

def modulo_vector(vector):
   
    suma_cuadrados = sum(component ** 2 for component in vector)

    module = math.sqrt(suma_cuadrados)

    return module


vector = []

limit = int(input("Ingrese la longitud del arreglo: "))

for i in range(0, limit, 1):

    num = int(input("Ingrese un numero para agregarle al vector: "))

    vector.append(num)

module = modulo_vector(vector)

print("El modulo del vector es: ", module )

#Ejercicio 14

def comprobar_primo(num):

    primeB = True  

    if num <= 1:

        primeB = False  

    else:

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:

                primeB = False  
                
                break

    return primeB

num = int(input("Ingrese un número: "))

prime = comprobar_primo(num)

if prime:

    print("Usted ingresó un número primo")

else:

    print("Usted no ingresó un número primo")

#Ejercicio 15

def factorial(num):

    if num == 0:

        return 1
    
    else:

        return num * factorial(num - 1)


cont = 0

while True:

    num = int(input("Ingrese un número, se mostrará el factorial de este (0 para salir): "))

    cont += 1

    if num == 0:

        break

    else:

        fact = factorial(num)

        print("El factorial es: ", fact)

        break


print("Cantidad de numeros ingresados: ", cont)

#Ejercicio 16

def calcular_frecuencia(num, digits):
    
    numero_str = str(num)

    digito_str = str(digits)

    frequency = 0
    
    for d in numero_str:
        
        if d == digito_str:
            
            frequency += 1  
    
    return frequency


num = int(input("Ingrese un número entero: "))

digits = int(input("Ingrese un dígito: "))

frecuencia = calcular_frecuencia(num, digits)

print("Frecuencia:", frecuencia)

#Ejercicio 17

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def suma_de_digitos(numero):
    total = 0
    while numero > 0:
        total += numero % 10
        numero //= 10
    return total

def calcular_frecuencia(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    frecuencia = numero_str.count(digito_str)
    return frecuencia

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

mayor_number = 0


while True:

        number = int(input("Ingrese un número primo (o uno no primo para salir): "))

        if not es_primo(number):

            break

        if number > mayor_number:

            mayor_number = number

        suma = suma_de_digitos(number)

        print(f"Suma de dígitos del número {number}: {suma}")

        digito = int(input("Ingrese un dígito: "))

        frecuencia = calcular_frecuencia(number, digito)

        print(f"Frecuencia del dígito {digito} en el número {number}: {frecuencia}")



if mayor_number > 0:

    fact = factorial(mayor_number)

    print(f"Factorial del mayor número ingresado ({mayor_number}): {fact}")

else:
    
    print("No se ingresaron números primos.")