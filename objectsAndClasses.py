# Python it's multi-paradigm language
# it has object, classes and inheritance
# The objects in python are a type of data that contains properties
# and methods, that's what an object is.
# The methods are function that are going to work with the object and the
# properties that it has.
# El plano seria la clase

# Always use upper case for the name of the class, just like in java
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print('Hola, mi nombre es: ', self.nombre, self.apellido)

# The instances must be written in lower case
usuario = Usuario("Felipe", "Feliz")
#usuario2 = Usuario("Chanchito", "Feliz")

#print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

usuario.saludo()
#usuario2.saludo()
usuario.nombre = "Chanchito"
usuario.saludo()
del usuario.nombre()
usuario.saludo()
