import time

def busqueda_binaria(datos, numero):
    inicio = 0
    fin = len(datos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if datos[medio] == numero:
            return medio
        elif datos[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1



with open("datos.txt", "r") as archivo:
    datos = []

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            datos.append(int(linea))


datos.sort()

numero = int(input("Ingresa el número que quieres buscar: "))

inicio_tiempo = time.perf_counter()

posicion = busqueda_binaria(datos, numero)

fin_tiempo = time.perf_counter()

tiempo_ms = (fin_tiempo - inicio_tiempo) * 1000


if posicion != -1:
    print("Número encontrado")
    print("Número:", numero)
    print("Posición:", posicion)
else:
    print("Número no encontrado")

print("Tiempo de búsqueda:", round(tiempo_ms, 6), "milisegundos")
