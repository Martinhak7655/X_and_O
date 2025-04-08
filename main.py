board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = "X"

def draw_board():
    for row in board:
        print(row)

def checkwinner(position1, position2, player):
    if board[position1][0] == player and board[position1][1] == player and board[position1][2] == player:
        print(f"Duq haxteciq {player}")
        return True
    elif board[0][position2] == player and board[1][position2] == player and board[2][position2] == player:
        print(f"Duq haxteciq {player}")
        return True
    elif (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        print(f"Duq haxteciq {player}")
        return True
    return False

while True:
    print("*" * 20)
    draw_board()
    print("*" * 20)
    num1 = int(input(f"Yntreq toxy {player}: "))
    print("*" * 20)
    num2 = int(input(f"Yntreq blocky {player}: "))

    if (num1 < 0 or num1 > 2) or (num2 < 0 or num2 > 2):
        print("Sa sahmanneric durs e, pordzeq noric")
        continue

    if board[num1][num2] != "-":
        print("Dashty arden zbaxvac e, pordzeq noric")
        continue

    board[num1][num2] = player

    if checkwinner(num1, num2, player):
        draw_board()
        break

    if player == "X":
        player = "O"
    else:
        player = "X"