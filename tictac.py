import os


def clear_console():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Winning Positions
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
o_wins = 0
x_wins = 0

times_to_play = int(input("How Many Rounrs You Want To Play ? :"))


# Game initialization
def game_init():
    draw_board()
    start_game('X')

# Drawing board
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
            
    print("  \033[91m----------------------\033[0m")
    print("  \33[7mLet's play Py-Pac-Poe!\033[0m")
    print("  \033[91m----------------------\033[0m")
    print("        ")
    print(f"\33[35m      A | B | C\033[0m")
    print("        ")
    print(f"1)    {list_first[0]} \033[32m|\033[0m {list_first[1]} \033[32m|\033[0m {list_first[2]}")
    print("\033[32m     -----------\033[0m")
    print(f"2)    {list_second[0]} \033[32m|\033[0m {list_second[1]} \033[32m|\033[0m {list_second[2]}")
    print("\033[32m     -----------\033[0m")
    print(f"3)    {list_third[0]} \033[32m|\033[0m {list_third[1]} \033[32m|\033[0m {list_third[2]}")
    print("        ")
    print("  \033[91m-----------------\033[0m")
    print(f"  \33[7m X score {x_wins} \033[0m")
    print(f"  \33[7m O score {o_wins} \033[0m")
    print("  \033[91m-----------------\033[0m")


def start_game(turn):
    global winning_positions, occupied_positions_o, x_wins, o_wins
    while True:
        if turn == "X":
            user_input = input("Player X's Move (example B2):").upper()
            if (user_input not in occupied_positions_o) and (user_input not in occupied_positions_x) and any(user_input in sublist for sublist in winning_positions):
                occupied_positions_x.append(user_input)
                winner = check_for_win(occupied_positions_x)
                if winner:
                    print(f"\x1b[6;30;42m {turn} is the Winner !!!\033[0m")
                    o_wins += 1
                    clear_console()
                    draw_board(occupied_positions_x, occupied_positions_o)
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
                    print(f"\x1b[6;30;42m {turn} is the Winner !!!\033[0m")
                    x_wins += 1
                    clear_console()
                    draw_board(occupied_positions_x, occupied_positions_o)
                    break
            else:
                print(f"{user_input} is invalid Input !")
                continue

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        if len(occupied_positions_x) + len(occupied_positions_o) == 9:
            print(f"It is a Tie !")
            break
        clear_console()
        draw_board(occupied_positions_x, occupied_positions_o)


# Checking for Winner
def check_for_win(occupied_positions):
    for winning_position in winning_positions:
        if all(item in occupied_positions for item in winning_position):
            return True


for times in range(times_to_play):
    occupied_positions_x = []
    occupied_positions_o = []
    clear_console()
    game_init()

    
