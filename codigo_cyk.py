def cyk_algorithm(grammar, string):
    """
    Implementación del algoritmo CYK.
    :param grammar: Diccionario con las reglas de producción de la gramática en forma CNF.
                    Claves son variables (no terminales), valores son listas de posibles producciones.
    :param string: La cadena de entrada a ser analizada.
    :return: Verdadero si la cadena es generada por la gramática, falso en caso contrario.
    """
    n = len(string)
    # Crear la tabla n x n
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Poblamos la primera fila con las reglas de producción para los símbolos terminales
    for i in range(n):
        for variable, productions in grammar.items():
            for production in productions:
                if production == string[i]:
                    table[i][i].add(variable)
    
    # Mostramos la tabla inicial
    print("Tabla inicial con producciones para terminales:")
    for row in table:
        print(row)
    
    # Rellenamos la tabla
    for length in range(2, n+1):  # Longitud de la subcadena
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j):
                # Combinamos las variables de las celdas [i][k] y [k+1][j]
                for B in table[i][k]:
                    for C in table[k+1][j]:
                        # Verificamos si existe una producción A -> BC en la gramática
                        for A in grammar:
                            if (B, C) in grammar[A]:
                                table[i][j].add(A)
    
    # Mostramos la tabla final
    print("\nTabla final después de rellenar:")
    for row in table:
        print(row)

    # Verificamos si el símbolo inicial (S) está en la parte superior derecha de la tabla
    return 'S' in table[0][n-1]

# Gramática ajustada en forma CNF
grammar = {
    'S': [('A', 'B')],    # S -> AB
    'A': [('C', 'D')],    # A -> CD
    'B': [('C', 'D')],    # B -> CD
    'C': ['a'],           # C -> a
    'D': ['b']            # D -> b
}

# Solicitar la cadena a verificar desde la terminal
if __name__ == "__main__":
    string = input("Introduce la cadena a verificar: ")
    result = cyk_algorithm(grammar, string)
    if result:
        print("\nLa cadena pertenece al lenguaje.")
    else:
        print("\nLa cadena NO pertenece al lenguaje.")
