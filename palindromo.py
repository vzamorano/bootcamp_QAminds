# Alumna: Vivian Zamorano Castelo
# Código 1
# Crea una función que reciba (directamente o desde el usuario) una cadena de texto y retorne un mensaje confirmando si es un Palindromo o no.

def palindromo():
    var = True
    while var:
        cadena = input('Ingrese una palabra o expresión: ')
        cadena = cadena.strip(".") # Se eliminan los puntos que puede contener la expresión
        cadena = cadena.replace(" ", "").lower() # Se eliminan los espacios en blanco y se convierte la cadena de texto a minuúsculas
        if cadena == cadena[::-1]: # Se compara la cadena original con su inversa
            print("El texto ingresado es un palíndromo")
        else:
            print("El texto ingresado no es un palíndromo")
        var = False

palindromo() # Se llama a la función
