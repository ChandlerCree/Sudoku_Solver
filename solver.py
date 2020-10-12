"""---------------------
## IMPORTED LIBRARIES ##
---------------------"""
from random import randint
# from random import seed


"""-------------------
## GLOBAL VARIABLES ##
-------------------"""
size = 9
box_size = 3

array_empty = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

array_0 = [
    [0, 6, 0, 3, 0, 0, 8, 0, 4],
    [5, 3, 7, 0, 9, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 6, 3, 0, 7],
    [0, 9, 0, 0, 5, 1, 2, 3, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 1, 3, 6, 2, 0, 0, 4, 0],
    [3, 0, 6, 4, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 6, 0, 5, 2, 3],
    [1, 0, 2, 0, 0, 9, 0, 8, 0]
]

array_1 = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

"""------------
## FUNCTIONS ##
------------"""


def check_board(array):
    loc = check_empty_loc(array)
    if not loc:
        return True
    else:
        row, col = loc

    for i in range(1, size + 1):
        if valid_assign(array, row, col, i):
            array[row][col] = i

            if check_board(array):
                return True

            array[row][col] = 0

    return False


def valid_assign(array, row, col, check_num):

    if check_row_duplicate(array, row, col, check_num):
        return False
    if check_col_duplicate(array, row, col, check_num):
        return False
    if check_box_duplicate(array, row - row % 3,
                           col - col % 3,
                           check_num):
        return False
    return True


def check_row_duplicate(array, row, col, check_num):
    for x in range(size):
        if array[row][x] == check_num and col != x:
            return True
    return False


def check_col_duplicate(array, row, col, check_num):
    for x in range(size):
        if array[x][col] == check_num and row != x:
            return True
    return False


def check_box_duplicate(array, row, col, check_num):
    col_box = col // 3
    row_box = row // 3

    for x in range(row_box * 3, row_box * 3 + 3):
        for y in range(col_box * 3, col_box * 3 + 3):
            if array[x][y] == check_num and (x, y) != (row, col):
                return True
    return False


def print_board(array):
    for x in range(size):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - -")

        for y in range(size):
            if y % 3 == 0 and y != 0:
                print("| ", end="")

            if y == size - 1:
                print(array[x][y])
            else:
                print(str(array[x][y]) + " ", end='')
    print("")


def check_empty_loc(array):
    for x in range(size):
        for y in range(size):
            if array[x][y] == 0:
                return x, y
    return None


def generate_board():
    for x in range(size):
        for y in range(size):
            r_int = randint(1, 9)

            if randint(1, 20) <= 9:
                if not check_row_duplicate(array_empty, x, y, r_int) and not check_col_duplicate(array_empty, x, y, r_int) and not check_box_duplicate(array_empty, x - x % 3, y - y % 3, r_int):
                    array_empty[x][y] = r_int
            else:
                array_empty[x][y] = 0

    print_board(array_empty)
    return array_empty


def check_possible_board(array):
    if(check_board(array)):
        print_board(array)
        print("There is a solution!")
    else:
        print("generating new board...")
        check_possible_board(check_board(generate_board()))
        # print("No Solution")


if __name__ == "__main__":
    #array = array_1
    array = generate_board()

    check_possible_board(array)

    # if(check_board(array)):
    #    print_board(array)
    #    print("There is a solution!")
    # else:
    #    print("generating new board...")
    #    check_board(generate_board())
    #    # print("No Solution")
    #    """
