#Paulina Ivonne Cortés Díaz
#A01568040

#Imprime mi sudoku
def mostrar_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" "),
        print()

#Crear una funcion para llamar la matriz

def leer_sudoku():
    
    #COMENZAR A TRANSCRIBIR LA MATRIZ
    
    # Leer archivo de texto
    with open('Inputs/Input.txt') as f:
        lines = f.readlines()
    
    # Crear matriz vacia
    #Escribe un 0 nueve veces nueve veces para crear la matriz
    mat = [[0 for i in range(9)]for i in range(9)]
    
    # Quita lineas horizontales
    #Lineas dibujadas en el texto, SOLO GUARDA LAS QUE NO SEAN IGUALES A ESTAS
    lines = [line for line in lines if line != '---------+---------+---------\n']
    
    
    #Un enumerate se usa cuando tengo un arreglo hace un objeto de lo de mi arreglo, con el for te indica el índice del arreglo seguido por el valor. 
    for i, line in enumerate(lines):
        #Comprobar que si sea guardado correctamente
        print(i, line)
        # Quita espacio inicial y '\n' final
        line = line.strip()
    
        # Saltear linea horizontal
        if line == '---------+---------+---------':
            print('continue')
            i -= 1
            continue
        
        # Quita '|' lineas divisoras
        line = line.replace('|', '')
    
        # Separa en numeros
        nums = line.split()
        #print (nums)
    
        # Llena matriz recorriendo j que tiene el indice y n que tiene el número. 
        #Recorre en el renglon de la linea, esribe 0 si el numero es un punto y si no escribe el número. 
        for j, n in enumerate(nums):
            mat[i][j] = 0 if n == '.' else int(n)
    
    for line in mat:
        print(line)

    return mat

sudoku = leer_sudoku()

#PROBLEM SOLVING AGENT

#Espacio de estados 9 factorial por 9 factorial

#Estado inicial, sudoku con datos de inicio solamente

#Acciones a tomar es colocar un numero en mi bloque

#Prueba de meta no hay espacios vacios y se cumplen las reglas de no repetir numeros en filas ni columnas

#Costo del camino, todos son iguales (1) 

#VALIDACION DE SUDOKU

#Eliminar los 0, cualquier n que no sea 0 va a ser verdadero

def validar_sudoku(sudoku, row, col, num):

    #Iteración por filas
    for row in sudoku:
        row = [n for n in row if n]
        print (row)

        # Convertir a conjunto y comparar tamaños
        #Conjunto ignora orden e ignora repeticiones
        # Si no son iguales, significa que se repite un número, no es válido

        if len(row) != len(set(row)):
            return False
        
    #Iteracion por columnas
    # zip * sudoku regresa la matriz transpuesta iterando sobre las filas que representan las columnas 
    for col in zip(*sudoku):
        col = [n for n in col if n]
        
        # Convertir a conjunto y comparar tamaños
        # Conjunto ignora orden e ignora repeticiones
        # Si no son iguales, significa que se repite un número, no es válido
        if len(col) != len(set(col)):
            return False
        
    #Crear los bloques individuales
    #Defino mi bloque como mi propio arreglo 
    block_1 = []
    block_2 = []
    block_3 = []
    block_4 = []
    block_5 = []
    block_6 = []
    block_7 = []
    block_8 = []
    block_9 = []

    # Poblar los bloques fila por fila
    
    #Array splice, tengo en donde inicio, en donde termino y tamaño del paso, inicio en 0 y termino en 3 INICIO EXCLUSIVO [)
    #Extend tengo arreglos y los pega en un solo arreglo pero no uno dentro del otro solo unidos
    
    for row in sudoku[:3]:
        block_1.extend(row[0:3])
        block_2.extend(row[3:6])
        block_3.extend(row[6:9])

    for row in sudoku[3:6]:
        block_4.extend(row[0:3])
        block_5.extend(row[3:6])
        block_6.extend(row[6:9])
        
    for row in sudoku[6:9]:
        block_7.extend(row[0:3])
        block_8.extend(row[3:6])
        block_9.extend(row[6:9])
        
    blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9]
    for block in blocks:
        block = [n for n in block if n]
        if len(block) != len(set(block)):
            return False
        
    return True

def en_fila(sudoku,row,num):
    return num in sudoku [row]


def en_columna(sudoku,col,num):
    for i in range (9):
        if sudoku[1][col]== num:
            return True
    return False
    
    
#Busca el numero en su bloque correspondiente
def en_bloque(sudoku, row, col, num):
    for i in range(3):
        for j in range(3):
            if (sudoku[i + row][j + col] == num):
                return True
    return False

#Valida que se puede incertar dentro de mi sudoku 
def se_puede_insertar(sudoku, row, col, num):  
    return (not en_fila(sudoku, row, num)) and (not en_columna(sudoku, col, num)) and (not en_bloque(sudoku, row - row % 3, col - col % 3, num))

#RESOLVER EL SUDOKU!!!! YIPPY

#Checa el sudoku y busca si hay un espacio vacio representado con 0's si tiene es True y actualiza l y si no tiene es False

def encontrar_vacio(sudoku, l):
    for row in range(9):
        for col in range(9):
            if (sudoku[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

# RESOLVER SUDOKU
sudoku = leer_sudoku()

# Basado en la solucion de Backtracking de GeeksForGeeks usando mi propia funcion de validacion y sin recursion

def resolver(sudoku):
    # l Tiene informacion de que celda se esta resolviendo si todas las celdas estabn resueltas ya se termina el Sudoku
    l = [0, 0]

    if (not encontrar_vacio(sudoku, l)):
        return True

    # Asignar listas de la funcion a columnas y filas
    row = l[0]
    col = l[1]

    # Solamente toma en cuenta los numeros del 1 al 9
    for num in range(1, 10):
        if se_puede_insertar (sudoku, row, col, num):
            #Asignamos numero
            sudoku[row][col]=num
            #Resolvemos para este nuevo sudoku
            if resolver(sudoku):
                return True
            #No es numero correcto reiniciamos a 0
            sudoku[row][col]=0

    #Triggerear backtracking
    return False

if resolver (sudoku):
    mostrar_sudoku(sudoku)
else:
    print("No se puede resolver")