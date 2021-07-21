# A list is a data group
# Son datos agrupados

# Add, copy, clear
# lista = [1, 2, 3, 3] # To define a list we need to use [ ]

lista = ['Hola', 'Mundo', 'Chanchito feliz']

#lista2 = lista.copy()
# To add an element to a list
#lista.append(4)
lista.append('Chanchito triste')
# It changes the list without the need to create a new one

# lista.clear() # It clears the list

#print(lista, lista2)

# Counting
# Quantity of the specified element
#print(lista.count(3))

# print(len(lista)) # Count total of elements
# largoLista = len(lista)
# print(largoLista) # It's the same


#print(lista[0]) # The first element will always be 0

# Deleting elements on the list
# lista.pop() # Deletes the last element on the list
#lista.remove('Hola') # Deletes element for it's value
#print(lista)

lista.reverse()
lista.sort()
print(lista)
