# def miFuncion():
#     print('Mi primera función!')
#
# miFuncion()

# En lugar de decir que estoy pasándole un argumento, yo voy a decir
# que le estoy pasando un parámetro. Cuando nosotros llamamos a la función y le pasamos un valor
# en estos paréntesis, el valor que nosotros le estamos entregando es un parámetro.
# Pero cuando nosotros hacemos referencia a ese valor dentro de la función se llama argumento.
# def imprimeDato(nombre, apellido):
#     print('El nombre completo es:', nombre, apellido)
#
#imprimeDato(input('Su nombre es: '), input('Y su apellido: '))
# imprimeDato()
# Si la función tiene un argumento, hay que pasarle un parámetro
# Si la función tiene dos argumentos, hay que pasarle dos parámetros
# y así necesariamente.

# def imprimeDato(*nombre):
#     print('El nombre completo es:', nombre)
# nombre seria una tumpla y no la podemos modificar
# imprimeDato('Chanchito', 'feliz', 'lala', 'lele')

# def nombreCompleto(apellido, nombre):
#     print(nombre, apellido)
#
# nombreCompleto(nombre='Chanchito', apellido='Feliz')
#
# def nombreCompleto2(**kwargs):
#     print(kwargs['nombre'], kwargs['apellido'])
#
# nombreCompleto2(nombre='Chanchito', apellido='Feliz')

# def miFuncion2(argumento = 'Chanchito'):
#     print(argumento)
#
# # miFuncion2("Batman")
# # miFuncion2()
#
# def miFuncionLista(lista):
#     for el in lista:
#         print(el)
#
# miFuncionLista(['Chanchito', 'Feliz'])
#
# def concatenaNombres(lista):
#     i = ''
#     for el in lista:
#         i = i + el + ' '
#     return i
#
# nombres = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
