import random

sudoku_array = []
sudoku_first_row = []


def generate_first_row():
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


def print_board(board):
    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

def main(arr):
    first_row = generate_first_row()
    sec_and_third = rotate_by_three(first_row)
    fourth = rotate_by_one(sec_and_third)
    fifth_and_sixth = rotate_by_three(fourth)
    seventh = rotate_by_one(fifth_and_sixth)
    eigtht_and_ninth = rotate_by_three(seventh)
    print_board(sudoku_array)

    
main(sudoku_array)
összevont_lista = []
for elem in sudoku_array:
    összevont_lista += elem
print(összevont_lista)

index_list = []
for i in range(0,81):
    index_list.append(i)
random.shuffle(index_list)

create_60_missing = sorted(index_list[0:60])
print(create_60_missing)

def valami():
    for i in range(len(összevont_lista)):
        for index in create_60_missing:
            if i == index:
                összevont_lista[i] = '.'
    return összevont_lista
            

print(valami())

def divide_list_by_nine(lista):
    divided_list = [lista[x:x+9] for x in range(0, len(lista), 9)]
    return divided_list

nullásitott = divide_list_by_nine(valami())

print_board(nullásitott)