
#Ejercicio 1

anios = int(input("Ingrese la cantidad de años que tiene su computadora: "))

if (anios <= 2):
    print("Su computadora es nueva")

else:

    print("Su computadora es vieja, tiene más de 2 años")   


#Ejercicio 2    

anios = int(input("Ingrese la cantidad de años que tiene su computadora: "))

if (anios <= 2):
    print("Su computadora es nueva")


elif(anios < 0):

    print("Su número ingresado es negativo")


else:

    print("Su computadora es vieja, tiene más de 2 años")   


#Ejercicio 3
 
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

if (nombre1[0] == nombre2[0]):

   print("Coincidencia")

else: 

    print("No hay coincidencia")


#Ejercicio 4

respuesta = input("Ingrese uno de los 3 candidatos para votar(A, B, C): ")

respuesta = respuesta.lower()

if(respuesta == 'a'):

    print("Usted ha votado al partido rojo")

elif(respuesta == "b"):

    print("Usted ha votado al partido de la verdad") 

elif(respuesta == "c"):

    print("Usted ha votado al partido azul")
else:
    print("Opción errónea")

#Ejercicio 5    

letra = input("Ingrese una letra: ")


if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
 
     print("Su letra ingresada es una vocal")    
elif(len(letra) > 0):
     
     print("Ingrese una letra, no un String")

#Ejercicio 6

anio = int(input("Ingrese un año: "))

if(anio % 4 == 0 and anio % 100 != 0):

  print("Es un año biciesto")

elif(anio % 100 == 0 and anio % 400 == 0):

  print("Es un año biciesto")

else:

  print("No es un año biciesto")  

  #Ejercicio 7

  numero1 = int(input("Ingrese el primer número: "))

numero2 = int(input("Ingrese el segundo número: "))

numero3 = int(input("Ingrese el tercer número: "))

menor = numero1

if(menor > numero2):

    menor = numero2

if (menor > numero3):

    menor = numero3

print("El menor es: ", menor )

 #Ejercicio 8

nombre = input("Ingrese su nombre: ")
contrasenia = input("Ingrese su contraseña: ")

if (nombre == "Gwenevere" and contrasenia == "excalibur"):

  print("Usuario y contraseña correctos, puede ingresar a Camelot")

else:

  print("Acceso denegado")

#Ejercicio 9

nombre = input("Ingrese la letra de su nombre: ")

if (nombre < "m"):
 
 print("Usted pertenece al grupo de las mujeres")
 
elif(nombre > "n"):

 print("Usted pertenece al grupo de los hombres")

#Ejercicio 10

edad = int(input("Ingrese la edad del cliente: "))

if(edad < 4):

    print("Puede entrar gratis")

elif(edad >= 4 and edad <= 18):

    print("Usted debe pagar $500")

elif(edad > 18 ):

    print("Usted debe pagar 1000")    

#Ejercicio 11

print("Ingrese una opción")

print("1 - Pizza no Vegana")

print("2 - Pizza Vegana")

opcion = input("Ingrese una de las 2 opciones: 1 / 2: ")

if(opcion == "1"):

    pizza = "No vegana, con "

    print("LISTA DE INGREDIENTES: ")

    print("1- Pepperoni")

    print("2- Jamón")

    print("3- Salmón")

    opcionNV = input("Ingrese un ingrediente 1 / 2 / 3: ")



    if(opcionNV == "1"):

     pizza = pizza + "Pepperoni"

    elif(opcionNV == "2"):

     pizza = pizza + "Jamón"

    elif(opcionNV == "3"):
  
     pizza = pizza + "Salmón"


if(opcion == "2"):

    pizza = "Vegana, con "

    print("LISTA DE INGREDIENTES: ")

    print("1- Tofu")

    print("2- Pimiento" )
   
    opcionV = input("Ingrese un ingrediente 1 / 2: ")
     
    
    if(opcionV == "1"):

     pizza = pizza + "Tofu"

    elif(opcionV == "2"):

     pizza = pizza + "Pimiento"


print("Su pizza es", pizza, ", Mozzarella y Tomate")

#Ejercicio 12

anioActual = int(input("Ingrese el año actual: "))

