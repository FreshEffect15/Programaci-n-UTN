
#Ejercicio 1


passengers_list = []


city_list = []

def agregar_pasajero():

    name = input("Ingrese el nombre del pasajero: ")

    dni = input("Ingrese el DNI del pasajero: ")

    destiny = input("Ingrese el destino del pasajero: ")

    passengers_list.append((name, dni, destiny))

def agregar_ciudad():

    city = input("Ingrese el nombre de la ciudad: ")

    country = input("Ingrese el nombre del país al que pertenece la ciudad: ")

    city_list.append((city, country))

def buscar_destino_por_dni():

    dni = input("Ingrese el DNI del pasajero: ")

    for name, dni_passenger, destiny in passengers_list:

        if dni_passenger == dni:

            print(f"El pasajero {name} viaja a {destiny}.")

            return
        
    print("DNI no encontrado.")

def contar_pasajeros_por_ciudad():

    city = input("Ingrese el nombre de la ciudad: ")

    count= sum(1 for _, _, destino in passengers_list if destino == city)

    print(f"La cantidad de pasajeros que viajan a {city} es {count}.")

def buscar_pais_por_dni():

    dni = input("Ingrese el DNI del pasajero: ")

    for _, dni_passenger, destiny in passengers_list:

        if dni_passenger == dni:

            for city, country in city_list:

                if city == destiny:

                    print(f"El pasajero viaja a {country}.")

                    return
                
    print("DNI no encontrado o destino no asociado a una ciudad.")

def contar_pasajeros_por_pais():

    country = input("Ingrese el nombre del país: ")

    count = sum(1 for city, p in city_list if p == country for _, _, destiny in passengers_list if destiny == city)

    print(f"La cantidad de pasajeros que viajan a {country} es {count}.")

while True:
    print("MENÚ PRINCIPAL")
    print("1 - Agregar pasajeros")
    print("2 - Agregar ciudades")
    print("3 - Consultar destino por DNI")
    print("4 - Mostrar cantidad de pasajeros por ciudad")
    print("5 - Consultar país por DNI")
    print("6 - Mostrar cantidad de pasajeros por país")
    print("7 - Salir del programa")

    respuesta = input("Ingrese su respuesta: ")

    if respuesta == '1':

        agregar_pasajero()

    elif respuesta == '2':

        agregar_ciudad()

    elif respuesta == '3':

        buscar_destino_por_dni()

    elif respuesta == '4':

        contar_pasajeros_por_ciudad()

    elif respuesta == '5':

        buscar_pais_por_dni()

    elif respuesta == '6':

        contar_pasajeros_por_pais()

    elif respuesta == '7':

        print("Saliendo del programa. ¡Hasta luego!")

        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


#Ejercicio 2

def obtener_domicilios_facturacion(purchase_list):

    adress_facturation = {}

    for customer, _, _, adress in purchase_list:

        adress_facturation[customer] = adress

    
    unique_adress = list(adress_facturation.values())

    return unique_adress


purchase_list = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
                 
                 ('Nuria Costa', 12, 567.8, 'Calle 1 - 456')]

adress = obtener_domicilios_facturacion(purchase_list)

print(adress)

#Ejercicio 3

members = {

    1: {'nombre': 'Amanda Núñez', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    2: {'nombre': 'Bárbara Molina', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True}
}

def cantidad_de_miembros():

    return len(members)

def pagar_cuotas(numero_miembro):

    if numero_miembro in members:

        members[numero_miembro]['cuota_al_dia'] = True

        print(f"El miembro {numero_miembro} ha pagado todas las cuotas adeudadas.")

    else:

        print("Número de miembro no válido.")

def corregir_fecha_ingreso():

    for numero_miembro, informacion_miembro in members.items():

        if informacion_miembro['fecha_ingreso'] == '13/03/2018':

            informacion_miembro['fecha_ingreso'] = '14/03/2018'

def dar_de_baja(nombre, apellido):

    miembros_a_eliminar = []

    for numero_miembro, informacion_miembro in members.items():

        if informacion_miembro['nombre'] == nombre and informacion_miembro['apellido'] == apellido:

            miembros_a_eliminar.append(numero_miembro)

    for numero_miembro in miembros_a_eliminar:

        members.pop(numero_miembro)

        print(f"El miembro {numero_miembro} ({nombre} {apellido}) ha sido dado de baja.")

def imprimir_lista_miembros():

    print("\nLista de miembros:")

    for numero_miembro, informacion_miembro in members.items():

        print(f"Miembro n°{numero_miembro}: {informacion_miembro['nombre']}, Fecha de Ingreso: {informacion_miembro['fecha_ingreso']}, Cuota al día: {'Sí' if informacion_miembro['cuota_al_dia'] else 'No'}")

while True:
    print("\nMENÚ PRINCIPAL")
    print("1 - Informar cantidad de miembros")
    print("2 - Registrar pago de cuotas")
    print("3 - Corregir fecha de ingreso")
    print("4 - Dar de baja a un miembro")
    print("5 - Imprimir lista de miembros")
    print("6 - Salir del programa")

    respuesta = int(input("Ingrese su respuesta: "))

    if respuesta == 1:

        print(f"La cantidad de miembros es: {cantidad_de_miembros()}")

    elif respuesta == 2:

        numero_miembro = int(input("Ingrese el número de miembro que ha pagado todas las cuotas adeudadas: "))

        pagar_cuotas(numero_miembro)

    elif respuesta == 3:

        corregir_fecha_ingreso()

        print("La fecha de ingreso ha sido corregida para todos los miembros.")

    elif respuesta == 4:

        nombre = input("Ingrese el nombre del miembro a dar de baja: ")

        apellido = input("Ingrese el apellido del miembro a dar de baja: ")

        dar_de_baja(nombre, apellido)

    elif respuesta == 5:

        imprimir_lista_miembros()

    elif respuesta == 6:

        print("Saliendo del programa")
        
        break
    else:

        print("Opción no válida. Por favor, seleccione una opción válida.")