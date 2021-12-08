import random
import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = list(alphabet)
sudoku_array = []


def generate_first_row():
    sudoku_first_row = []
    for i in range(1,10):
        sudoku_first_row.append(i)
    random.shuffle(sudoku_first_row)
    sudoku_array.append(sudoku_first_row)
    return sudoku_first_row

def rotate_by_three(row):
    for i in range(2):
        row = row[6:9] + row[0:6]
        sudoku_array.append(row)
    return row

def rotate_by_one(row):
    row = row[-1:] + row[0:8]
    sudoku_array.append(row)
    return row


def generate_sudoku_array():
    first_row = generate_first_row()
    sec_and_third = rotate_by_three(first_row)
    fourth = rotate_by_one(sec_and_third)
    fifth_and_sixth = rotate_by_three(fourth)
    seventh = rotate_by_one(fifth_and_sixth)
    eigtht_and_ninth = rotate_by_three(seventh)
    return eigtht_and_ninth


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


def create_hard_board(indexlst):
    create_60_missing_hard = sorted(indexlst[0:60])
    return create_60_missing_hard

def create_dont_touch_numbers(indexlst):
    rest_indicies_of_hard = sorted(indexlst[60:])
    return rest_indicies_of_hard


def hide_numbers(merge_sudoku_array, lst_with_zeros, dont_touch_numbers):
    for i in range(len(merge_sudoku_array)):

        for index in lst_with_zeros:

            if i == index:
                merge_sudoku_array[i] = '.'
        for tiltott in dont_touch_numbers:
            if i == tiltott:
                merge_sudoku_array[i] = "\033[91m{}\033[00m" .format(merge_sudoku_array[i])
    return merge_sudoku_array



def paint_to_red(board):
    for row in board:
        for element in row:
            if element != ".":
                element = prRed(element)

def divide_list_by_nine(lista):
    divided_list = [lista[x:x+9] for x in range(0, len(lista), 9)]
    return divided_list


def search_coordinates(nullásitott):
    list_of_tuples = []
    for i in range(len(nullásitott)):
        for j in range(len(nullásitott[0])):
            if nullásitott[i][j] != ".":
                c = (i,)
                f = j
                tup = c + (f,)
                list_of_tuples.append(tup)
    return list_of_tuples


def validate_user_choice(board, dont_touch_coord):
    user_choice = input("Which square do you want to fill out?" ).upper()
    sorok_szama = len(board)
    oszlopok_szama = len(board[0])

    valid_rows = [i for i in alpha[0:oszlopok_szama]]
    valid_cols = [i for i in range(1,sorok_szama+1)]
    
    
    
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
                print("This field cannot be changed! Choose another one babe! ")
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


def main():
    generate_sudoku_array()
    merged_array = merge_sudoku_array_together(sudoku_array)
    print(merged_array)
    index_list = create_list_of_indices()
    hard_board = create_hard_board(index_list)
    red_nums = create_dont_touch_numbers(index_list)
    divided = hide_numbers(merged_array, hard_board, red_nums)
    nullásitott = divide_list_by_nine(divided)
    print(nullásitott)
    print_board(nullásitott)
    dont_touch_coord = search_coordinates(nullásitott)
    while True:
        coordinates = validate_user_choice(nullásitott, dont_touch_coord)
        number = ask_num_from_1_to_9()
        filled = fill_board(coordinates, number, nullásitott)
        print_board(nullásitott)
        point_counter = check_win(nullásitott)
        print(point_counter)
        #merged_filled_array = merge_sudoku_array_together(nullásitott)
        if point_counter == 0:
            merged_filled_array = merge_sudoku_array_together(nullásitott)
            #how tocompare two array, weather the are same, or not
            print("You already guessed a word.")
            quit()




main()


# create_50_missing_middle = sorted(index_list[0:50])
# print(create_50_missing_middle)

# create_40_missing_easy = sorted(index_list[0:40])
# print(create_40_missing_easy)
