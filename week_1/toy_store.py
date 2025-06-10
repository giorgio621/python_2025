# #Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y muñecas. Suele hacer venta por correo y la
# empresa de logística les cobra por peso de cada paquete así
# que deben calcular el peso de los payasos y muñecas que
# saldrán en cada paquete a demanda. Cada payaso pesa
# 112 g y cada muñeca 75 g. Escribir un programa que lea el
# número de payasos y muñecas vendidos en el último pedido y
# calcule el peso total del paquete que será enviado.

clown_weight = 112
doll_weight = 75
clown_amount = int(input("¿Cuantos payasos se vendieron? "))
doll_amount = int(input("¿Cuantas muñecas se vendieron? "))
clown_total = clown_weight * clown_amount
doll_total = doll_weight * doll_amount
total = doll_total + clown_total
print("El peso total es: " + str(total) + "gr")
