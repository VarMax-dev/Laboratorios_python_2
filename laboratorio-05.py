# Verificación múltiplos de 3 y 5


numero = int(input("Ingrese un número: "))



if numero % 3 == 0:
	print("El número " + str(numero) + " es múltiplo de 3")
else:
	print("El número " + str(numero) + " no es múltiplo de 3") 
	
if numero % 5 == 0:
	print("El numero " + str(numero) + " es múltiplo de 5")
else:
	print("El número " + str(numero) + " no es múltiplo de 5")
