def mergeSort(input_list):
    """
    input_list: a list of any n integers, duplicates allowed
    Returns a tuple:
        sorted list in non-decreasing order;
        and a count of inversions.
    """

    def merge(left_list, right_list):
        nonlocal inversion_count#Allows for this function to have closure
        sortedlist = []
        i, j = 0, 0
        while True:
            if left_list[i] <= right_list[j]:
                sortedlist.append(left_list[i])
                if i < len(left_list) - 1:#prevents falling off list
                    i += 1
                else:#If left is empty, append right directly.
                    sortedlist += right_list[j:]
                    break
            else:
                sortedlist.append(right_list[j])
                inversion_count += len(left_list) - i#Count inversions
                if j < len(right_list) - 1:
                    j += 1
                else:
                    sortedlist += left_list[i:]
                    break
        return sortedlist

    #####
    #Basecase and empty list
    #####
    if len(input_list) <= 1:
        inversion_count = 0
        return input_list, inversion_count

    #####
    #Recursive calls and book-keeping
    #####
    else:
        left_list, inversion_count = mergeSort(input_list[:len(input_list) // 2])
        #Need the right_list_tuple variable as a temp holder so that inversion_
        #count can be incremented.
        right_list_tuple = mergeSort(input_list[len(input_list) // 2:])
        right_list = right_list_tuple[0]
        inversion_count += right_list_tuple[1]
        sorted_list = merge(left_list, right_list)
        return sorted_list, inversion_count

if __name__ == '__main__':
    #Load in the data from a file
    filename = 'inversion_data.txt'
    with open(filename) as f:
        datalist = []
        for line in f:
            datalist.append(int(line))
    print(mergeSort(datalist)[1])#Correct answer: 2407905288 (2,407,905,288)
