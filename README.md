# Búsqueda Binaria en Python


# ¿Qué es la búsqueda binaria?

La búsqueda binaria es un algoritmo eficiente para encontrar un elemento dentro de una lista ordenada.  
El algoritmo divide repetidamente el conjunto de datos a la mitad hasta encontrar el valor deseado.

---


# Análisis de complejidad

## Complejidad temporal

| Caso | Complejidad |
|---|---|
| Mejor caso | O(1) |
| Caso promedio | O(log n) |
| Peor caso | O(log n) |

### Explicación

- En cada iteración, la búsqueda binaria reduce el tamaño del problema a la mitad.
- Esto hace que sea mucho más rápida que una búsqueda secuencial en listas grandes.

Ejemplo:

Si existen 1,000,000 de elementos:

- Búsqueda secuencial:
  - Puede revisar hasta 1,000,000 de posiciones.
- Búsqueda binaria:
  - Aproximadamente solo 20 comparaciones.

---

# Casos de uso

La búsqueda binaria es recomendable cuando:

- Los datos están ordenados.
- Se trabaja con grandes cantidades de información.
- Se necesitan búsquedas rápidas y frecuentes.
- Se desea optimizar tiempo de ejecución.

## Ejemplos reales

- Motores de búsqueda.
- Bases de datos indexadas.
- Sistemas de inventario.
- Búsqueda de usuarios o registros.
- Videojuegos y aplicaciones con listas extensas.

---

# Comparativa teórica contra búsqueda secuencial

| Característica | Búsqueda Binaria | Búsqueda Secuencial |
|---|---|---|
| Requiere datos ordenados | Sí | No |
| Complejidad promedio | O(log n) | O(n) |
| Velocidad en listas grandes | Muy rápida | Más lenta |
| Implementación | Moderada | Simple |

## Diferencia principal

La búsqueda secuencial revisa elemento por elemento hasta encontrar el dato.

La búsqueda binaria divide constantemente el conjunto de datos en dos partes, reduciendo significativamente el número de comparaciones necesarias.

---
