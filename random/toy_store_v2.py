peso_payaso = 112
peso_muneca = 75
cantidad_payasos= int (input ("Cuantos payason se vendieron "))
cantidad_munecas= int (input ("Cuantas muñecas se vendieron "))
peso_total_payasos= peso_payaso * cantidad_payasos
peso_total_munecas = peso_muneca * cantidad_munecas
peso_total_venta= peso_total_payasos + peso_total_munecas
print ("La cantidad de payasos vendidos fue: "+ str (cantidad_payasos) + " y el peso total de payasos fue: " + str (peso_total_payasos) + " gramos")
print ("La cantidad de muñecas vendidas fue: "+ str (cantidad_munecas) + " y el peso total de muñecas fue: " + str (peso_total_munecas)+ " gramos")
print ("El peso total de la venta es: "+ str (peso_total_venta)+ " gramos")
