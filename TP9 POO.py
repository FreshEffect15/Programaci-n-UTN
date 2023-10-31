
#Ejercicio 1

class Persona:

    def __init__(self, name="", age=0, DNI=""):

        self.name = name

        self.age = age
        
        self.DNI = DNI

    def mostrar(self):

        print("Nombre:", self.name)
        print("Edad:", self.age)
        print("DNI:", self.DNI)

    def esMayorDeEdad(self):
        return self.age >= 18

    def setNombre(self, nombre):
        self.name = name

    def setEdad(self, edad):
        if age >= 0:
            self.age = age
        else:
            print("La edad no puede ser negativa.")

    def setDNI(self, DNI):
        self.DNI = DNI

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDNI(self):
        return self.DNI


name = input("Ingresa el nombre: ")

age = int(input("Ingresa la edad: "))

DNI = input("Ingresa el DNI: ")


person1 = Persona(name, age, DNI)

person1.mostrar()

print("Es mayor de edad:", person1.esMayorDeEdad())

#Ejercicio 2

class Cuenta:

    def __init__(self):

        self.headline = input("Ingrese el nombre: ")

        self.amount = 0.0

    def mostrar(self):

        print("Titular de la cuenta:", self.headline)

        print("Saldo en la cuenta:", self.amount)

    def ingresar(self, amount):

        if amount > 0:

            self.amount += amount

            print(amount, " ingresado en la cuenta.")

        else:

            print("La cantidad ingresada debe ser mayor que cero.")

    def retirar(self, amount):

        if amount > 0:

            if self.amount >= amount:

                self.amount -= amount

                print(amount, " retirado de la cuenta.")

            else:

                print("No hay suficiente saldo en la cuenta.")

        else:
            
            print("La cantidad a retirar debe ser mayor que cero.")

account = Cuenta()

account.mostrar()

amount = float(input("Ingrese la cantidad a ingresar en la cuenta: "))

account.ingresar(amount)

account.mostrar()

amount = float(input("Ingrese la cantidad a retirar de la cuenta: "))

account.retirar(amount)

account.mostrar()


#Ejercicio 3

class Triangulo:

    def __init__(self, side1, side2, side3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def determinar_tipo(self):

        if self.side1 == self.side2 == self.side3:

            return "Equilátero"
        
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:

            return "Isósceles"
        
        else:

            return "Escaleno"

    def imprimir_lado_mayor(self):

        higher = max(self.side1, self.side2, self.side3)

        print("El lado con mayor longitud es ", higher)


side1 = float(input("Ingrese la longitud del primer lado: "))
side2 = float(input("Ingrese la longitud del segundo lado: "))
side3 = float(input("Ingrese la longitud del tercer lado: "))

triangle = Triangulo(side1, side2, side3)

print("El triángulo es de tipo " , triangle.determinar_tipo())

triangle.imprimir_lado_mayor()

#Ejercicio 4

class Contacto:
    def __init__(self, name, phone, email):

        self.name = name
        self.phone = phone
        self.email = email

class Agenda:

    def __init__(self):

        self.contacts = []

    def add_contact(self, name, phone, email):

        contact = Contacto(name, phone, email)

        self.contacts.append(contact)

        print("Contacto ", name, " agregado a la agenda.")

    def list_contacts(self):

        if not self.contacts:

            print("La agenda está vacía.")

        else:

            print("Lista de contactos:")

            for contact in self.contacts:

                print("Nombre: ", contact.name, " Teléfono: ", contact.phone, " Email: ", contact.email)

    def search_contact(self, name):

        for contact in self.contacts:

            if contact.name == name:

                print("Contacto encontrado - Nombre: ", contact.name, " Teléfono: ", contact.phone, " Email: ", contact.email)

                return
            
        print("Contacto con nombre ", name, " no encontrado.")

    def edit_contact(self, name, new_phone, new_email):

        for contact in self.contacts:

            if contact.name == name:

                contact.phone = new_phone

                contact.email = new_email

                print("Contacto ", name, " actualizado.")

                return
            
        print("Contacto con nombre ", name, " no encontrado.")

    def menu(self):


        while True:

            print("\nMenú de Agenda:")

            print("1. Añadir contacto")

            print("2. Lista de contactos")

            print("3. Buscar contacto")

            print("4. Editar contacto")

            print("5. Cerrar agenda")

            option = input("Elija una opción (1/2/3/4/5): ")

            if option == '1':

                name = input("Nombre del contacto: ")

                phone = input("Teléfono del contacto: ")

                email = input("Email del contacto: ")

                self.add_contact(name, phone, email)

            elif option == '2':

                self.list_contacts()

            elif option == '3':
                name = input("Nombre del contacto a buscar: ")
                self.search_contact(name)

            elif option == '4':

                name = input("Nombre del contacto a editar: ")

                new_phone = input("Nuevo teléfono: ")

                new_email = input("Nuevo email: ")

                self.edit_contact(name, new_phone, new_email)

            elif option == '5':

                print("Agenda cerrada.")

                break

            else:
                
                print("Opción no válida. Intente de nuevo.")



my_agend = Agenda()

my_agend.menu()