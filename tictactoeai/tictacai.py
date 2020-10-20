import random

wincollection = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

wastechance = {
    1: (2, 3, 4, 5, 7, 9),
    2: (1, 3, 5, 8),
    3: (1, 2, 5, 6, 9, 7),
    4: (1, 5, 7, 6),
    5: (1, 2, 3, 4, 6, 7, 8, 9),
    6: (3, 5, 9, 4),
    7: (4, 5, 8, 9, 1, 3),
    8: (2, 5, 7, 9),
    9: (1, 3, 6, 5, 7, 8)
}


def showboard():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def choosenumber():
    while True:
        a = int(input("choose a cell :  "))
        a -= 1
        try:
            if a in range(0, 9):
                return a
            else:
                print("out of range please choose 0-9")
                continue
        except TypeError:
            print("choose a number 0-9")
            continue


def player1():
    sel1 = choosenumber()
    if board[sel1] == "x" or board[sel1] == "o":
        print("\n this positin before selected , choose another")
        player1()
    else:
        board[sel1] = "x"


def computer():
    selectpalyer = list()
    for i in range(9):
        if board[i] == "x":
            selectpalyer.append(i + 1)
    print(selectpalyer)
 
    if len(selectpalyer) == 1 :
        waste = random.choice(wastechance[selectpalyer[-1]])
        if board[waste - 1] not in ["x", "o"]:
            board[waste - 1] = "o"

    elif len(selectpalyer) > 1:
        for n in wincollection:
            if board[n[0]] == board[n[1]] =="x" :
                board[n[2]] = "o"
            elif board[n[2]] == board[n[1]] =="x" :
                board[n[0]] = "o"
            elif board[n[2]] == board[n[0]] =="x" :
                board[n[1]] = "o"


    else:
        computer()


def reset():
    for i in range(9):
        board[i] = i + 1


def check_state():
    count = 0
    for n in wincollection:

        if board[n[0]] == board[n[1]] == board[n[2]] == "x":
            print("player win")
            return True

        elif board[n[0]] == board[n[1]] == board[n[2]] == "o":
            print("player lose")
            return True

    for cnt in range(9):

        if board[cnt] == "x" or board[cnt] == 'o':
            count += 1

        if count == 9:
            print("game endded without winner !")
            return True


def play():
    end = False
    while not end:
        showboard()
        print("_________")
        end = check_state()
        if end == True:
            break
        player1()
        print()

        showboard()
        print("_________")
        end = check_state()
        if end == True:
            break
        computer()
        print()
    play_again = input("Do you want play again ? (y/n)")
    print("")
    print("")
    if play_again == "y":
        reset()
        play()
    else:
        print("see you again !")


play()
