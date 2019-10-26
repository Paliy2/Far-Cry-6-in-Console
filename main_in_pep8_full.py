import random
import math


def type_of_number(number):
    """
    this function returns list of number`s type
    """
    type_of_number = []
    if number in Happy:
        type_of_number.append('H')
    if number in Prime:
        type_of_number.append('P')
    if number in Ulama:
        type_of_number.append('U')

    return type_of_number


def def_to_check(a, b):
    """
    this function checks if two numbers have any types in common
    """
    type_of_a = type_of_number(a)
    type_of_b = type_of_number(b)
    common_types = list(set(type_of_a).intersection(type_of_b))
    if len(common_types) > 0:
        return True
    elif a == 0 or b == 0:
        return True
    else:
        return False


def list_digits_of_num(num):
    """
    this function makes a list of digits of given number
    this function is neccesary for generating happy numbers
    """
    num_lenght = int(math.log10(num))+1
    digits_of_num = []
    m = 0
    while m < num_lenght:
        m += 1
        digits_of_num.append(0)

    for k in range(num_lenght):
        digit = num // 10 ** k % 10
        digits_of_num[num_lenght - (k + 1)] = digit
    return(digits_of_num)


def generate_happy(max):
    """
    this function generates list of happy numbers
    """
    happy = []
    for i in range(1, max):
        checker = 0
        a = len(list_digits_of_num(i))
        lap = 0
        m = i
        while lap < 100:
            lap += 1

            for k in range(a):
                checker += list_digits_of_num(m)[k] ** 2

            m = checker
            a = len(list_digits_of_num(m))

            if checker == 1:
                happy.append(i)
                break
            else:
                checker = 0
    return(happy)


def ulan_generator(max):
    """
    this function generates list of Ulam numbers
    """
    arr = [1, 2, 3]
    for i in range(4, max):
        sum_counter = 0
        for k in range(0, len(arr)):
            if (i - arr[k]) in arr and (arr[k] * 2) != i:
                sum_counter += 1
            if sum_counter > 2:
                break
        if sum_counter == 2:
            arr.append(i)
    return arr


def generate_prime(max):
    """
    this function generates list of prime numbers
    """
    prime_list = [2]
    for i in range(3, max):
        div_count = 0
        for k in range(2, i + 1):
            if (i % k) == 0:
                div_count += 1
            if div_count >= 2:
                break
        if div_count == 1:
            prime_list.append(i)
    return(prime_list)


def shift_num_right(lst):
    """
    this function shifts number right if the folowing number is 0
    >>> [0, 0, 1, 0]
    [0, 0, 0, 1]
    """
    for i in range(len(lst)):
        for k in range(3):
            if lst[i][k] != 0:
                while lst[i][k + 1] == 0:
                    lst[i][k+1] = lst[i][k]
                    lst[i][k] = 0
    return lst


def add_right(lst):
    """
    this function add neighbour numbers that have at least one type in common
    and shift the result to the right
    >>> [[1, 0, 1, 0], [7, 1, 1, 0], [7, 0, 1, 0], [0, 7, 1, 0]]
    [[0, 0, 0, 2], [0, 0, 7, 2], [0, 0, 0, 8], [0, 0, 0, 8]]
    """
    for i in range(4):
        lst = shift_num_right(lst)
    for i in range(4):
        if def_to_check(lst[i][2], lst[i][3]):
            lst[i][3] = lst[i][2] + lst[i][3]
            lst[i][2] = 0
            lst = shift_num_right(lst)

        if def_to_check(lst[i][1], lst[i][2]):
            lst[i][2] = lst[i][1] + lst[i][2]
            lst[i][1] = 0
            lst = shift_num_right(lst)

        if def_to_check(lst[i][0], lst[i][1]):
            lst[i][1] = lst[i][0] + lst[i][1]
            lst[i][0] = 0
            lst = shift_num_right(lst)

    return lst


