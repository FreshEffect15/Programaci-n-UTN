#Trabajo 1

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

final = ""

corrimiento = int(input("Ingrese el corrimiento: "))

mensaje = input("Ingrese el mensaje que desea mandar: ")

for i in mensaje:

    if i.lower() in letras:

        indice = (letras.index(i.lower()) + corrimiento) % len(letras)

        if i.isupper():

            final += letras[indice].upper()

        else:

            final += letras[indice]
    else:
        
        final += letra

print("Mensaje encriptado:", final)

#2 

salir = False

pares = 0

inpares = 0

while salir != True:
 print("Ingrese un número, se dividirán sus digitos y se contará cuanles de ellos son pares e inpares")

 num = int(input("Ingrese un número entero positivo, ingrese un 0 para salir: "))

 if (num == 0):
  
  salir = True

 elif (num < 0):
  
  print("Por favor, ingrese un número válido")

 else:
  
  if num < 10:
   
   if num % 2 == 0:

    pares = pares + 1
   else:
    inpares = inpares + 1
  else:
   
    digitos = [int(digito) for digito in str(num)]
   
    for i in digitos:
   
     if(i % 2 == 0):
      pares = pares + 1
     else:
      inpares = inpares + 1
   
print("La cantidad de carácteres pares fue de: ", pares)
print("La cantidad de carácteres inpares fue de: ", inpares)