# Complejidad Algoritmo CYK

*Participantes:*
- Bryan Ariza
- Manuel Cardena
- Andres Toledo
- Juan Wilches

---
## Descripción
Este proyecto implementa el algoritmo CYK (Cocke-Younger-Kasami), el programa genera una gráfica que compara el tiempo real de ejecución del algoritmo CYK con su complejidad teórica 𝑂(𝑛^3), mostrando cómo escala el rendimiento del algoritmo a medida que la longitud de la cadena aumenta.
## Instrucciones de uso

### 1. Descargar el Archivo CYK

Antes de comenzar, debes descargar el archivo necesario desde este repositorio de GitHub llamado codigo_cyk.py. 

### 2. Abre una terminal en Linux
Primero, abre la terminal de tu sistema operativo Linux. Este será el entorno donde se ejecutarán los comandos para la instalación y uso del analizador léxico.

### 3. Ejecuta el Archivo Principal del Analizador Léxico
Para poder ejecutar el codigo codigo_cyk.py Utiliza el siguiente comando en la terminal:
```bash
python3 codigo_cyk.py
```
El código crea una tabla para ver cómo se puede derivar la cadena usando las reglas de la gramática. Luego, mide el tiempo que realmente tarda el algoritmo en procesar cadenas de distintos tamaños y lo compara con el tiempo esperado teóricamente, que sigue la complejidad 𝑂(𝑛^3). Esto significa que, si la cadena crece en longitud, el tiempo de ejecución debería aumentar aproximadamente con el cubo de esa longitud. Al final, se genera un gráfico para mostrar cómo cambia el tiempo de ejecución a medida que las cadenas se vuelven más largas.

![image](https://github.com/user-attachments/assets/41d54c14-2335-40e7-a581-107f7332f2e5)