anio = int(input("Ingrese cualquier otro año: "))

resultado = (anio - anioActual).__abs__()

if (anio > anioActual):

 print("Faltan ", resultado, " años")

elif(anio < anioActual):

 print("Pasaron ", resultado, " años desde ese año")

else:

 print("Estamos en ese mismo año")

 #Ejercicio 13

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mayor = num1
menor = num2

if (mayor < menor):

 mayor = num2
 menor = num1


if (mayor == 0 or menor == 0):
 
 print("Uno de los 2 números es nulo")

elif(mayor < 0 or menor < 0):
 
 print("Uno de los 2 números es negativo")

else:

 if(mayor % menor == 0):
 
  print("El número mayor es múltiplo del menor")
 
 else:
  
  print("El número mayor no es múltiplo del menor")

 #Ejercicio 14

a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
    
if a == 0:
        if b == 0:
            print("Todos los números son solución")
        else:
            print("La ecuación no tiene solución")
else:
        x = -b / a
        print(f"La solución es x = {x}")

#Ejercicio 15

import math

respuesta = input("¿Desea calcular el area de un triangulo? (t/T) ¿Desea calcular el area de un círculo? (c/C)").lower()

if (respuesta == "t"):

 base = int(input("Ingrese la base: "))

 altura = int(input("Ingrese la altura: "))

 areaT = (base * altura) / 2

 print("El area del triángulo es: ", areaT)

elif (respuesta == "c"):
 
 radio = int(input("Ingrese el radio: "))

 areaC = math.pi * radio ** 2

 print("El área del círculo es de: ", areaC)

 #Ejercicio 16

 num1 = int(input("Ingrese el primer número: "))

num2 = int(input("Ingrese el segundo número: "))

print("¿Que desea?")

print("1- Suma")

print("2- Multiplicación")

print("3- Resta")

print("4- División")

respuesta = int(input("Ingrese un número (1-4): "))

if (respuesta == 1 ):
    suma = num1 + num2
    print("La suma entre ambos números es: ", suma)

elif (respuesta == 2):
    multi = num1 * num2
    print("La multiplicación entre ambos números es: ", multi)

elif (respuesta == 3):
    resta = num1 - num2
    print("La resta entre ambos números es: ", resta)

elif (respuesta == 4):
    divi = num1 / num2
    print("La división entre ambos números es: ", divi)

#Ejercicio 17

respuesta = input("Ingrese el nombre de un día: ").lower()

if(respuesta == "lunes"):

    print("Hoy es lunes")

if(respuesta == "viernes"):

    print("Hoy es viernes")

if(respuesta == "sábado" or respuesta == "sabado" or respuesta == "domingo"):

    print("Hoy es sábado o domingo")

else:

    print("El día ingresado no es correcto")

#Ejercicio 18

horas_trabajadas = int(input("Ingrese las horas trabajadas por mes: "))

salario_hora = int(input("Ingrese el salario que gana por hora: "))

if(horas_trabajadas > 48):

 hrs_extra = horas_trabajadas - 48

 print("Usted trabajo ", hrs_extra, "horas extra")

 extra = hrs_extra * 0.10

 total = extra + horas_trabajadas * salario_hora

 print("Su salario total es de: ", total)    

#Ejercicio 19

lapices = int(input("Ingrese la cantidad de lápices a comprar: "))

if lapices > 60:

    descuento = 0.07

    total_descuento = descuento * 60 * lapices

    a_pagar = lapices * 60 - total_descuento

    print("El precio con descuento es:", a_pagar)

else:

    a_pagar = 60 * lapices

    print("No hay descuento")
    
    print("El precio final es:", a_pagar)

#Ejercicio 20

print("Ingrese las 4 notas")

nota1 = int(input("Primera nota: "))
nota2 = int(input("Segunda nota: "))
nota3 = int(input("Tercera nota: "))
nota4 = int(input("Cuarta nota: "))

promedio = ((nota1 + nota2 + nota3 + nota4) / 4).__trunc__()

if (promedio >= 6):

    print("Aprobado, su promedio es de: ", promedio)

else:

   print("Desaprobado, su promedio es de: ", promedio) 