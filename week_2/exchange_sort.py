# a. Al inicio del programa colocar los siguientes mensajes en 2 líneas
# diferentes:
# Hola Soy “tu nombre” del grado 9.
# Este programa permitirá clasificar número mayor y menor de tres números
# enteros.
# b. Solicitar 3 números enteros
# c. Elaborar la estructura del código que permita clasificar los números mayor y
# menor de los 3 números enteros, sin hacer uso de elementos iterables (listas,
# tuplas, otros), ni tampoco funciones como max o min.
# d. El programa imprimirá en consola:
# El número mayor es “número mayor” y el número menor es “número menor”
# e. El programa debe ser capaz de clasificar los números como mayor y menor,
# en cualquier orden que se ingresen los números.

print("Hola Soy Sergio Ardila del grado 9.")
print(
    "Este programa permitirá clasificar número mayor y menor de tres números enteros."
)

number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
number_3 = int(input("Ingrese el tercer numero: "))

if number_1 > number_2:
    number_1, number_2 = number_2, number_1
if number_1 > number_3:
    number_1, number_3 = number_3, number_1
if number_2 > number_3:
    number_2, number_3 = number_3, number_2

smaller_number = number_1
intermediate_number = number_2
larger_number = number_3

print(
    "El número mayor es: "
    + str(larger_number)
    + ", el número medio es: "
    + str(intermediate_number)
    + " y el numero menor es: "
    + str(smaller_number)
)
