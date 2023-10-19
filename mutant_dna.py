import sys

sys.path.append("C:/Users/RYZEN/Desktop/Ejercicio ADN/magneto-mutants")
from functions.mutant_check import is_mutant

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
