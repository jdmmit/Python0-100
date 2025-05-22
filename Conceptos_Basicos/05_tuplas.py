### Tuplas ###

my_tuple = tuple()  # Tupla vacía
my_other_tuple = ()  # Tupla vacía

my_tuple = (42, 1.84, "Juan", "Murillo")  # Tupla con elementos
print(my_tuple)  # Imprime la tupla
print(type(my_tuple))  # Imprime el tipo de la tupla
print(my_tuple[0])  # Imprime el primer elemento de la tupla
print(my_tuple[1])  # Imprime el segundo elemento de la tupla
print(my_tuple[-1])  # Imprime el último elemento de la tupla

print(my_tuple.count(42))  # Imprime cuántas veces aparece el número 42 en la tupla
print(my_tuple.index(1.84))  # Imprime el índice del primer elemento que es 1.84
print(my_tuple.index("Juan"))  # Imprime el índice del primer elemento que es "Juan"
print(
    my_tuple.index("Murillo")
)  # Imprime el índice del primer elemento que es "Murillo"

my_sum_tuple = my_tuple + my_other_tuple  # Suma de tuplas
print(my_sum_tuple)  # Imprime la tupla resultante de la suma

print(my_sum_tuple[1:3])  # Imprime el cuarto y sexto elemento de la tupla


my_tuple = list(my_tuple)  # Convierte la tupla en una lista
print(type(my_tuple))  # Imprime la lista resultante de la conversión
my_tuple = tuple(my_tuple)  # Convierte la lista en una tupla
print(type(my_tuple))  # Imprime la tupla resultante de la conversión

del my_tuple  # Elimina la tupla

my_tuple = (42, 1.84, "Juan", "Murillo")  # Tupla con elementos
print(my_tuple)  # Imprime la tupla
print(type(my_tuple))  # Imprime el tipo de la tupla
