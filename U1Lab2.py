#Convertir Dias en anios, semanas y dias

#Pedimos el ingreso de la cantidad de DIAS a CONVERTIR
numDias = int(input('Cantidad de dias a Ingresar: '))

#Division para obtener el numero de años, usando doble slash para que salga un numero entero
anios = numDias//(365)
#Division para obtener numero de semanas
semanas = (numDias//7)
#Usamos una resta con el numero de dias por lo resultante del producto de semanas con su cantidad respectiva 
#para ver los dias restantes 
dias = numDias-(semanas * 7)

#Funciones print imprimen los resultados 
print('Años: ', anios)
print('Semanas: ', semanas)
print('Dias: ', dias)
