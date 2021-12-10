import random
import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = list(alphabet)


def generate_first_row(sudoku_array):
    sudoku_first_row = []
    for i in range(1,10):
        sudoku_first_row.append(i)
    random.shuffle(sudoku_first_row)
    sudoku_array.append(sudoku_first_row)
    return sudoku_array

def rotate_by_three(sudoku_array):
    row = sudoku_array[-1]
    for i in range(2):
        row = row[6:9] + row[0:6]
        sudoku_array.append(row)
    return sudoku_array

def rotate_by_one(sudoku_array):
    row = sudoku_array[-1]
    row = row[-1:] + row[0:8]
    sudoku_array.append(row)
    return sudoku_array


def generate_sudoku_array():
    sudoku_array = []
    sudoku_array = generate_first_row(sudoku_array)
    sudoku_array = rotate_by_three(sudoku_array)
    sudoku_array = rotate_by_one(sudoku_array)
    sudoku_array = rotate_by_three(sudoku_array)
    sudoku_array = rotate_by_one(sudoku_array)
    sudoku_array = rotate_by_three(sudoku_array) # last row_t visszaadni
    return sudoku_array # mentor review
# inkább hosszabb, de érthetőbb legyen

def print_board(board):
    print("      "+"   ".join([str(i) for i in range(1,len(board)+1)]) + "\n")
    print("    +" + "---+"*9)
    for i, row in enumerate(board):
        print(((alpha[i]) + "   |" + " {}   {}   {} |"*3).format(*[x for x in row]))
        if i % 3 == 2:
            print("    +" + "---+"*9)
        else:
            print("    +" + "   +"*9)



def merge_sudoku_array_together(sudoku_array):
    merge_sudoku_array = []
    for elem in sudoku_array:
        merge_sudoku_array += elem
    return merge_sudoku_array


def create_list_of_indices():
    index_list = []
    for i in range(0,81):
        index_list.append(i)
    random.shuffle(index_list)
    return index_list


def create_indicies_of_missings(indexlst, missing_squares):
    not_displayed_numbers = sorted(indexlst[0:missing_squares])
    return not_displayed_numbers

def create_dont_touch_numbers(indexlst, missing_squares):
    displayed_numbers = sorted(indexlst[missing_squares:])
    return displayed_numbers


def hide_numbers(merge_sudoku_array, lst_of_missings, dont_touch_numbers):
    for i in range(len(merge_sudoku_array)):
        for index in lst_of_missings:
            if i == index:
                merge_sudoku_array[i] = '.'
        for forbidden in dont_touch_numbers:
            if i == forbidden:
                merge_sudoku_array[i] = "\033[31m{}\033[00m" .format(merge_sudoku_array[i])
    return merge_sudoku_array


def divide_list_by_nine(big_array):
    divided_list = [big_array[x:x+9] for x in range(0, len(big_array), 9)]
    return divided_list


def search_coordinates(dotted_list):
    list_of_tuples = []
    for i in range(len(dotted_list)):
        for j in range(len(dotted_list[0])):
            if dotted_list[i][j] != ".":
                first_coordinate = (i,)
                second_coordinate = j
                tuple_of_coordinates = first_coordinate + (second_coordinate,)
                list_of_tuples.append(tuple_of_coordinates)
    return list_of_tuples


def validate_user_choice(board, dont_touch_coord):
    user_choice = input("Which square do you want to fill out?" ).upper()
    num_of_rows = len(board)
    num_of_columns = len(board[0])

    valid_rows = [i for i in alpha[0:num_of_columns]]
    valid_cols = [i for i in range(1,num_of_rows+1)]
    
    while True:
        if user_choice == "Q":
            print("Bye_bye!")
            quit()
        elif user_choice[0] in valid_rows and user_choice[1] in str(valid_cols):
            a = alpha.index(user_choice[0])
            b = int(user_choice[1]) - 1
            tapple = (a,)
            whole_tapple = tapple + (b,)
            if whole_tapple in dont_touch_coord:
                print("This field cannot be changed! Choose another one! ")
                user_choice = input("Which square do you want to fill out?" ).upper()
            else:
                return a,b
        else:
            print("Invalid input")
            user_choice = input("Which square do you want to fill out?" ).upper()
            continue

