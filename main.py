import random

def type_of_number(number, Ulama, Prime, Happy):
    pass
    return type_of_number

#complition for taple function                                                          TABLE COMPLITION
def output(lst):
    '''
    Outputs number table to console
    '''
    for i in lst:
        print(i)
        
def ulan_generator(max):
#this function generates list of Ulam numbers                                            ULAM NUMBERS
    arr = [1, 2, 3]
    for i in range(4, max):
        sum_counter = 0
        for k in range(0, len(arr)):
            if (i - arr[k]) in arr and (arr[k]*2) != i:
                sum_counter +=1
            if sum_counter > 2:
                break
        if sum_counter == 2 :
            arr.append(i)
    return arr

def generate_prime(max):

#this function generates list of prime numbers                                           PRIME NUMBERS
    
    prime_list = [2]
    for i in range(3, max):
        div_count = 0
        for k in range(2, i+1):
            if (i % k) == 0:
                div_count += 1
            if div_count >= 2:
                break    
        if div_count == 1:
            prime_list.append(i)
    return(prime_list)
 
# main loop of the gameimport random
def sum_one_lst(lst):
    summa = 0
    for i in lst:
        summa += i
    return summa

#try complete this
def add_up(lst):
    """
    lst -> lst
    adds all possible numbers in down-up order
    """
    # стовпчики
    l1 = [0, 0, 0, 0]
    l2 = [0, 0, 0, 0]
    l3 = [0, 0, 0, 0]
    l4 = [0, 0, 0, 0]
    #отримати стовпчики чисел
    for i in range(0, 4):
        l1[i] = (lst[i][0])
        l2[i] = lst[i][1]
        l3[i] = lst[i][2]
        l4[i] = lst[i][3]

    lst[0][0] = sum_one_lst(l1)
    lst[0][1] = sum_one_lst(l2)
    lst[0][2] = sum_one_lst(l3)
    lst[0][3] = sum_one_lst(l4)
    lst[1] = [0,0,0,0]
    lst[2] = [0,0,0,0]
    lst[3] = [0,0,0,0]
    
    return lst 

def add_down(lst):
    return lst
    pass
   
def add_left(lst):
    return lst
    pass

def add_right(lst):
    return lst
    pass
            
def choose_number(ul, pr, hp):
    """
    lst, lst, lst -> int
    
    chooses random number from Ulama orr Prime or Happy
    """
    gn = random.randint(1, 3)
    if gn == 1:
        return(random.choice(ul)) 
    elif gn == 2:
        return(random.choice(pr))
    else:
        return(random.choice(hp))

def spawn_number(array, max_pos):
    #checks if can spawn in loop and adds 1 number to array
    #index
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
    #gets key to make a move soon
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

#this fuction creates table with given height and width                              TABLE SIZE
    
    num_list = []
    
    for i in range(height):
        line = []
        for k in range(width):
            line.append(0)  
        num_list.append(line)
    return num_list


#DATA
Ulama = ulan_generator(300)


Prime = generate_prime(300)

Happy = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100,
     103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230,
      236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338 ]

#-------------------------------------------------------------------------------------|

#Settings
#generates table
all_numbers = size_of_table(4,4)
#one of possible moves
key_pressed = ''
#'a' is the max position of all_numbers
a = len(all_numbers[0])-1
game_is_playing = True

#moves allowed
x = 0
while game_is_playing:
    x += 1
    if x == 100:
            break
    #spawn number
    spawn_number(all_numbers, a)
    #geys move from player
    while not key_get():
        key_get()
    
    output(all_numbers)

    if key_pressed == 'w':
        all_numbers = add_up(all_numbers)
    elif key_pressed == 's':
        all_numbers = add_down(all_numbers)
    elif key_pressed == 'a':
        all_numbers = add_left(all_numbers)
    elif key_pressed == 'd':
        all_numbers = add_right(all_numbers)
    #print table    
    