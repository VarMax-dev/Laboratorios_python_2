# Solicitaar un número al usuario, que a su vez representa la cantidad de nombres a ingresar para guardarse en lista

number = input("Ingrese un número por favor: ")

while not number.isdecimal():
    print("error")
    number = (input("Ingrese un número por favor: "))
    
number = int(number)

names = input("Ingrese " + str(number) + " nombres por favor: ")
    
list = []
list.append([names])

for name in list:
    print("Los nombres dentro de la lista son: ", names)
