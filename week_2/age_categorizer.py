# a. Al inicio del programa colocar los siguientes mensajes en 2 líneas
# diferentes:
# Hola Soy “tu nombre” del grado 9.
# Bienvenido al programa de clasifica de edades.
# b. El usuario debe ingresar su edad, pero si digita un número negativo o un
# número mayor a 110, se le debe indicar que ha cometido un error en la
# digitación del valor y se le volverá pedir que digite su edad hasta que lo haga
# correctamente.
# c. Luego de haber digitado la edad correctamente, el programa debe ser
# capaz de clasificar la edad digitada en una de las categorías que se muestran a
# continuación:
# 1. Infancia (0 a 6 años de edad)
# 2. Niñez (7 a 12 años de edad)
# 3. Adolescencia (13 a 20 años de edad)
# 4. Juventud (21 a 25 años de edad)
# 5. Adultez (26 a 60 años de edad)
# 6. Ancianidad (60 años en adelante)
# d. El programa imprimirá en consola:
# Tu edad es “edad digitada” Ten encuentras en la categoría de “categoría”
# Ejemplo de mensaje en consola, suponiendo que se digito 20: “Tu edad es de 20
# y te encuentras en la categoría de adolescencia”

print("Hola Soy Sergio Ardila del grado 9.")
print("Bienvenido al programa de clasifica de edades.")

category = ""
age = int(input("Ingrese su edad: "))

while age < 0 or age > 110:
    age = int(input("Edad erronea, ingrese su edad otra vez: "))

if age >= 0 and age <= 6:
    category = "Infancia"

if age >= 7 and age <= 12:
    category = "Niñez"

if age >= 13 and age <= 20:
    category = "Adolescencia"

if age >= 21 and age <= 25:
    category = "Juventud"

if age >= 26 and age <= 60:
    category = "Adultez"

if age > 60:
    category = "Ancianidad"

print("Tu edad es: " + str(age) + ", Te encuentras en la categoría de: " + category)

