### Strings ###

my_string = "Mi string"
mu_other_string = "Mi otro string"

print(len(my_string))  # Longitud del string
print(my_string + " " + mu_other_string)  # Concatenación de strings

my_new_string = "este es un string \n con salto de linea"
print(my_new_string)  # Imprime el string con salto de línea

my_tab_string = "este es un string \t con tabulacion"
print(my_tab_string)  # Imprime el string con tabulación

my_scape_string = "\\ este es un string \\ con barra invertida"
print(my_scape_string)  # Imprime el string con barra invertida

name, surname = "Juan", "Pérez"
print(f"Hola, mi nombre es {name} {surname}")  # Imprime el string con variables
print("Hola, mi nombre es {} {}".format(name, surname))  # Imprime el string con variables usando format
print("Hola, mi nombre es %s %s" % (name, surname))  # Imprime el string con variables usando el operador %
print("Hola, mi nombre es {0} {1}".format(name, surname))  # Imprime el string con variables usando format con índices

# Desempaquetando caracteres
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)  # Imprime el primer carácter del string
print(b)
print(c)
print(d)
print(e)
print(f)
print(lenguaje[0])  # Imprime el primer carácter del string

# Division de strings

language_slice = lenguaje[1:3]
print (language_slice)  # Imprime una parte del string (desde el índice 1 hasta el índice 3)

lenguaje_slice = lenguaje[1:]  # Imprime una parte del string (desde el índice 1 hasta el final)
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # Imprime el penúltimo carácter del string
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2] # Imprime el string desde el índice 0 hasta el índice 6, con un paso de 2
print(lenguaje_slice)  # Imprime el string con un paso de 2

# Reverso de un string

reversed_string = lenguaje[::-1]  # Invierte el string
print(reversed_string)  # Imprime el string invertido



# Métodos de strings
print(lenguaje.upper())  # Convierte el string a mayúsculas
print(lenguaje.lower())  # Convierte el string a minúsculas
print(lenguaje.capitalize())  # Convierte la primera letra del string a mayúsculas
print(lenguaje.title())  # Convierte la primera letra de cada palabra del string a mayúsculas
print(lenguaje.strip())  # Elimina los espacios en blanco al principio y al final del string
print(lenguaje.replace("P", "J"))  # Reemplaza una letra por otra en el string
print(lenguaje.split("t"))  # Divide el string en una lista de strings, usando un separador
print(lenguaje.split())  # Divide el string en una lista de strings, usando un separador por defecto (espacio)
print(lenguaje.find("t"))  # Busca una letra en el string y devuelve su índice
print(lenguaje.count("t"))  # Cuenta cuántas veces aparece una letra en el string
print(lenguaje.startswith("P"))  # Comprueba si el string empieza con una letra
print(lenguaje.endswith("n"))  # Comprueba si el string termina con una letra
print(lenguaje.isalpha())  # Comprueba si el string contiene solo letras
print(lenguaje.isalnum())  # Comprueba si el string contiene solo letras y números
print(lenguaje.isdigit())  # Comprueba si el string contiene solo números
print(lenguaje.isnumeric())  # Comprueba si el string contiene solo números
print(lenguaje.isdecimal())  # Comprueba si el string contiene solo números decimales
print(lenguaje.isidentifier())  # Comprueba si el string es un identificador válido
print(lenguaje.isprintable())  # Comprueba si el string es imprimible
print(lenguaje.islower())  # Comprueba si el string está en minúsculas
print(lenguaje.isupper())  # Comprueba si el string está en mayúsculas
print(lenguaje.istitle())  # Comprueba si el string está en formato de título
print(lenguaje.swapcase())  # Cambia las mayúsculas por minúsculas y viceversa
print(lenguaje.zfill(10))  # Rellena el string con ceros a la izquierda hasta que tenga una longitud de 10
print(lenguaje.ljust(10))  # Rellena el string con espacios a la derecha hasta que tenga una longitud de 10
print(lenguaje.rjust(10))  # Rellena el string con espacios a la izquierda hasta que tenga una longitud de 10
print(lenguaje.center(10))  # Rellena el string con espacios a la izquierda y a la derecha hasta que tenga una longitud de 10
print(lenguaje.expandtabs(4))  # Cambia las tabulaciones por espacios       
print(lenguaje.index("t"))  # Busca una letra en el string y devuelve su índice
print(lenguaje.rindex("t"))  # Busca una letra en el string y devuelve su índice, empezando por el final
print(lenguaje.rfind("t"))  # Busca una letra en el string y devuelve su índice, empezando por el final
print(lenguaje.partition("t"))  # Divide el string en una tupla de 3 elementos, usando un separador
print(lenguaje.rpartition("t"))  # Divide el string en una tupla de 3 elementos, usando un separador, empezando por el final
print(lenguaje.splitlines())  # Divide el string en una lista de strings, usando un separador por defecto (salto de línea)
print(lenguaje.translate(str.maketrans("aeiou", "AEIOU")))  # Cambia las vocales por mayúsculas
print(lenguaje.translate(str.maketrans("aeiou", "AEIOU", "aeiou")))  # Cambia las vocales por mayúsculas y elimina las minúsculas
