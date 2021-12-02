# Esta función recibe como argumento el nombre de una
# ciudad y retorna su temperatura (en Kelvin) en tiempo real.
# Retorno: float
# Argumento (ciudad): str
def obtener_temperatura(ciudad):
    from urllib.parse import quote
    from urllib.request import urlopen
    import json
    API_KEY = "ad5fa90757c9ab691f25ae08f22a3e19"
    ciudad = quote(ciudad)
    r = urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}")
    if r.getcode() == 200:
        contenido = json.loads(r.read())
        temp = contenido["main"]["temp"]
        return temp
 
 
# ~ # Para hacer:
# ~ # (1) Imprimir en pantalla la temperatura en Buenos Aires.
# ~ # (2) Pedirle el nombre de una ciudad al usuario (vía input())
# ~ #     y mostrar la temperatura en dicha ciudad.
# ~ #     (Londres, London)

print(obtener_temperatura("Buenos Aires"))

temp_user = input("Ingrese el nombre de una ciudad: ")
print(obtener_temperatura(temp_user))

