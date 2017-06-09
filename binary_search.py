# -*- coding: utf-8 -*-

def binary_search(sorted_list, target):
    """
    Searches through a list for target.

    sorted_list: a non-empty list of non-decreasing ints, floats, or strings
    target: a literal of the same type as elements of sorted_list
    returns: a tuple (False) if the target is not in the list; (True, index_num)
    if the target is there.

    Duplicates are allowed, but if found, the index of an arbitrary duplicate
    element will be returned.

    Raises AssertionError if the passed list is empty.
    """

    #Initialize variables
    assert len(sorted_list) > 0
    min = 0
    max = len(sorted_list) - 1
    guess = (max + min) // 2

    #Main search function
    while True:
        if sorted_list[guess] == target:
            return (True, guess)
        elif max < min:
            return (False)
        elif sorted_list[guess] > target:
            max = guess - 1
            guess = (max + min) // 2
        else:
            min = guess + 1
            guess = (max + min) // 2

def main():
    """
    Test suite
    """
    a = [1,2,3,4,5,6,7,9]
    b = []
    c = [5,5,5,5,5]
    d = [5,5,5,5,5,6,7]

    print(binary_search(a, 5))#(True, 4)
    print(binary_search(a, 10))#False
    try:
        print(binary_search(b, 7))
    except AssertionError:
        print("AssertionError raised.")#"AssertionError raised."
    print(binary_search(c, 5))#(True, 2)
    print(binary_search(d, 5))#(True, 3)


#Test suite
if __name__ == '__main__':
    main()
