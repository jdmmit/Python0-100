### Listas ###

my_list = list() # Inicializa una lista vacía
my_other_list = [] # Inicializa una lista vacía

print(len(my_list)) # Imprime la longitud de la lista

my_list = [1, 2, 3, 3, 3, 4, 5] # Inicializa una lista con elementos

print(my_list) # Imprime la lista
print(len(my_list)) # Imprime la longitud de la lista

my_other_list = [35, 1.77, "Hola", True] # Inicializa una lista con diferentes tipos de datos
print(type(my_other_list)) # Imprime la lista

print(my_other_list[0]) # Imprime el primer elemento de la lista
print(my_other_list[1]) # Imprime el segundo elemento de la lista
print(my_other_list[2]) # Imprime el tercer elemento de la lista        
print(my_other_list[3]) # Imprime el cuarto elemento de la lista
print(my_other_list[-1]) # Imprime el último elemento de la lista
print(my_other_list[::-1]) # Imprime el penúltimo elemento de la lista
print(len(my_other_list)) # Imprime la longitud de la lista
print(my_other_list.count(1.77)) # Imprime la cantidad de veces que aparece el elemento 1.77 en la lista
print(my_other_list.index(1.77)) # Imprime el índice del elemento 1.77 en la lista
print(my_list.count(3)) # Imprime la cantidad de veces que aparece el elemento 3 en la lista
print(my_list.index(3)) # Imprime el índice del elemento 3 en la lista
print(my_list.index(3, 3)) # Imprime el índice del elemento 3 en la lista a partir del índice 3