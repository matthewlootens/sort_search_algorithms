def merge(left_list, right_list, inversion_count = 0):
    sortedlist = []
    i, j = 0, 0
    #while i < (len(right_list)) or j < (len(left_list)):
    while True:
        if left_list[i] <= right_list[j]:
            sortedlist.append(left_list[i])
            if i < len(left_list) - 1:#prevents falling off list
                i += 1
            else:#if right_list is empty, append remainder of left_list to sortedlist
                sortedlist += right_list[j:]
                break
        else:
            sortedlist.append(right_list[j])
            #inversion_count += len(left_list) - i
            if j < len(left_list) - 1:
                j += 1
            else:
                sortedlist += left_list[i:]
                break
    # if len(sortedlist) == len(standard):
    #      print "Final Result: " + str(inverse)
    return sortedlist

def mergeSort(list, inversion_count = 0):
    """list: a list of any n integers, duplicates allowed
    Returns a sorted list in non-decreasing order."""
    #Handles the base case and empty lists.
    if len(list) <= 1:
        return list
    else:
        x = len(list)
        left_list = mergeSort(list[0:(x // 2)])
        right_list = mergeSort(list[(x // 2):x + 1])

        return merge(left_list, right_list)

if __name__ == '__main__':
    #inverse = 0
    #file = 'inversion_data.txt'
    # datafile = open(file)
    # datalist = []
    # for line in datafile:
    #     datalist.append(int(line))
    # standard = len(datalist)

    num_list = [6, -3, 213, 4, 403, 1000, 2, 0, 50, -12, 34, 34, 45, 32, -12, 0]
    #num_list = [4,3,2,1]
    print(mergeSort(num_list))
