from itertools import permutations

def is_magic(square):
    # Transforma a lista em uma matriz 3x3
    square = [square[0:3], square[3:6], square[6:9]]
    
    # Soma das linhas
    for row in square:
        if sum(row) != 15:
            return False

    # Soma das colunas
    for col in range(3):
        if square[0][col] + square[1][col] + square[2][col] != 15:
            return False

    # Soma das diagonais
    if square[0][0] + square[1][1] + square[2][2] != 15:
        return False
    if square[0][2] + square[1][1] + square[2][0] != 15:
        return False

    return True

def encontrar_quadrado_magico():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for perm in permutations(numeros):
        if is_magic(perm):
            # Mostra o quadrado mágico encontrado
            print("Quadrado Mágico Encontrado:")
            for i in range(0, 9, 3):
                print(perm[i], perm[i+1], perm[i+2])
            break  # Remove este `break` se quiser encontrar todas as soluções

encontrar_quadrado_magico()
