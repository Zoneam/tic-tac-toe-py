winning_positions = [
    ['A1', 'B1', 'C1'],
    ['A2', 'B2', 'C2'],
    ['A3', 'B3', 'C3'],
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'B2', 'A3'],
    ['A1', 'B2', 'C3'],
    ['C1', 'C2', 'C3']
]

occupied_positions_x = []
occupied_positions_o = []


def game_init():
    draw_board()
    start_game('X')


def draw_board(occupied_positions_x = [], occupied_positions_o = []):
    list_first = [' ', ' ', ' ']
    list_second = [' ', ' ', ' ']
    list_third = [' ', ' ', ' ']

    for pos in occupied_positions_x:
        if list(pos)[0] == "A":
            y_pos = 0
        if list(pos)[0] == "B":
            y_pos = 1
        if list(pos)[0] == "C":
            y_pos = 2
        if list(pos)[1] == "1":
            list_first[y_pos] = "X"
        if list(pos)[1] == "2":
            list_second[y_pos] = "X"
        if list(pos)[1] == "3":
            list_third[y_pos] = "X"

    for pos in occupied_positions_o:
        if list(pos)[0] == "A":
            y_pos = 0
        if list(pos)[0] == "B":
            y_pos = 1
        if list(pos)[0] == "C":
            y_pos = 2
        if list(pos)[1] == "1":
            list_first[y_pos] = "O"
        if list(pos)[1] == "2":
            list_second[y_pos] = "O"
        if list(pos)[1] == "3":
            list_third[y_pos] = "O"


    print("X--->",list_first)
    print(occupied_positions_x, occupied_positions_o)
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")
    print("        ")
    print(f" A | B | C")
    print("        ")
    print(f" {list_first[0]} | {list_first[1]} | {list_first[2]}")
    print("-----------")
    print(f" {list_second[0]} | {list_second[1]} | {list_second[2]}")
    print("-----------")
    print(f" {list_third[0]} | {list_third[1]} | {list_third[2]}")


def start_game(turn):
    global winning_positions, occupied_positions_o
    while True:
        if turn == "X":
            user_input = input("Player X's Move (example B2):").upper()
            if (user_input not in occupied_positions_o) and (user_input not in occupied_positions_x) and any(user_input in sublist for sublist in winning_positions):
                occupied_positions_x.append(user_input)
                winner = check_for_win(occupied_positions_x)
                if winner:
                    print(f"{turn} is a Winner !!!")
                    break
            else:
                print(f"{user_input} is invalid Input !")
                continue
        else:
            user_input = input("Player O's Move (example C2):").upper()
            if (user_input not in occupied_positions_o) and (user_input not in occupied_positions_x) and any(user_input in sublist for sublist in winning_positions):
                occupied_positions_o.append(user_input)
                winner = check_for_win(occupied_positions_o)
                if winner:
                    print(f"{turn} is a Winner !!!")
                    break
            else:
                print(f"{user_input} is invalid Input !")
                continue

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        draw_board(occupied_positions_x, occupied_positions_o)

# Checking for Winner
def check_for_win(occupied_positions):
    for winning_position in winning_positions:
        if all(item in occupied_positions for item in winning_position):
            return True

game_init()


