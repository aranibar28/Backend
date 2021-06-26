coordenadas = [
    [1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]
]


def imprimirMatriz():
    '''
    Función para imprimir la matriz Tic Tac Toe
    '''

    print(' Esta es la matriz de coordenadas ')
    print('''
    ''')

    print('', coordenadas[0][0], '\t', coordenadas[0]
          [1], '\t', coordenadas[0][2])
    print('', coordenadas[1][0], '\t', coordenadas[1]
          [1], '\t', coordenadas[1][2])
    print('', coordenadas[2][0], '\t', coordenadas[2]
          [1], '\t', coordenadas[2][2])
    print('')


def victoria():
    '''
    Esta función define si un jugador ha ganado y, si es así, quién ha ganado antes de permitir
    la ejecución de la función del turno de juego.
    '''

    if coordenadas[0][0] == 1 and coordenadas[0][1] == 1 and coordenadas[0][2] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[1][0] == 1 and coordenadas[1][1] == 1 and coordenadas[1][2] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[2][0] == 1 and coordenadas[2][1] == 1 and coordenadas[2][2] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][0] == 1 and coordenadas[1][0] == 1 and coordenadas[2][0] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][1] == 1 and coordenadas[1][1] == 1 and coordenadas[2][1] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][2] == 1 and coordenadas[1][2] == 1 and coordenadas[2][2] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][0] == 1 and coordenadas[1][1] == 1 and coordenadas[2][2] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][2] == 1 and coordenadas[1][1] == 1 and coordenadas[2][0] == 1:
        ganador = 'si'
        jugador = 'jugador 1'

    elif coordenadas[0][0] == 2 and coordenadas[0][1] == 2 and coordenadas[0][2] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[1][0] == 2 and coordenadas[1][1] == 2 and coordenadas[1][2] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[2][0] == 2 and coordenadas[2][1] == 2 and coordenadas[2][2] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[0][0] == 2 and coordenadas[1][0] == 2 and coordenadas[2][0] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[0][1] == 2 and coordenadas[1][1] == 2 and coordenadas[2][1] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[0][2] == 2 and coordenadas[1][2] == 2 and coordenadas[2][2] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[0][0] == 2 and coordenadas[1][1] == 2 and coordenadas[2][2] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    elif coordenadas[0][2] == 2 and coordenadas[1][1] == 2 and coordenadas[2][0] == 2:
        ganador = 'si'
        jugador = 'jugador 2'

    else:
        ganador = 'no'

    if ganador == 'si':
        print('El juego ha terminado! ',  jugador, ' ganador!')
        exit(0)


print(imprimirMatriz(),
      victoria())
