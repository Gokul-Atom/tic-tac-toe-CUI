from random import choice

positions = [position for position in range(9)]
all_positions = positions.copy()
board = ["x" for _ in range(9)]
winning_possibilities = ["012", "036", "048", "147", "345", "678", "258", "246"]
board_format = '''
+-------+-------+-------+
|   1   |   2   |   3   |
|-------+-------+-------|
|   4   |   5   |   6   |
|-------+-------+-------|
|   7   |   8   |   9   |
+-------+-------+-------+
'''


def display_board():
    temp_board = board_format
    for i, p in zip(board, all_positions):
        temp_board = temp_board.replace(str(p+1), i)
    print(temp_board.replace("x", " "))


def check_gameover():
    for possibility in winning_possibilities:
        if board[int(possibility[0])] == board[int(possibility[1])] == board[int(possibility[2])] == "X":
            print("You Win!")
            return True
        if board[int(possibility[0])] == board[int(possibility[1])] == board[int(possibility[2])] == "O":
            print("You Lose!")
            return True
        if not positions:
            return True


def player_turn():
    while True:
        try:
            player_move = int(input("Your Move: ")) - 1
        except ValueError:
            print("Position must be an integer.")
            continue

        if not 0 <= player_move <= 8:
            print("Values must be between 1 and 9.")
            continue

        if board[player_move] != "x":
            print("Position already marked.")
        else:
            board[player_move] = "X"
            positions.remove(player_move)
            break


def cpu_turn():
    for possibility in winning_possibilities:
        winning_possibility = []
        if board[int(possibility[0])] == "O":
            winning_possibility.append("O")
        else:
            winning_possibility.append(int(possibility[0]))
        if board[int(possibility[1])] == "O":
            winning_possibility.append("O")
        else:
            winning_possibility.append(int(possibility[1]))
        if board[int(possibility[2])] == "O":
            winning_possibility.append("O")
        else:
            winning_possibility.append(int(possibility[2]))
            print(winning_possibility)
        if winning_possibility.count("O") == 2:
            print(winning_possibility)
            cpu_move = [move for move in winning_possibility if move != "O"][0]
            if cpu_move not in positions:
                continue
            else:
                board[cpu_move] = "O"
                positions.remove(cpu_move)
                return

    if positions:
        cpu_move = choice(positions)
        board[cpu_move] = "O"
        positions.remove(cpu_move)


def main():
    while positions:
        player_turn()
        if check_gameover():
            break
        cpu_turn()
        display_board()
        if check_gameover():
            break


if __name__ == "__main__":
    print("Welcome to TIC TAC TOE")
    display_board()
    main()
    print("Final Board:")
    display_board()