def add_left(lst):
    """
    this function add neighbour numbers that have at least one type in common
    and shift the result to the left
    >>> [[1, 0, 1, 0], [7, 1, 1, 0], [7, 0, 1, 0], [0, 7, 1, 0]]
    [[2, 0, 0, 0], [8, 1, 0, 0], [8, 0, 0, 0], [8, 0, 0, 0]]
    """
    lst_reversed = []
    for i in range(len(lst)):
        lst_reversed.append(list(reversed(lst[i])))

    add_right(lst_reversed)

    lst_reversed_back = []
    for i in range(len(lst)):
        lst_reversed_back.append(list(reversed(lst_reversed[i])))

    return lst_reversed_back


def rotate_table(lst):
    """
    this function rotates table in order to make possible adding up or down
    """
    lst = lst[::-1]
    rotated_lst = []
    for k in range(len(lst)):
        column = []
        for i in range(len(lst)):
            column.append(lst[i][k])
        rotated_lst.append(column)

    return rotated_lst


def add_up(lst):
    """
    this function adds all possible numbers up
    """
    lst = add_right(rotate_table(lst))
    for i in range(3):
        lst = rotate_table(lst)
    return lst


def add_down(lst):
    """
    this function adds all possible numbers down
    """
    lst = add_left(rotate_table(lst))
    for i in range(3):
        lst = rotate_table(lst)
    return lst


def choose_number(U, P, H):
    """
    lst, lst, lst -> int

    chooses random number from Ulama orr Prime or Happy
    """
    gen_U = U[0:4]
    gen_P = P[0:4]
    gen_H = H[0:4]

    gn = random.randint(1, 3)
    if gn == 1:
        return(random.choice(gen_U))
    elif gn == 2:
        return(random.choice(gen_P))
    else:
        return(random.choice(gen_H))


def spawn_number(array, max_pos):
    """
    checks if can spawn in loop and adds 1 number to array
    index
    """
    while True:
        a = random.randint(0, max_pos)
        b = random.randint(0, max_pos)

        if array[a][b] != 0:
            a = random.randint(0, max_pos)
            b = random.randint(0, max_pos)

        if array[a][b] == 0:
            array[a][b] = choose_number(Ulama, Prime, Happy)
            return array


def key_get():
    """
    gets key to make a move soon
    """
    k = input('make your turn: ')
    k = k.lower()
    sett = ['w', 's', 'd', 'a']
    for i in sett:
        if k == i:
            global key_pressed
            key_pressed = k
            return True

    print("wrong key pressed. Click 'w', 's', 'd', 'a'")
    return False


# our table
def size_of_table(height, width):
    '''
    this fuction creates table with given height and width
    '''
    num_list = []
    for i in range(height):
        line = []
        for k in range(width):
            line.append(0)
        num_list.append(line)
    return num_list


def int_to_str(lst):
    '''
    complition for table function
    '''
    str_list = []
    for k in range(len(lst)):
        list_of_line = []
        for i in range(4):
            list_of_line.append(str(lst[k][i]))
        str_list.append(list_of_line)

    return(str_list)


def output(grid):
    '''
    outputs table 4x4 into screen
    '''
    grid = int_to_str(grid)
    print("\n")

    for i in range(len(grid)):
        res = "\t\t"
        for j in range(len(grid[i])):
            for _ in range(5 - len(grid[i][j])):
                res += " "
            res += grid[i][j] + " "
        print(res)
        print("\n")
    return 0

# DATA
limit_for_num = 999

Ulama = ulan_generator(limit_for_num)

Prime = generate_prime(limit_for_num)

Happy = generate_happy(limit_for_num)
# -----------------------------------------------------------------|

# Settings
# generates table
all_numbers = size_of_table(4, 4)
# one of possible moves
key_pressed = ''
# 'a' is the max position of all_numbers
a = len(all_numbers[0])-1
game_is_playing = True

# moves allowed
x = 0
while game_is_playing:
    output(all_numbers)
    x += 1
    if x == 100:
            break
    # gets move from player
    while not key_get():
        key_get()

    if key_pressed == 'w':
        all_numbers = add_up(all_numbers)
    elif key_pressed == 's':
        all_numbers = add_down(all_numbers)
    elif key_pressed == 'a':
        all_numbers = add_left(all_numbers)
    elif key_pressed == 'd':
        all_numbers = add_right(all_numbers)
    spawn_number(all_numbers, a)
