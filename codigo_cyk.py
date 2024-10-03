import time
import matplotlib.pyplot as plt
import numpy as np

def llenar_tabla_cadena_simple(tabla, cadena, gramatica):
    for i, char in enumerate(cadena):
        for lhs, rhs in gramatica:
            if rhs == char:
                tabla[i][i].add(lhs)

def llenar_tabla_subcadenas_largas(tabla, n, gramatica):
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for lhs, rhs in gramatica:
                    if len(rhs) == 2:
                        B, C = rhs
                        if B in tabla[i][k] and C in tabla[k + 1][j]:
                            tabla[i][j].add(lhs)

def algoritmo_cyk(gramatica, cadena):
    n = len(cadena)
    tabla = [[set() for _ in range(n)] for _ in range(n)]
    llenar_tabla_cadena_simple(tabla, cadena, gramatica)
    llenar_tabla_subcadenas_largas(tabla, n, gramatica)
    return 'S' in tabla[0][n - 1]

gramatica_3 = [
    ('S', 'BC'), 
    ('B', 'b'), 
    ('C', 'c')
]

# Probar diferentes longitudes de cadena
longitudes_cadenas = range(1, 21)  # Longitudes de 1 a 20
tiempos_ejecucion = []

for longitud in longitudes_cadenas:
    cadena_prueba = 'b' * longitud  # Crea una cadena con longitud variable
    start_time = time.time()
    algoritmo_cyk(gramatica_3, cadena_prueba)
    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    tiempos_ejecucion.append(tiempo_ejecucion)

# Generar la curva teórica O(n^3)
longitudes = np.array(list(longitudes_cadenas))
complejidad_teorica = longitudes ** 3

# Graficar los resultados
plt.plot(longitudes_cadenas, tiempos_ejecucion, label='Tiempo de ejecución real', marker='o')
plt.plot(longitudes, complejidad_teorica / max(complejidad_teorica) * max(tiempos_ejecucion), 
         label='Complejidad O(n^3)', linestyle='--')

plt.xlabel('Longitud de la cadena')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación entre el tiempo de ejecución real y la complejidad O(n³)')
plt.legend()
plt.grid(True)
plt.show()
