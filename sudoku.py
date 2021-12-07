import random


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
    print(merge_sudoku_array)
    return merge_sudoku_array


def create_list_of_indices():
    index_list = []
    for i in range(0,81):
        index_list.append(i)
    random.shuffle(index_list)
    return index_list


def create_hard_board(indexlst):
    create_60_missing_hard = sorted(indexlst[0:60])
    print(create_60_missing_hard)
    return create_60_missing_hard

def create_dont_touch_numbers(indexlst):
    rest_indicies_of_hard = sorted(indexlst[60:])
    print(rest_indicies_of_hard)
    return rest_indicies_of_hard


def hide_numbers(merge_sudoku_array, lst_with_zeros):
    for i in range(len(merge_sudoku_array)):
        for index in lst_with_zeros:
            if i == index:
                merge_sudoku_array[i] = '.'
    return merge_sudoku_array


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


def main():
    generate_sudoku_array()
    print_board(sudoku_array)
    merged_array = merge_sudoku_array_together(sudoku_array)
    index_list = create_list_of_indices()
    hard_board = create_hard_board(index_list)
    create_dont_touch_numbers(index_list)
    divided = hide_numbers(merged_array, hard_board)
    nullásitott = divide_list_by_nine(divided)
    print(nullásitott)
    print_board(nullásitott)
    dont_touch_coord = search_coordinates(nullásitott)
    print(dont_touch_coord)


main()

def validate_user_choice(board):
    user_choice = ask_for_input()
    sorok_szama = len(board)
    oszlopok_szama = len(board[0])

    valid_rows = [i for i in alpha[0:oszlopok_szama]]
    valid_cols = [i for i in range(1,sorok_szama+1)]
    
    
    while True:
        if user_choice == "Q":
            print("Bye_bye!")
            quit()
        elif user_choice[0] in valid_rows and user_choice[1] in str(valid_cols):
            return user_choice
        else:
            print("Invalid input")
            user_choice = ask_for_input()
            continue

def ask_for_input():
    user_choice = input("Which tile do you want to reveal? ").upper()
    return user_choice

    
def set_coordinates(user_choice):

    a = alpha.index(user_choice[0])
    b = int(user_choice[1]) - 1
    
    return a,b


    
def write_first_letter(board,lst,x,y):
    board[x][y] = lst[x][y]
    return board[x][y]




# create_50_missing_middle = sorted(index_list[0:50])
# print(create_50_missing_middle)

# create_40_missing_easy = sorted(index_list[0:40])
# print(create_40_missing_easy)
