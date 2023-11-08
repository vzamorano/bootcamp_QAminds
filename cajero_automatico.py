# Alumna: Vivian Zamorano Castelo
# Código 2

import random
import string

from abc import ABC

class Cajero(ABC):
    
    def __init__(self):
        self.cuentas = []

    def crear_cuenta(self, id, nombre, apellidoPaterno, apellidoMaterno, diaNacimiento, mesNacimiento, anioNacimiento,
                     genero, saldoInicial): # Método para crear una cuenta
        self.id = id
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.diaNacimiento = diaNacimiento
        self.mesNacimiento = mesNacimiento
        self.anioNacimiento = anioNacimiento
        self.genero = genero
        self.saldoInicial = saldoInicial
        if id not in self.cuentas:
            cuenta = {"ID": self.id, 
                      "Nombre": self.nombre, 
                      "ApellidoPaterno": self.apellidoPaterno, 
                      "ApellidoMaterno": self.apellidoMaterno, 
                      "DiaNacimiento": self.diaNacimiento, 
                      "MesNacimiento": self.mesNacimiento, 
                      "AnioNacimiento": self.anioNacimiento, 
                      "Genero": self.genero, 
                      "SaldoInicial": self.saldoInicial}
            cuenta['rfc'] = self.generar_rfc(cuenta)
            self.cuentas.append(cuenta)
            print("Su cuenta ha sido creada exitosamente")
    
    def visualizar_cuenta(self, id): # Método para visualizar una cuenta
        for cuenta in self.cuentas:
            if cuenta["ID"] == id:
                
                print("Detalle de la cuenta: ")
                print(f"ID: {id}")
                print(f"Nombre: {cuenta['Nombre']}")
                print(f"Apellido Paterno: {cuenta['ApellidoPaterno']}")
                print(f"Apellido Materno: {cuenta['ApellidoMaterno']}")
                print(f"Fecha de Nacimiento: {cuenta['DiaNacimiento']}/{cuenta['MesNacimiento']}/{cuenta['AnioNacimiento']}")
                print(f"Género: {cuenta['Genero']}")
                print(f"RFC: {cuenta['rfc']}")
                print(f"Saldo: {cuenta['SaldoInicial']}")
            print("La cuenta no existe")
    
    def eliminar_cuenta(self, id): # Método para eliminar una cuenta
        for cuenta in self.cuentas:
            if cuenta["ID"] == id:
                self.cuentas.remove(cuenta)
                print(f"La cuenta con el número de ID: {id} fue eliminada")
            print("La cuenta no existe")

    def depositar_saldo(self, id, monto): # Método para depositar saldo a una cuenta
        for cuenta in self.cuentas:
            if cuenta["ID"] == id:
                deposito = cuenta["SaldoInicial"] + monto
                if deposito <= 8000:
                    print(f"Se depositaron ${monto} a su cuenta.")
                else:
                    excedente = 8000 - deposito
                    excedente = excedente * (-1)
                    print(f"El monto máximo a depositar es de $8000, tu excedente es de ${excedente}. No es posible realizar el depósito")    
            print("La cuenta no existe")

    def retirar_saldo(self, id, monto): # Método para retirar saldo de una cuenta
        for cuenta in self.cuentas:
            if cuenta["ID"] == id:
                if cuenta["SaldoInicial"] >= monto:
                    cuenta["SaldoInicial"] -= monto
                    print(f"Se retiraron ${monto} de su cuenta.")
                else:
                    print("Saldo insuficiente")
            print("La cuenta no existe")

    def generar_rfc(self, cuenta): # Método para generar el RFC de una persona
        self.nombre = cuenta["Nombre"].upper() # Se convierte el nombre a mayúsculas
        self.apellidoPaterno = cuenta["ApellidoPaterno"].upper() # Se convierte el apellido paterno a mayúsculas
        self.apellidoMaterno = cuenta["ApellidoMaterno"].upper() # Se convierte el apellido materno a mayúsculas
        self.diaNacimiento = cuenta["DiaNacimiento"]
        self.mesNacimiento = cuenta["MesNacimiento"]
        self.anioNacimiento = cuenta["AnioNacimiento"][-2:] # Se obtienen los dos últimos dígitos del año de nacimiento

        homoclave = string.ascii_uppercase + string.digits # Letras mayúsculas y/o dígitos para la homoclave
        rfc = (
            self.apellidoPaterno[:2] +
            self.apellidoMaterno[0] +
            self.nombre[0] +
            self.anioNacimiento +
            self.mesNacimiento +
            self.diaNacimiento +
            random.choice(homoclave) +
            random.choice(homoclave) + 
            random.choice(homoclave)
        )
        return rfc

        
def menu(): # Función para seleccionar distintas opciones de un menú
    cajero = Cajero() # Se crea una instancia del cajero

    while True:
        print("\nBienvenido al menú del Cajero Automático, estas son las operaciones disponibles:")
        print("1. Crear cuenta")
        print("2. Visualizar cuenta")
        print("3. Eliminar cuenta")
        print("4. Depositar saldo")
        print("5. Retirar saldo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("Ingrese el ID de la cuenta: "))
            nombre = input("Ingrese el nombre del titular de la cuenta: ")
            apellidoPaterno = input("Ingrese el apellido paterno del titular de la cuenta: ")
            apellidoMaterno = input("Ingrese el apellido materno del titular de la cuenta: ")
            diaNacimiento = input("Ingrese el día de nacimiento del titular de la cuenta (2 dígitos): ")
            mesNacimiento = input("Ingrese el mes de nacimiento del titular de la cuenta (2 dígitos): ")
            anioNacimiento = input("Ingrese el año de nacimiento del titular de la cuenta (4 dígitos): ")
            genero = input("Ingrese el género del titular de la cuenta, debe ingresar solo H o M: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cajero.crear_cuenta(id, nombre, apellidoPaterno, apellidoMaterno, diaNacimiento, mesNacimiento, anioNacimiento, genero, saldo_inicial)
        elif opcion == '2':
            id = int(input("Ingrese el ID de la cuenta: "))
            cajero.visualizar_cuenta(id)
        elif opcion == '3':
            id = int(input("Ingrese el ID de la cuenta a eliminar: "))
            cajero.eliminar_cuenta(id)
        elif opcion == '4':
            id = int(input("Ingrese el ID de la cuenta: "))
            monto = float(input("Ingrese el monto a depositar: "))
            cajero.depositar_saldo(id, monto)
        elif opcion == '5':
            id = int(input("Ingrese el ID de la cuenta: "))
            monto = float(input("Ingrese el monto a retirar: "))
            cajero.retirar_saldo(id, monto)
        elif opcion == '6':
            break
        else:
            print("No existe esa opción. Por favor, seleccione una opción válida.")

           
menu() # Se llama a la función menu
