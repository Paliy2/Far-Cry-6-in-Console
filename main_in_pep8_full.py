    #!/usr/bin/python
# -*- coding: utf-8 -*-
#import random
#import math
import os
from assets import *


# getting system infornation
if __name__ == '__main__':
    if os.name == 'nt':
        systema = 'cls'
    elif os.name == 'posix':
        systema = 'clear'
    else:
        systema = '\33c'


# launch program
if __name__ == '__main__':
    #initialization   
    x = 0
    while x < 20:
        x += 1
        #print('Initialization... ')
        downloading(systema)


    # DATA

    limit_for_num = 3000

    Ulama = ulan_generator(limit_for_num)
    Prime = generate_prime(limit_for_num)
    Happy = generate_happy(limit_for_num)

    # -----------------------------------------------------------------|

    # Settings
    # global variables
    global opened_ulam
    opened_ulam = []
    global opened_happy
    opened_happy = []
    global opened_prime
    opened_prime = []
    global score
    score = 0
    # one of possible moves
    key_pressed = ''

    # swift initialization of game
    game_is_playing = True
    all_numbers = size_of_table(4, 4)
    a = len(all_numbers[0]) - 1
    spawn_number(all_numbers, a)
    spawn_number(all_numbers, a)

    # initialization finished

    # intro
    os.system(systema)
    print('Initialization finished')
    input('Press any key to continue... ')
    print('Now you are ready to start')
    input()
    os.system(systema)
    print()
    print("in old days... ")
    input()
    os.system(systema)
    print('\n\t\t\n')
    print("old \33[30mblack mage\33[0m cursed the world")
    input()
    print('And \33[31mNOW\33[0m')
    print('\n\t\33[34mYOU\33[0m must save the world')
    input()
    os.system(systema)
    print('''
    Game rule is very simple if you know what is 
    Ulama, Prime or Happy numbers.
    Don't you?
    Then try and learn, save \33[34mWORLD\33[37m from dAngEr!!!
    *** The world is corrupted if all fields of numbers are filled =( ***
    ''')
    input("  Yes, I'm in (press 'yes' \n  No, I'm in (press any key) ")

    # main loop of the program
    while game_is_playing:

        # show table of numbers
        output(all_numbers)
        # check if there is any 0 to contionue
        if check_for_lose(all_numbers):
            print('Evil wins, you are loser')
            break

        # show colour description
        colour_description()

        # show list of opened numbers

        print('\33[31mList of  Ulam numbers, you have opened:' \
            + str(sorted(opened_ulam)))
        print('\33[32mList of Prime numbers, you have opened:' \
            + str(sorted(opened_prime)))
        print('\33[34mList of Happy numbers, you have opened:' \
            + str(sorted(opened_happy)))

        # showing score in terminal
        show_score(score)

        # gets move from player
        x = 0
        while not key_get():
            x += 1
            key_get()

            # if player is uneble to make a move: break
            if x > 10:
                print('You lost, try again :(')
                break

        # making game physics - add to side

        if key_pressed == 'w':
            all_numbers = add_up(all_numbers)
        elif key_pressed == 's':
            all_numbers = add_down(all_numbers)
        elif key_pressed == 'a':
            all_numbers = add_left(all_numbers)
        elif key_pressed == 'd':
            all_numbers = add_right(all_numbers)

        # generate new numbers
        spawn_number(all_numbers, a)
        spawn_number(all_numbers, a)

        # clear terminal - not macos well-supported 
        os.system(systema)

print('game was hard, dont worry< all will be OK')
