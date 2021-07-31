# dato = input('Ingrese dato: ')
# 
# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']
# 
# if lista.count(dato) > 0:
#     print('El dato existe: ', dato)
# else:
#     print('El dato no existe: ', dato)

# primero = int(input('Ingrese primer número: '))
# segundo = int(input('Ingrese segundo número: '))
# 
# if (type(primero) is int and type(segundo) is int):
#     print(primero + segundo)
# else:
#     print('Introduzca los números de nuevo')


primero = input('Ingrese primer número: ')
try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

print(primero + segundo)
