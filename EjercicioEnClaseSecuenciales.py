fecha = input("Ingrese la fecha (formato: dia/mes/año): ")

nombre_dia = fecha.split("/")[0].lower()

mes_num = int(fecha.split("/")[1])

dia_num = int(fecha.split("/")[2])

if (nombre_dia == "lunes" and dia_num <= 31 and mes_num <= 12):
    
    print("Dia Lunes")

    print("Clases de nivel inicial")
 
    respuesta = input("¿Hubo exámenes? (S/N): ")

    respuesta = respuesta.lower()

    if(respuesta == "s"):

         aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
           
         desaprob =  int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
     
         porcentaje_Aprob = aprob / (aprob + desaprob) * 100

         porcentaje_Aprob = porcentaje_Aprob.__trunc__()

         print("El porcentaje de aprobados fue del ", porcentaje_Aprob, "%")



elif (nombre_dia == "martes" and dia_num <= 31 and mes_num <= 12):

    print("Dia Martes")

    print ("Clases de nivel intermedio")

    respuesta = input("¿Hubo exámenes? (S/N): ")

    respuesta = respuesta.lower()

    if(respuesta == "s"):

         aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
           
         desaprob =  int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
     
         porcentaje_Aprob = aprob / (aprob + desaprob) * 100

         porcentaje_Aprob = porcentaje_Aprob.__trunc__()

         print("El porcentaje de aprobados fue del ", porcentaje_Aprob, "%")

elif(nombre_dia == "miércoles" or nombre_dia == "miercoles" and dia_num <= 31 and mes_num <= 12):

    print("Dia Miércoles")

    print("Clases de nivel avanzado")

    respuesta = input("¿Hubo exámenes? (S/N): ")

    respuesta = respuesta.lower()

    if(respuesta == "s"):

         aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
           
         desaprob =  int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
     
         porcentaje_Aprob = aprob / (aprob + desaprob) * 100

         porcentaje_Aprob = porcentaje_Aprob.__trunc__()

         print("El porcentaje de aprobados fue del ", porcentaje_Aprob, "%")

elif (nombre_dia == "jueves" and dia_num <= 31 and mes_num <= 12):

    print("Dia Jueves")

    print ("Clases de práctica hablada")

    porcentaje_asis = int(input("Ingrese el porcentaje de alumnos que asistieron: "))

    if(porcentaje_asis > 50):

          print("Asistió la mayoría")  
    else:
          print("Faltó la mayoría")

elif(nombre_dia == "viernes" and dia_num <= 31 and mes_num <= 12):

    print("Dia Viernes")

    print("Clases de inglés para viajeros")

    if(dia_num == 1 and mes_num == 1 or mes_num == 7):
         print("Comienzo del nuevo ciclo")

         alumnos_ingreso = int(input("Ingrese la cantidad de alumnos ingresantes del nuevo ciclo: "))

         arancel = int(input("Ingrese el arencel por cada alumno: "))

         total = alumnos_ingreso * arancel

         print("El ingreso total: $", total )


elif (nombre_dia == "sábado" or nombre_dia == "sabado" and dia_num <= 31 and mes_num <= 12):

    print("Dia Sábado")

    print("No es un día escolar")

elif(nombre_dia == "domingo" and dia_num <= 31 and mes_num <= 12):

    print("Dia Domingo")

    print("No es un día escolar")

else:

    print("Error, por favor ingrese una fecha válida")