def ask_num_from_1_to_9():
    guessed_number = input("Type number between 1 and 9: ")
    while True:
        if guessed_number not in "123456789":
            print("Please read about how to play sudoku, sweetie!")
            guessed_number = input("Type number between 1 and 9: ")
            continue
        return guessed_number

def fill_board(user_choice, number, board):
    x = user_choice[0]
    y = user_choice[1]
    board[x][y] = number
    return board[x][y]

    
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_win(board):
    point_counter = 0
    for row in board:
        for square in row:
            if square == ".":
                point_counter += 1
    return point_counter


def create_array_to_check(lst):
    filled_array = []
    for element in lst:
        if len(element) > 1:
            to_be_examined = int(element[5])
            filled_array.append(to_be_examined)
        else:
            to_be_examined = int(element)
            filled_array.append(to_be_examined)
    return filled_array


def add_game_mode():
    game_mode = input('''    How brave are you? 😁

    Press 1 for EASY level
    Press 2 for MIDDLE level 
    Press 3 for HARD level 
    Press 4 for DEMO mode 
    
    For qutting the game type 'Q'
    ''')
    console_clear()
    return game_mode



def valid_input_mode(game_mode):
    if game_mode not in '1234Qq':
        print('INVALID INPUT!')
        add_game_mode()
    else:
        if game_mode == '1':
            game_core(40)
        elif game_mode == '2':
            game_core(50)
        elif game_mode == '3':
            game_core(60)
        elif game_mode == '4':
            game_core(1)
        elif game_mode == 'Q' or 'q':
            quit()


def game_core(missing_squares):
    sudoku_array = generate_sudoku_array()
    merged_array = merge_sudoku_array_together(sudoku_array)
    index_list = create_list_of_indices()
    sorted_index_list = create_indicies_of_missings(index_list, missing_squares)
    fix_numbers = create_dont_touch_numbers(index_list, missing_squares)
    dotted_colored_list = hide_numbers(merged_array, sorted_index_list, fix_numbers)
    list_divided_by_9 = divide_list_by_nine(dotted_colored_list)
    print_board(list_divided_by_9)
    dont_touch_coord = search_coordinates(list_divided_by_9)
    while True:
        coordinates = validate_user_choice(list_divided_by_9, dont_touch_coord)
        number = ask_num_from_1_to_9()
        console_clear()
        fill_board(coordinates, number, list_divided_by_9)
        print_board(list_divided_by_9)
        replaced_by_guess = merge_sudoku_array_together(list_divided_by_9)
        point_counter = check_win(list_divided_by_9)
        if point_counter == 0:
            array_to_check = create_array_to_check(replaced_by_guess)
            one_array = merge_sudoku_array_together(sudoku_array)
            if array_to_check == one_array:
                print("\033[33m{}\033[00m" .format("""  ______          _            _   _      _ 
 |  ____|        | |          | | (_)    | |
 | |__ __ _ _ __ | |_ __ _ ___| |_ _  ___| |
 |  __/ _` | '_ \| __/ _` / __| __| |/ __| |
 | | | (_| | | | | || (_| \__ \ |_| | (__|_|
 |_|  \__,_|_| |_|\__\__,_|___/\__|_|\___(_)
                                            """))
                print("You guessed all the numbers!\n")
                quit()


def main():
    print("\033[34m{}\033[00m" .format("""                   __      __            ____            ____           __                  
   _______  ______/ /___  / /____  __   / __/_  ______  / __/___ ______/ /_____  _______  __
  / ___/ / / / __  / __ \/ //_/ / / /  / /_/ / / / __ \/ /_/ __ `/ ___/ __/ __ \/ ___/ / / /
 (__  ) /_/ / /_/ / /_/ / ,< / /_/ /  / __/ /_/ / / / / __/ /_/ / /__/ /_/ /_/ / /  / /_/ / 
/____/\__,_/\__,_/\____/_/|_|\__,_/  /_/  \__,_/_/ /_/_/  \__,_/\___/\__/\____/_/   \__, /  
                                                                                   /____/   """))
    mode = add_game_mode()
    valid_input_mode(mode)
 
main()


