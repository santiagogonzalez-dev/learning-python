# To define a dictionary we need to use { }
# diccionario = {
#         "nombre": "Chanchito feliz",
#         "raza": "Persa",
#         "edad": 5
# }
# Let's not forget to use , at the end
# print(diccionario)
# print(diccionario["nombre"])
# print(diccionario['raza'])
# We can also use a method to access the values
# print(diccionario.get('nombre'))

# To change a value from a dictionary
# diccionario['nombre'] = 'Fluffy'

# print(len(diccionario)) # Count elements in the dictionary

# diccionario['ronronea'] = 'Si'

# diccionario.pop('ronronea')
# diccionario.popitem()
# copiaGatito = diccionario.copy() # It makes a copy
# copiaGatito = dict(diccionario) # It makes a copy
# del diccionario['nombre']
# diccionario.clear()
# print(diccionario, copiaGatito)

fluffy= {
    "nombre": "Fluffy",
    "edad": 4
}

mamba= {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

# Constructors

perritos = dict(nombre = "Chanchito Feliz", edad = 6) # " " " " "
print(perritos)
