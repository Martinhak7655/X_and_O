board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = "X"

def draw_picture():
    for row in board:
        print(row)

while True:
    draw_picture()
    print("*" * 20)
    num1 = int(input("Yntreq toxy: "))
    print("*" * 20)
    num2 = int(input("Yntreq blocky: "))
    print("*" * 20)

    if (num1 < 0 or num1 > 2) or (num2 < 0 or num2 > 2):
        print("sa sahmanneric dus e, pordzeq noric")
        continue
    if board[num1][num2] != "-":
        print("Dashty arden zbaxvac e, pordzeq noric")
        continue
    
    board[num1][num2] = player
    if player == "X":
        player = "O"
    else:
        player = "X"

