# Escribir un programa que pregunte al usuario por el número de
# horas trabajadas y el costo por hora. Después debe mostrar
# por pantalla la paga que le corresponde. (Recuerda que al
# pedir un dato con input queda como STR y debes hacer la
# conversión del tipo de dato correspondiente)

hours = int(input("¿Cuantas horas trabajaste? "))
pay_hour = int(input("Cuanto te pagan por hora? "))
total_pay = hours * pay_hour
print("Tu pago coresponde a: " + str(total_pay) + "$")
