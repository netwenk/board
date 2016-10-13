#!/usr/bin env python
#! -*- coding: utf-8 -*-

'''
9宫格连线游戏
人类跟机器人世纪巅峰对战 堪比深蓝
'''

#定义全局变量
SQUARES_NUM = 9  #棋盘方格数量
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"

def main():
    show_welcome()
    trun = X
    person, computer = pieces()
    board = new_board()
    display_board(board)

    while not wins(board):
        if trun == person:
            move = person_move(board)
            board[move] = person
        else:
            move = computer_move(board, computer, person)
            board[move] = computer

        display_board(board)
        trun = next_trun(trun)

    winner = wins(board)
    congrat_winner(winner, computer, person)

def show_welcome():
    print(
        """
            欢迎进入9宫格连线游戏

            输入一个数字 如：0-8
            该数字将会对应到方格的位置

                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8

            让我们开始这个游戏吧！\n\n
        """
    )

def ask_yes_no(question):
    response = None

    while response not in ("y", "n"):
        response = input(question).lower()

    return response


def pieces():
    go_first = ask_yes_no("你要先走第一步吗? (y/n)")
    
    if go_first == "y":
        print("\n 你先走")
        person = X
        computer = O
    else:
        print("\n对方先走")
        person = O
        computer = X

    return person, computer


def new_board():
    board = []
    for square in range(SQUARES_NUM):
        board.append(EMPTY)

    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------");
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------");
    print("\t", board[6], "|", board[7], "|", board[8])
    print("\t", "----------");


def legal_moves(board):
    moves = []

    for square in range(SQUARES_NUM):
        if board[square] == EMPTY:
            moves.append(square)

    return moves


def wins(board):
    wins = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
        )

    for row in wins:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def person_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("请输入你要连线的方格数字(0-8): ", 0, SQUARES_NUM)
        if move not in legal:
            print("\n该方格已被占用，请换一个输入\n")

    return move


def computer_move(board, computer, person):
    board_bak = board[:]

    best_square = (4, 0, 2, 4, 8, 1, 3, 5, 7)

    print("\n计算机选择方格: ", end=" ")
    for move in legal_moves(board_bak):
        board_bak[move] = computer
        if wins(board_bak) == computer:
            print(move)
            return move

        board_bak[move] = EMPTY

    for move in legal_moves(board_bak):
        board_bak[move] = person
        if wins(board_bak) == person:
            print(move)
            return move

        board_bak[move] = EMPTY


    for move in best_square:
        if move in legal_moves(board_bak):
            print(move)
            return move


def next_trun(trun):
    if trun == X:
        return O
    else:
        return X

def ask_number(question, low, high):
    response = None

    while response not in range(low, high):
        response = int(input(question))

    return response


def congrat_winner(winner, computer, person):
    if winner == computer:
        print("\n You lose")
    elif winner == person:
        print("\n You win")
    elif winner == TIE:
        print("平局")


if __name__ == '__main__':
    main()
