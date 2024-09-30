def cyk_algorithm(grammar, string):
    """
    Implementación del algoritmo CYK que maneja correctamente las producciones unitarias.
    :param grammar: Diccionario con las reglas de producción de la gramática en forma CNF.
                    Las claves son variables (no terminales) y los valores son listas de posibles producciones.
    :param string: La cadena de entrada a ser analizada.
    :return: Verdadero si la cadena es generada por la gramática, falso en caso contrario.
    """
    n = len(string)  # Obtiene la longitud de la cadena de entrada

    # Crear la tabla n x n
    # Se crea una tabla de sets vacíos, cada celda representará variables no terminales que pueden generar la subcadena correspondiente.
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar la primera fila con las reglas de producción para los símbolos terminales
    # Se recorre cada posición de la cadena para buscar qué variables generan los símbolos terminales.
    for i in range(n):
        for variable, productions in grammar.items():  # Recorre las variables y sus producciones
            for production in productions:
                if len(production) == 1 and production[0] == string[i]:  # Si la producción es un terminal que coincide con el símbolo en la cadena
                    table[i][i].add(variable)  # Se agrega la variable que genera ese terminal a la celda correspondiente.

    # Mostrar la tabla inicial con las producciones para terminales
    print("Tabla inicial con producciones para terminales:")
    for row in table:
        print(row)

    # Rellenar la tabla para combinaciones de producciones binarias
    # Ahora se analizan combinaciones de subcadenas de mayor longitud, comenzando por 2.
    for length in range(2, n + 1):  # Itera sobre todas las longitudes posibles de subcadenas
        for i in range(n - length + 1):  # Define el inicio de la subcadena
            j = i + length - 1  # Define el final de la subcadena
            for k in range(i, j):  # Divide la subcadena en dos partes
                # Combinamos las variables de las celdas [i][k] y [k+1][j] (particiones)
                for B in table[i][k]:  # Recorre las variables en la primera partición
                    for C in table[k + 1][j]:  # Recorre las variables en la segunda partición
                        # Verificamos si existe una producción A -> BC en la gramática
                        for A, productions in grammar.items():  # Recorre todas las producciones de la gramática
                            if [B, C] in productions:  # Si existe una producción A -> BC
                                table[i][j].add(A)  # Se añade A a la celda correspondiente en la tabla

    # Verificar producciones unitarias (como S -> C)
    # Busca producciones unitarias, es decir, variables que generan otras variables directamente.
    for i in range(n):
        for j in range(i, n):
            added = True  # Variable que indica si se han agregado nuevas variables a la celda
            while added:  # Repite el proceso mientras se sigan añadiendo variables
                added = False
                for variable, productions in grammar.items():
                    for production in productions:
                        if len(production) == 1 and production[0] in table[i][j]:  # Si hay una producción unitaria
                            if variable not in table[i][j]:  # Si la variable aún no está en la celda
                                table[i][j].add(variable)  # Añadir la variable a la celda
                                added = True  # Indica que se ha agregado una nueva variable

    # Mostrar la tabla final después de rellenar
    print("\nTabla final después de rellenar:")
    for row in table:
        print(row)

    # Verificamos si el símbolo inicial (S) está en la parte superior derecha de la tabla
    # Si 'S' está en la celda [0][n-1], la cadena es aceptada por la gramática.
    return 'S' in table[0][n - 1]

# Nueva gramática para aceptar tanto 'ab' como 'c'
grammar = {
    'S': [['A', 'B'], ['C']],  # S -> AB o S -> C
    'A': [['a']],               # A -> a
    'B': [['b']],               # B -> b
    'C': [['c']]                # C -> c
}

# Solicitar la cadena a verificar desde la terminal
if __name__ == "__main__":
    string = input("Introduce la cadena a verificar: ")  # Solicita la cadena de entrada al usuario
    result = cyk_algorithm(grammar, string)  # Llama a la función que ejecuta el algoritmo CYK
    if result:
        print("\nLa cadena pertenece al lenguaje.")  # Si el resultado es verdadero, la cadena pertenece al lenguaje.
    else:
        print("\nLa cadena NO pertenece al lenguaje.")  # Si el resultado es falso, la cadena no pertenece al lenguaje.
