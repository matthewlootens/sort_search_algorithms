def median_pivot(input_list, start, stop):
    """
    Returns: the index number of the median value of the first, middle,
    and last element of the list.
    """
    a = input_list[start]
    if abs(start - stop) % 2 == 1:
        b = input_list[(abs(stop - start) // 2) + start]
    else:
        b = input_list[((abs(stop - start) // 2) - 1) + start]
    c = input_list[stop - 1]
    if (a >= b and a <= c) or (a <= b and a >= c):
        return start
    if (b >= a and b <= c) or (b <= a and b >= c):
        if abs(start - stop) % 2 == 1:
            return (abs((stop - start)) // 2) + start
        else:
            return abs((((stop - start) // 2) - 1)) + start
    if (c >= a and c <= b) or (c <= a and c >= b):
        return stop - 1

def quick_sort(input_list, start, stop):
    """
    Uses the quicksort algorithm to sort a list in-place.
    Global variable 'comparisons' counts the number of comparisons needed to
    sort the array.
    """
    global comparisons
    if abs(stop - start) <= 1:
        return input_list
    else:
        #Three options to determine the pivot.
        #Change by commenting/uncommenting.

        #1. Median of first, middle, last (uses median_pivot subroutine)
        q = median_pivot(input_list, start, stop)#Returns the index of the median.
        p = input_list[q]
        input_list[start], input_list[q] = input_list[q], input_list[start]

        #2: End of list
        #p = input_list[stop - 1]
        #input_list[start], input_list[stop - 1] = input_list[stop - 1], input_list[start]

        #3: Beginning of list
        #p = input_list[start]

        comparisons += abs(stop - start) - 1
        i, j = start + 1, start + 1
        while j < stop:
            if input_list[j] > p:
                j += 1
            else:
                input_list[j], input_list [i] = input_list[i], input_list[j]
                j += 1
                i += 1
        input_list[start], input_list[i - 1] = input_list [i - 1], input_list[start]
        quick_sort(input_list, start, i-1)
        quick_sort(input_list, i, stop)
    return input_list

def quick_sort_wrapper(input_list):
    """
    Wrapper function
    """
    return quick_sort(input_list, 0, len(input_list))

def main():
    """
    Test suite and debugging tool
    Loads up data from datafile to check implementation and then does
    a sanity check to confirm list is indeed sorted.
    """
    file = 'quicksort_data.txt'
    datalist = []
    with open(file) as f:
        for line in f:
            datalist.append(int(line))
    #sortedlist = quick_sort(datalist, 0, len(datalist))
    sorted_list = quick_sort_wrapper(datalist)
    print(comparisons)

    #Confirm list is sorted
    a = sorted_list[0]
    for i in sorted_list:
        if i < a:
            print(i)
            a = i
        else:
            a = i
comparisons = 0
if __name__ == '__main__':
    main()
