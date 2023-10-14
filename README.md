# Ejercicio Magneto

## Introduccion
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.

Te ha contratado a ti para que desarrolles un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.

Para eso te ha pedido crear un programa con un método o función con la siguiente firma:

  **def is_mutant(dna):**

## Funcionamiento

Se recibirá como parámetro un array de Strings que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.

Se sabrá si un humano es mutante, si se encuentra **MAS DE UNA SECUENCIA** de cuatro letras iguales, de forma oblicua, horizontal o vertical.

Las filas de la matriz a verificar se ingresan por teclado.

Ejemplo de input: '**ATCGTA**' (esto equivale a una fila de la matriz)

Una vez cargada correctamente la misma, se aplica una función que verifica si hay presencia en la matriz de mutantes o no y se devuelve el resultado al usuario en base a eso.

## Logica

Al recibir la matriz con el formato correcto (validado anteriormente), se verifican las filas, columnas y diagonales primarias, secundarias y terciarias, iterando en la matriz principal con un bucle for y comprension de lista. Una vez obtenida la nueva lista, se la pasa como parametro a un lambda, que se encarga de verificar la ocurrencia de 4 letras seguidas en esa sublista. La funcion lambda es la siguiente:

    check_pattern = lambda data: any(data[i:i+4].count(data[i]) == 4 for i in range(len(data) - 3))


## Ejemplos de ADN

Ejemplo de matriz **MUTANTE**:

['A', '**T**', 'A', 'A', 'T', 'G']

['**G**', 'T', '**T**', 'A', 'G', 'T']

['**G**', 'A', 'C', '**T**', 'C', 'G']

['**G**', 'T', 'G', 'A', '**T**', 'G']

['**G**', 'T', 'A', 'G', 'T', 'C']

['**A**', '**A**', '**A**', '**A**', 'T', 'A']

Ejemplo de matriz **NO MUTANTE**:

['A', 'T', 'G', 'A', 'T', 'G']

['G', 'T', 'C', 'T', 'T', 'A']

['A', 'A', 'T', 'T', 'G', 'G']

['A', 'C', 'T', 'A', 'G', 'T']

['G', 'G', 'A', 'T', 'T', 'C']

['A', 'G', 'G', 'C', 'A', 'A']

## Pruebas Unitarias

Se incluyen casos de pruebas contemplando todos los patrones posibles (en filas, columnas y diagonales).
