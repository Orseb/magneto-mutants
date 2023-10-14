def is_mutant(dna):
    
    # Funcion lambda que recorre una lista y comprueba si hay cuatro coincidencias entre los elementos
    check_pattern = lambda data: any(data[i:i+4].count(data[i]) == 4 for i in range(len(data) - 3))
    
    # Variable que se va a encargar de contar los patrones que se encuentren
    found_patterns = 0

    # Verificamos los patrones en las filas
    for row in dna:
        if check_pattern(row):
            found_patterns += 1

    # Verificamos los patrones en las columnas
    for j in range(6):
        column = [dna[i][j] for i in range(6)]
        if check_pattern(column):
            found_patterns += 1

    # Verificamos los patrones en las diagonales principales
    main_diagonal1 = [dna[i][i] for i in range(6)]
    main_diagonal2 = [dna[5-i][i] for i in range(5, -1, -1)]

    if check_pattern(main_diagonal1):
        found_patterns += 1

    if check_pattern(main_diagonal2):
        found_patterns += 1

    # Verificamos los patrones en las diagonales secundarias izquierdas
    secondary_diagonal1 = [dna[i][i-1] for i in range(1, 6)]
    secondary_diagonal2 = [dna[i-1][i] for i in range(1, 6)]

    if check_pattern(secondary_diagonal1):
        found_patterns += 1

    if check_pattern(secondary_diagonal2):
        found_patterns += 1

    # Verificamos los patrones en las diagonales secundarias derechas
    secondary_diagonal3 = [dna[5-i][i-1] for i in range(5, 0, -1)]
    secondary_diagonal4 = [dna[5-i][i+1] for i in range(4, -1, -1)]

    if check_pattern(secondary_diagonal3):
        found_patterns += 1

    if check_pattern(secondary_diagonal4):
        found_patterns += 1

    # Verificamos los patrones en las diagonales terciarias izquierdas
    tertiary_diagonal1 = [dna[i][i-2] for i in range(2, 6)]
    tertiary_diagonal2 = [dna[i][i+2] for i in range(4)]

    if check_pattern(tertiary_diagonal1):
        found_patterns += 1

    if check_pattern(tertiary_diagonal2):
        found_patterns += 1

    # Verificamos los patrones en las diagonales terciarias derechas
    tertiary_diagonal3 = [dna[5-i][i-2] for i in range(5, 1, -1)]
    tertiary_diagonal4 = [dna[6-i][i+1] for i in range(4, 0, -1)]

    if check_pattern(tertiary_diagonal3):
        found_patterns += 1

    if check_pattern(tertiary_diagonal4):
        found_patterns += 1

    # Devolvemos la comprobacion
    return found_patterns > 1


if __name__ == '__main__':

    dna = []

    # Por cada una de las 6 filas
    for x in range(6):

        while True:
            
            # Pedimos las 6 letras de la fila 
            row = list(input(f"Ingrese los 6 elementos de la fila {x+1}: ").upper())

            # Hasta que no se cumpla la condicion de que tenga 6 letras y sean letras validas no salimos del bucle
            if len(row) == 6 and all(x in 'ATCG' for x in row):
                dna.append(row)
                break
            else:
                print("Ingrese la cantidad correcta de elementos y/o letras permitidas")
    
    # Mostramos el ADN
    print("Las bases nitrogenadas del ADN son:")
    for base in dna:
        print(base)

    # Guardamos el resultado en una variable
    result = is_mutant(dna)
    
    # Mostramos el resultado
    print(f"La persona es mutante? {result}")
