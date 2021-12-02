# La funcion calcular mayor
# Tiene que tomar tres números como argumentos
# y devolver el mayor
# Usar condicionales dentro de la función


def calcular_mayor(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
         return b
    else:
         return c
         


print("El mayor es: " + str(calcular_mayor(7,5,10)))
print("El mayor es: " + str(calcular_mayor(1,3,2)))
