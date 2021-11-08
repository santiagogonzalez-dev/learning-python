# Multiply without using asterisk

# num1 = int(input('Enter first number ->'))
# num2 = int(input('Enter second number ->'))
num1 = 9
num2 = 3

a = 9
b = 3
result_for = 0
for x in range(a):
    result_for += b

print('Result ->', result_for)


# Insert name and lastname and print them backwards

name_user = 'Santiago'
lastname_user = 'Gonzalez'

concatenated = name_user + ' ' + lastname_user

print(concatenated[::-1])


# Find the smallest element from a list

numbers_list = [ 1, 2, 5, 3, 55, -24, -13 ]

menor = 'init'

for x in numbers_list:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor


# Create a function that returns the volume of a sphere with the radius

import math

# radius = int(input('Give the radius of the sphere ==>'))
radius = 3

# Formula: 4/3 x pi x (diameter /2)^3
def volume_of_sphere(r):
    return (4/3 * math.pi * (r) ** 3)


print(volume_of_sphere(radius))


# Write a function the tells if the user is of legal age

def user_legale_age(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = user_legale_age(usuario)
resultado2 = user_legale_age(usuario2)

print(resultado1, resultado2)
print()


# Check if a number is odd(impar) or even(par)

def odd_even(num):
    if num%2 == 0:
        return print('Number is even')
    elif num%2 == 1:
        return print('Number is odd')

# odd_even(6)
odd_even(10)
print()


# Write a function that indicates how many vowels a word has

def quantity_vowels(word):
    count = 0
    # for c in word:
    #     print('Current character ->', c)
    #     if c == 'a':
    #         count += 1
    #     elif c == 'e':
    #         count += 1
    #     elif c == 'i':
    #         count += 1
    #     elif c == 'o':
    #         count += 1
    #     elif c == 'u':
    #         count += 1
    # OR DO THIS THAT IS CLEANER
    for c in word:
        if c in 'aeiou':
            count += 1

    print('There is', count, 'vowels in this word')


word = 'Chanchito'.lower()
quantity_vowels(word)


# Write an application that receives an infinite quantity of numbers until the user types
# "stop", for later receive the sum of entered numbers.

respuesta = '0'
final_result = 0
while respuesta != 'stop':
    respuesta = input('Enter numbers to sum: ')
    if respuesta == 'stop':
        print('User input: stop')
    else:
        try:
            respuesta_int = int(respuesta)
            final_result += respuesta_int
        except:
            print('The introduced character is not a number, try again')

print('The total is ==>', final_result)


# Write a function that receives name and lastname that add thems to a file

def write_name(name_user, lastname_user):
    with open('list_names', 'a') as l:  # Write mode
        l.write("%s %s\n" % (name_user, lastname_user))

write_name(input('Enter name'), input('Enter last name'))
