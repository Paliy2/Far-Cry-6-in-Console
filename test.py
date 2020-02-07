def is_palindrom(number):
    '''
    int -> bool
    check if function is palindrom
    >>> is_palindrom(1221)
    True
    >>> is_palindrom(1234)
    False
    '''
    if type(number) == int or type(number) == str:
        word = str(number)
        if word == word[::-1]:
            return True
    return False


def is_layland(number):
    if number <= 1:
        return False
    
    for x in range(2, number + 1):
        for y in range(x, number + 1):
            if x ** y + y ** x == number:
                return True
    return False


def get_X(layland):
    for i in range(100000, 10000, -1):
        if is_layland(i):
            for j in range(i - 1, 10000, -1):
                if is_layland(j):
                    number = i * j
                    if not is_palindrom(number):
                        return number
    return False


def get_alts(number, lst=[]):
    '''
    int, list -> list
    alternative numbers y and z for it
    that x * y make our number
    '''
    for x in range(1, number + 1):
        for y in range(x, number + 1):
            if x * y == number:
                lst.append((x, y))
    return lst


# print(get_X(layland))
def task_2():
    '''
    None -> None
    function gets Layland number and alternative numbers y and z for it
    that x * y make our Layland number
    '''
    layland = {}
    # for i in range(10000, 100000):
    #     if is_layland(i):
    #         layland.add(i)
    #         print(i)
    # print('all Layland numbers from your range')
    print(layland)

    X = get_X(layland)
    print(X)
    alts = get_alts(X)


task_2()
