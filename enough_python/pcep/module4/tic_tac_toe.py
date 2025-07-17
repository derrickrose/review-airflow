import random
from time import sleep

COMPUTER_TOKEN = "X"
USER_TOKEN = "0"
GAME_POSITION_MAP = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0),
                     "8": (2, 1), "9": (2, 2)}


def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------+-------+-------+")
    for table in board:
        print("|  ", table[0], "  |  ", table[1], "  |  ", table[2], "  |")
        print("+-------+-------+-------+")


def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        game = input("What will be your game?? ")
        try:
            if 1 <= int(game) <= 9:
                print("Your game", game)
                if is_valid_game(board, game):
                    print("The game", game, "is valid!!!")
                    board[GAME_POSITION_MAP[game][0]][GAME_POSITION_MAP[game][1]] = USER_TOKEN
                    break
                else:
                    print("The game is already played!!!")
            else:
                print("You must select a game-play within 1 and 9")
        except Exception as e:
            print(e)
            print("You must enter a number between 1 and 9")
    return board


def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                free_fields.append((i, j))
    return free_fields


def is_valid_game(board, game):
    position = GAME_POSITION_MAP[game]
    print("position", position)
    free_fields = MakeListOfFreeFields(board)
    for field in free_fields:
        if position[0] == field[0] and position[1] == field[1]:
            return True
    return False


def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    position_y, position_x = random.choice(MakeListOfFreeFields(board))
    print("Draw move position (", position_y, ",", position_x, ")")
    print("Game played by the computer", board[position_y][position_x])
    board[position_y][position_x] = COMPUTER_TOKEN
    return board


def is_game_over(board):
    if not VictoryFor(board, COMPUTER_TOKEN) and not VictoryFor(board, USER_TOKEN) and not len(
            MakeListOfFreeFields(board)) == 0:
        return False

    if VictoryFor(board, COMPUTER_TOKEN):
        return True, "Computer"

    if VictoryFor(board, USER_TOKEN):
        return True, "User"

    if len(MakeListOfFreeFields(board)) == 0:
        return True, "Nobody"


if __name__ == "__main__":
    board = []
    index = 1
    for i in range(3):
        table = []
        for j in range(3):
            table.append(index)
            index += 1
        board.append(table)

    DisplayBoard(board)
    # first move always machine, put X in the center
    print("First move is always machine, put X in the center")
    board[1][1] = COMPUTER_TOKEN
    DisplayBoard(board)

    while True:
        if val := is_game_over(board):
            print("Game over!!!")
            if val[1]:
                print("Winner is", val[1])
            break
        # print(MakeListOfFreeFields(board))
        board = EnterMove(board)
        DisplayBoard(board)

        if val := is_game_over(board):
            print("Game over!!!")
            if val[1]:
                print("Winner is", val[1])
            break

        sleep(5)
        board = DrawMove(board)
        DisplayBoard(board)
