#Ejercicio 1 

base = int(input("Ingrese la base del rectángulo "))

altura = int(input("Ingrese la altura del rectángulo "))

area = base * altura

perimetro = 2 * altura + 2 * base

print("El area del rectángulo es: ", area)

print("El perímetro del rectángulo es: ", perimetro)

#Ejercicio 2

cateto1 = int(input("Ingrese el primer cateto del triángulo "))

cateto2 = int(input("Ingrese el segundo cateto del triángulo "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa es: ", hipotenusa)

#Ejercicio 3

num1 = int(input("Ingrese el primer número "))

num2 = int(input("Ingrese el segundo número "))
 
suma = num1 + num2

resta = num1 - num2

multi = num1 * num2

divis = num1 / num2

print("El resultado de la suma de los números es: ", suma)

print("El resultado de la resta de los números es: ", resta)

print("El resultado de la multiplicación de los números es: ", multi)

print("El resultado de la división de los números es: ", divis)

#Ejercicio 4

farenheit = int(input("Ingrese una cantidad de grados farenheit "))

celsius = (farenheit - 32 ) * 5 / 9

print("El resultado de la conversión es: ", celsius )

#Ejercicio 6

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

media = (num1 + num2 + num3) / 3

print ("La media es de: ", media)

#Ejercicio 7

minutos = int(input("Ingrese una cantidad de minutos: "))

horas = (minutos / 60).__trunc__()  

segundos = minutos * 60  

print("La cantidad de horas sería de:", horas)
print("La cantidad de segundos sería de:", segundos)

#Ejercicio 8

sueldo_base= int(input("Ingrese su sueldo base: "))
primera_venta= int(input("Ingrese los ingresos de su primera venta: "))
segunda_venta= int(input("Ingrese los ingresos de su segunda venta: "))
tercera_venta= int(input("Ingrese los ingresos de su tercera venta: "))

comision = 0.10

total_comisiones = (primera_venta + segunda_venta + tercera_venta) * comision

total_mes = sueldo_base * total_comisiones

print("El total de sus comisiones es: ", total_comisiones)

print("El total del mes fue: ", total_mes) 

#Ejercicio 9

precio = float(input("Ingrese el precio del producto: "))

descuento = precio * 0.15

precio_final = precio - descuento

print("El precio final del producto es: ", precio_final)

#Ejercicio 10

parcial1 = int(input("Ingrese la nota de su primer parcial: "))
parcial2 = int(input("Ingrese la nota de su segundo parcial: "))
parcial3 = int(input("Ingrese la nota de su tercer parcial: "))
examen_final = int(input("Ingrese la nota de su exámen final: "))
trabajo_final = int(input("Ingrese la nota de su trabajo final: "))

promedio_parciales = float((parcial1 + parcial2 + parcial3) / 3)

nota_final = float((promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15))

print("La nota final es: ", nota_final)

#Ejercicio 11

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

distancia = num1 - num2.__abs__()

print("La distancia entre ambos números es de: ", distancia)

#Ejercicio 12

num = int(input("Ingrese un número: "))

raiz_cuadrada = num ** (1/2)

raiz_cubica = num ** (1/3)

print("La raíz cuadrada del número es: ", raiz_cuadrada )

print("La raíz cúbica del número es: ", raiz_cubica )

#Ejercicio 13

num = int(input(" Ingrese un número de 2 cifras: "))

unidades = num % 10

decenas = num // 10

invertido = unidades * 10 + decenas

print("El número invertido es: ", invertido)

#Ejercicio 14

A = int(input("ingrese un número para A: "))
B = int(input("Ingrese un número para B: "))

aux = A
A = B
B = aux

print("La variable 'A' vale: ", A )

print("La variable 'B' vale: ", B)

#Ejercicio 15

horas = int(input("Ingrese las horas de partida: "))
minutos = int(input("Ingrese los minutos de partida: "))
segundos = int(input("Ingrese los segundos de partida: " ))
tiempo = int(input("Ingrese tiempo de viaje (segundos): "))

total_segundos = (horas * 3600) + (minutos * 60) + segundos + tiempo
 
horas = total_segundos / 3600

segundos_restantes = total_segundos % 3600

minutos = total_segundos / 60

segundos = segundos_restantes % 60

print("La hora de llegada a la ciudad B será: ", horas, ":", minutos, ":", segundos)

#Ejercicio 16

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[0] + "." + apellido1[0] + "." + apellido2[0]

print("Sus iniciales son: ", iniciales )

#Ejercicio 17

usuario = input("Ingrese su nombre: ")

print("Ahora estás en la Matrix, ",usuario)

#Ejercicio 18

costo = int(input("Ingrese el costo de la cena: "))

servicio = 0.062
propina = 0.10

costo_total = costo + (costo * servicio) + (costo * propina)

print("El costo total de la cena fue de: ", costo_total)

#Ejercicio 19

dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese el número de su mes de nacimiento: "))
anio = int(input("Ingrese su año de nacimiento: "))

print(dia,"/",mes,"/",anio )

#Ejercicio 20

fecha = input("Ingrese su dia de nacimiento en formato DD/MM/AAA: ")

dia = fecha.split("/")[0]

mes = fecha.split("/")[1]

anio = fecha.split("/")[2]

cumple = dia + "/" + mes + "/" + anio

print("Su día de nacimiento es: ", cumple)

#Ejercicio 21

cantidad_km = int(input("Ingrese la cantidad de KM que puede recorrer la moto con un litro de combustible: "))
capacidad_tanque = int(input("Ingrese la capacidad en LT de el tanque de combustible: "))
total_km = int(input("Ingrese la cantidad de KM que recorreran en total: "))

litros_necesarios = total_km / capacidad_tanque
tanques_necesarios = litros_necesarios / cantidad_km

print("La cantidad de tanques de combustible necesarios es: ", tanques_necesarios)
